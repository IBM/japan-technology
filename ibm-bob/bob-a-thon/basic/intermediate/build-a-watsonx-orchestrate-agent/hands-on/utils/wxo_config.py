"""
WxO Configuration Module

Configuration model for WxO API settings using Pydantic.

Author: Elena Lowery
AI Assistant: Bob
"""

from pydantic import BaseModel, SecretStr
from pathlib import Path

class WxOConfig(BaseModel):
    PROVIDER: str
    TOKEN_ENDPOINT: str
    API_KEY: SecretStr
    CACHE_PATH: Path
    TTL_SECONDS: int = 300
    AGENT_URL: str
