import hashlib
from typing import Any

def calculate_hash(data: Any) -> str:
    """Fungsi bantuan untuk menghitung hash"""
    return hashlib.sha256(str(data).encode()).hexdigest()