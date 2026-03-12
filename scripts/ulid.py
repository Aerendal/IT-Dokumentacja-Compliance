import os
import time

_CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def _encode_base32(data: bytes) -> str:
    n = int.from_bytes(data, "big")
    out = []
    for _ in range(26):
        out.append(_CROCKFORD[n & 31])
        n >>= 5
    return "".join(reversed(out))


def ulid() -> str:
    ms = int(time.time() * 1000) & ((1 << 48) - 1)
    ts = ms.to_bytes(6, "big")
    rnd = os.urandom(10)
    return _encode_base32(ts + rnd)
