"""
Token Manager Module

Token Manager supporting IBM IAM and AWS custom JWT endpoints with automatic
caching in memory and on disk.

Author: Elena Lowery
AI Assistant: Bob
"""

from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Optional, Any

import requests
from pydantic import SecretStr

logger = logging.getLogger(__name__)

class TokenManager:
    """
    Token Manager supporting IBM IAM and AWS custom JWT endpoints.

    - Automatically caches tokens in memory and on disk.
    - Public function: `get_token()`
    """

    def __init__(self, config) -> None:
        self.config = config
        self.token: Optional[str] = None
        self.token_expiry: Optional[datetime] = None

        self._load_from_file()

    # =====================================================================
    # Public API
    # =====================================================================

    def get_token(self) -> str:
        """Return a valid token, refreshing it if needed."""
        if self._is_expired():
            logger.debug("Loading token from file cache")
            self._load_from_file()

        if self._is_expired():
            logger.info("Generating new token")
            self._refresh()

        return self.token  # type: ignore

    # =====================================================================
    # Token Refresh Logic
    # =====================================================================

    def _refresh(self) -> None:
        """Get a new token from IBM or AWS."""

        provider = self.config.PROVIDER.lower()
        url = self.config.TOKEN_ENDPOINT
        api_key = self._extract_key(self.config.API_KEY)

        logger.info("Requesting new %s token from %s", provider.upper(), url)

        now = datetime.now(timezone.utc)

        if provider == "ibm":
            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Accept": "application/json",
                },
                data={
                    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                    "apikey": api_key,
                },
                timeout=30,
            )

        elif provider == "aws":
            response = requests.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={"apikey": api_key},
                timeout=30,
            )

        else:
            raise ValueError(f"Unsupported provider: {self.config.PROVIDER}")

        response.raise_for_status()
        payload = response.json()

        token = payload.get("access_token") or payload.get("token")
        expires_in = int(payload.get("expires_in", self.config.TTL_SECONDS))
        expiry = now + timedelta(seconds=expires_in)

        self.token = token
        self.token_expiry = expiry

        self._save_to_file(token)
        logger.info("New %s token acquired (TTL=%ds)", provider.upper(), expires_in)

    # =====================================================================
    # Cache
    # =====================================================================

    def _is_expired(self) -> bool:
        if not self.token or not self.token_expiry:
            return True
        return datetime.now(timezone.utc) >= self.token_expiry

    def _load_from_file(self) -> None:
        """Load cached token from disk if still valid."""
        path = self.config.CACHE_PATH
        if not path.is_file():
            return

        try:
            mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
            age = (datetime.now(timezone.utc) - mtime).total_seconds()

            if age < self.config.TTL_SECONDS:
                with path.open("r", encoding="utf-8") as f:
                    cached = f.read().strip()

                if cached:
                    self.token = cached
                    self.token_expiry = mtime + timedelta(seconds=self.config.TTL_SECONDS)
                    logger.debug("Loaded token from file cache.")
        except Exception as exc:
            logger.debug("Failed to read token cache: %s", exc)

    def _save_to_file(self, token: str) -> None:
        """Save token to disk."""
        try:
            with self.config.CACHE_PATH.open("w", encoding="utf-8") as f:
                f.write(token)
        except Exception as exc:
            logger.debug("Failed to write token cache: %s", exc)

    # =====================================================================
    # Utils
    # =====================================================================

    @staticmethod
    def _extract_key(value: Any) -> str:
        if isinstance(value, SecretStr):
            return value.get_secret_value()
        if isinstance(value, str):
            return value
        raise TypeError("API_KEY must be a SecretStr or str")
