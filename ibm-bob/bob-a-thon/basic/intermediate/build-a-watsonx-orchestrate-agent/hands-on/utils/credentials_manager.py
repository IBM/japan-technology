"""
Credentials Manager Module

Manager for loading and validating WxO credentials from environment variables.

Author: Elena Lowery
AI Assistant: Bob
"""

import os
from pathlib import Path
from pydantic import SecretStr
from dotenv import load_dotenv
from utils.wxo_config import WxOConfig


class CredentialsManager:
    """Manager for loading and validating WxO credentials from environment variables."""
    
    def __init__(self, cache_path: str = "./current_token.txt", ttl_seconds: int = 300):
        """
        Initialize the CredentialsManager.
        
        Args:
            cache_path: Path to the token cache file
            ttl_seconds: Time-to-live for cached tokens in seconds
        """
        self.cache_path = Path(cache_path)
        self.ttl_seconds = ttl_seconds
        self._config = None
    
    def load_credentials(self) -> WxOConfig:
        """
        Load configuration from environment variables and validate.
        
        Returns:
            WxOConfig: Validated configuration object
            
        Raises:
            ValueError: If required environment variables are missing or invalid
        """
        load_dotenv()

        cloud_provider = os.getenv("CLOUD_PROVIDER")
        agent_url = os.getenv("AGENT_URL")
        wxo_api_key = os.getenv("WXO_API_KEY")
        ibm_auth_endpoint = os.getenv("IBM_AUTH_ENDPOINT")
        aws_auth_endpoint = os.getenv("AWS_AUTH_ENDPOINT")

        # Validate required environment variables
        if not all([cloud_provider, agent_url, wxo_api_key]):
            raise ValueError("Missing required environment variables: CLOUD_PROVIDER, AGENT_URL, or WXO_API_KEY")
        
        if cloud_provider == "ibm" and not ibm_auth_endpoint:
            raise ValueError("IBM_AUTH_ENDPOINT is required when CLOUD_PROVIDER is 'ibm'")
        
        if cloud_provider == "aws" and not aws_auth_endpoint:
            raise ValueError("AWS_AUTH_ENDPOINT is required when CLOUD_PROVIDER is 'aws'")

        # choose endpoint based on provider
        auth_endpoint = ibm_auth_endpoint if cloud_provider == "ibm" else aws_auth_endpoint
        
        # Type assertions after validation
        assert cloud_provider is not None
        assert auth_endpoint is not None
        assert wxo_api_key is not None
        assert agent_url is not None

        self._config = WxOConfig(
            PROVIDER=cloud_provider,
            TOKEN_ENDPOINT=auth_endpoint,
            API_KEY=SecretStr(wxo_api_key),
            CACHE_PATH=self.cache_path,
            TTL_SECONDS=self.ttl_seconds,
            AGENT_URL=agent_url
        )

        return self._config
    
    def get_config(self) -> WxOConfig:
        """
        Get the current configuration, loading it if not already loaded.
        
        Returns:
            WxOConfig: The configuration object
        """
        if self._config is None:
            return self.load_credentials()
        return self._config
    
    @staticmethod
    def get_credentials() -> WxOConfig:
        """
        Static method for backward compatibility.
        Load configuration from environment variables and validate.
        
        Returns:
            WxOConfig: Validated configuration object
        """
        manager = CredentialsManager()
        return manager.load_credentials()


# Backward compatibility: keep the function for existing code
def get_credentials() -> WxOConfig:
    """
    Load configuration from environment variables and validate.
    This function is kept for backward compatibility.
    
    Returns:
        WxOConfig: Validated configuration object
    """
    return CredentialsManager.get_credentials()

# Made with Bob
