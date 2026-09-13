"""
WxO Agent Adapter Module

This module provides a class-based adapter for interacting with the WxO Agent API,
managing credentials, tokens, and API communication.

Author: Elena Lowery
AI Assistant: Bob
"""

import requests
import json
import sys
import io
from utils.credentials_manager import CredentialsManager
from utils.token_manager import TokenManager

# Set UTF-8 encoding for stdout to handle Unicode characters on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


class WxOAgentAdapter:
    """
    Adapter class for interacting with WxO Agent API.
    Manages credentials, tokens, and API communication.
    """
    
    def __init__(self, cache_path: str = "./current_token.txt", ttl_seconds: int = 300):
        """
        Initialize the WxO Agent Adapter.
        
        Args:
            cache_path: Path to the token cache file
            ttl_seconds: Time-to-live for cached tokens in seconds
        """
        # Initialize credentials manager
        self.credentials_manager = CredentialsManager(
            cache_path=cache_path,
            ttl_seconds=ttl_seconds
        )
        
        # Load configuration
        self.config = self.credentials_manager.load_credentials()
        
        # Initialize token manager
        self.token_manager = TokenManager(self.config)
    
    def get_token(self) -> str:
        """
        Get a valid authentication token.
        
        Returns:
            str: Valid authentication token
        """
        return self.token_manager.get_token()
    
    def route_to_wxo_streaming(self, user_message: str, thread_id: str | None = None):
        """
        Route user message to WxO agent API and stream the response.
        
        Args:
            user_message: The user's input message
            thread_id: Optional thread ID for conversation continuity
            
        Yields:
            dict: Streaming chunks with 'content' and optionally 'thread_id'
                  Format: {'content': str, 'thread_id': str (optional), 'done': bool}
        """
        # Get fresh token
        token = self.get_token()
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        # Add thread ID if we have one from previous interactions
        if thread_id:
            headers["X-IBM-THREAD-ID"] = thread_id

        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "response_type": "text",
                            "text": user_message
                        }
                    ]
                }
            ],
            "additional_parameters": {},
            "context": {},
            "stream": "true"
        }

        # Make the POST request with stream=True
        with requests.post(
            self.config.AGENT_URL,
            headers=headers,
            json=payload,
            stream=True
        ) as response:
            response.raise_for_status()

            returned_thread_id = None

            # Stream each line as it arrives
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    try:
                        # The API often prefixes streaming lines with 'data: '
                        if line.startswith("data: "):
                            line = line[len("data: "):]

                        obj = json.loads(line)
                        
                        # Capture thread_id from response
                        if "thread_id" in obj and not returned_thread_id:
                            returned_thread_id = obj["thread_id"]
                        
                        for choice in obj.get("choices", []):
                            delta = choice.get("delta", {})
                            if delta.get("role") == "assistant" and "content" in delta:
                                content = delta["content"]
                                
                                # Yield the streaming chunk
                                chunk = {'content': content, 'done': False}
                                if returned_thread_id:
                                    chunk['thread_id'] = returned_thread_id
                                
                                yield chunk
                    except json.JSONDecodeError as e:
                        # Log decode errors for debugging
                        print(f"Warning: Failed to parse JSON line: {e}")
                        continue
            
            # Yield final chunk to signal completion
            final_chunk = {'content': '', 'done': True}
            if returned_thread_id:
                final_chunk['thread_id'] = returned_thread_id
            yield final_chunk
