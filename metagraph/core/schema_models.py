from __future__ import annotations
from typing import Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime


LayerType = Literal["pm", "scrum", "docs", "system"]
StatusType = Literal["active", "draft", "blocked", "done", "archived"]


class NodeModel(BaseModel):
    id: str
    type_id: str
    title: str
    body: str = ""
    status: StatusType = "active"
    priority: int = Field(default=3, ge=1, le=5)
    metadata: dict = Field(default_factory=dict)
    layer: LayerType
    source_file: Optional[str] = None
    source_section: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class EdgeModel(BaseModel):
    id: str
    from_node: str
    to_node: str
    type_id: str
    weight: float = 1.0
    label: Optional[str] = None
    metadata: dict = Field(default_factory=dict)
    created_at: Optional[str] = None


class CreateNodeRequest(BaseModel):
    type_id: str
    title: str
    body: str = ""
    status: StatusType = "active"
    priority: int = Field(default=3, ge=1, le=5)
    metadata: dict = Field(default_factory=dict)
    source_file: Optional[str] = None
    source_section: Optional[str] = None


class CreateEdgeRequest(BaseModel):
    from_node: str
    to_node: str
    type_id: str
    weight: float = 1.0
    label: Optional[str] = None
