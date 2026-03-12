---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-077: Model Explainability Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-077 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead / Ethics] |

---

## 1. Explainability Requirements

### 1.1 Requirements by Model Tier

| Tier | Requirement | Methods |
|------|-------------|---------|
| Tier 1 (Critical) | Full explainability | SHAP, LIME, Counterfactuals |
| Tier 2 (Important) | Feature importance | SHAP, Permutation |
| Tier 3 (Standard) | Basic feature importance | Built-in importance |
| Tier 4 (Experimental) | Optional | Any |

### 1.2 Regulatory Requirements

| Regulation | Requirement |
|------------|-------------|
| GDPR Art. 22 | Right to explanation for automated decisions |
| EU AI Act | Transparency for high-risk AI |
| FCRA | Adverse action reasons for credit |
| ECOA | Non-discrimination explanation |

---

## 2. Explainability Methods

### 2.1 SHAP (SHapley Additive exPlanations)

```python
# explainability/shap_explainer.py
import shap
import mlflow
import numpy as np
import pandas as pd

class SHAPExplainer:
    """SHAP-based model explainability."""
    
    def __init__(self, model, background_data: pd.DataFrame):
        self.model = model
        self.explainer = shap.Explainer(model, background_data)
    
    def explain_prediction(self, instance: pd.DataFrame) -> dict:
        """Generate SHAP explanation for single prediction."""
        shap_values = self.explainer(instance)
        
        # Get feature contributions
        contributions = {}
        for i, feature in enumerate(instance.columns):
            contributions[feature] = {
                'value': float(instance.iloc[0, i]),
                'shap_value': float(shap_values.values[0, i]),
                'impact': 'positive' if shap_values.values[0, i] > 0 else 'negative'
            }
        
        # Sort by absolute impact
        sorted_features = sorted(
            contributions.items(),
            key=lambda x: abs(x[1]['shap_value']),
            reverse=True
        )
        
        return {
            'base_value': float(shap_values.base_values[0]),
            'prediction': float(self.model.predict(instance)[0]),
            'top_features': dict(sorted_features[:10]),
            'all_features': contributions
        }
    
    def generate_global_explanation(self, data: pd.DataFrame) -> dict:
        """Generate global feature importance."""
        shap_values = self.explainer(data)
        
        # Mean absolute SHAP values
        importance = np.abs(shap_values.values).mean(axis=0)
        
        return {
            'feature_importance': dict(zip(data.columns, importance.tolist())),
            'summary_plot_data': {
                'shap_values': shap_values.values.tolist(),
                'features': data.values.tolist(),
                'feature_names': data.columns.tolist()
            }
        }
    
    def log_to_mlflow(self, explanation: dict, run_id: str):
        """Log explanation artifacts to MLflow."""
        with mlflow.start_run(run_id=run_id):
            mlflow.log_dict(explanation, "explanation/shap_explanation.json")
            
            # Generate and log summary plot
            fig = shap.summary_plot(
                explanation['summary_plot_data']['shap_values'],
                explanation['summary_plot_data']['features'],
                feature_names=explanation['summary_plot_data']['feature_names'],
                show=False
            )
            mlflow.log_figure(fig, "explanation/shap_summary.png")
```

### 2.2 LIME (Local Interpretable Model-agnostic Explanations)

```python
# explainability/lime_explainer.py
import lime
import lime.lime_tabular

class LIMEExplainer:
    """LIME-based model explainability."""
    
    def __init__(self, model, training_data: pd.DataFrame, 
                 feature_names: list, class_names: list = None):
        self.model = model
        self.explainer = lime.lime_tabular.LimeTabularExplainer(
            training_data.values,
            feature_names=feature_names,
            class_names=class_names or ['Class 0', 'Class 1'],
            mode='classification'
        )
    
    def explain_prediction(self, instance: np.ndarray, num_features: int = 10) -> dict:
        """Generate LIME explanation for single prediction."""
        explanation = self.explainer.explain_instance(
            instance,
            self.model.predict_proba,
            num_features=num_features
        )
        
        return {
            'prediction': int(self.model.predict([instance])[0]),
            'prediction_proba': self.model.predict_proba([instance])[0].tolist(),
            'feature_contributions': explanation.as_list(),
            'intercept': explanation.intercept,
            'local_prediction': explanation.local_pred[0]
        }
```

### 2.3 Counterfactual Explanations

```python
# explainability/counterfactual.py
import dice_ml
from dice_ml import Dice

class CounterfactualExplainer:
    """Counterfactual explanation generator."""
    
    def __init__(self, model, data: pd.DataFrame, 
                 continuous_features: list, outcome_name: str):
        self.dice_data = dice_ml.Data(
            dataframe=data,
            continuous_features=continuous_features,
            outcome_name=outcome_name
        )
        self.dice_model = dice_ml.Model(model=model, backend='sklearn')
        self.explainer = Dice(self.dice_data, self.dice_model)
    
    def generate_counterfactuals(self, instance: pd.DataFrame, 
                                 desired_outcome: int,
                                 num_counterfactuals: int = 3) -> dict:
        """Generate counterfactual explanations."""
        cf = self.explainer.generate_counterfactuals(
            instance,
            total_CFs=num_counterfactuals,
            desired_class=desired_outcome
        )
        
        return {
            'original_instance': instance.to_dict(orient='records')[0],
            'original_prediction': int(self.dice_model.get_output(instance)[0]),
            'counterfactuals': cf.cf_examples_list[0].final_cfs_df.to_dict(orient='records'),
            'changes_needed': self._get_changes(instance, cf)
        }
    
    def _get_changes(self, original, counterfactuals) -> list:
        """Extract what changes are needed."""
        changes = []
        cf_df = counterfactuals.cf_examples_list[0].final_cfs_df
        
        for _, cf_row in cf_df.iterrows():
            cf_changes = {}
            for col in original.columns:
                if original[col].values[0] != cf_row[col]:
                    cf_changes[col] = {
                        'from': original[col].values[0],
                        'to': cf_row[col]
                    }
            changes.append(cf_changes)
        
        return changes
```

---

## 3. Explanation API

### 3.1 Explanation Service

```python
# explainability/service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(title="Model Explanation Service")

class ExplanationRequest(BaseModel):
    model_name: str
    model_version: str
    instances: List[Dict[str, Any]]
    explanation_type: str = "shap"  # shap, lime, counterfactual

class ExplanationResponse(BaseModel):
    model_name: str
    model_version: str
    explanations: List[Dict[str, Any]]

@app.post("/explain", response_model=ExplanationResponse)
async def explain_predictions(request: ExplanationRequest):
    """Generate explanations for predictions."""
    
    # Load model and explainer
    model = load_model(request.model_name, request.model_version)
    explainer = get_explainer(model, request.explanation_type)
    
    # Generate explanations
    explanations = []
    for instance in request.instances:
        df = pd.DataFrame([instance])
        explanation = explainer.explain_prediction(df)
        explanations.append(explanation)
    
    return ExplanationResponse(
        model_name=request.model_name,
        model_version=request.model_version,
        explanations=explanations
    )
```

---

## 4. Human-Readable Explanations

### 4.1 Natural Language Generation

```python
# explainability/natural_language.py
def generate_natural_explanation(shap_explanation: dict, 
                                 feature_descriptions: dict) -> str:
    """Generate human-readable explanation."""
    
    prediction = shap_explanation['prediction']
    top_features = list(shap_explanation['top_features'].items())[:5]
    
    # Determine prediction outcome
    if prediction == 1:
        outcome = "flagged as potentially fraudulent"
        threshold_msg = "above our risk threshold"
    else:
        outcome = "classified as legitimate"
        threshold_msg = "below our risk threshold"
    
    explanation = f"This transaction was {outcome}. "
    explanation += f"The risk score is {threshold_msg}.\n\n"
    explanation += "The main factors influencing this decision were:\n"
    
    for i, (feature, details) in enumerate(top_features, 1):
        feature_desc = feature_descriptions.get(feature, feature)
        value = details['value']
        impact = details['impact']
        
        if impact == 'positive':
            direction = "increased"
        else:
            direction = "decreased"
        
        explanation += f"{i}. {feature_desc}: {value} - This {direction} the risk score.\n"
    
    return explanation

# Example feature descriptions
FEATURE_DESCRIPTIONS = {
    'transaction_amount': 'Transaction amount',
    'user_account_age_days': 'Account age (days)',
    'transaction_velocity_1h': 'Number of transactions in the last hour',
    'device_trust_score': 'Device trust score',
    'location_risk_score': 'Location risk score'
}
```

---

## 5. Model Cards with Explainability

### 5.1 Model Card Template

```yaml
# model_card.yaml
model_details:
  name: "Fraud Detection Model"
  version: "2.1.0"
  type: "Binary Classification"
  
explainability:
  methods_available:
    - type: "SHAP"
      description: "Feature-level attribution for individual predictions"
      latency: "~50ms per prediction"
    - type: "Feature Importance"
      description: "Global feature importance ranking"
      
  key_features:
    - name: "transaction_amount"
      importance_rank: 1
      description: "Higher amounts increase fraud risk"
    - name: "transaction_velocity"
      importance_rank: 2
      description: "Rapid transactions increase fraud risk"
      
  limitations:
    - "Explanations are approximations and may not capture all model behavior"
    - "Feature interactions may not be fully captured"
    
  example_explanation: |
    "This transaction was flagged because:
    1. Transaction amount ($5,000) is unusually high for this user
    2. 5 transactions in the last hour (typical: 1-2)
    3. New device not previously seen"
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial explainability guide |
