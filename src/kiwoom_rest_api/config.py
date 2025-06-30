import os
from typing import Optional


# Base URLs
DEFAULT_BASE_URL = os.environ.get("KIWOOM_DEFAULT_BASE_URL", "https://api.kiwoom.com")
SANDBOX_BASE_URL = os.environ.get("KIWOOM_SANDBOX_BASE_URL", "https://mockapi.kiwoom.com")

# WebSocket URLs
DEFAULT_WS_URL = os.environ.get("KIWOOM_DEFAULT_WS_URL", "wss://api.kiwoom.com:10000")
SANDBOX_WS_URL = os.environ.get("KIWOOM_SANDBOX_WS_URL", "wss://mockapi.kiwoom.com:10000")
WS_ENDPOINT = "/api/dostk/websocket"

# API Credentials
API_KEY = os.environ.get("KIWOOM_API_KEY", "")
API_SECRET = os.environ.get("KIWOOM_API_SECRET", "")

# Authentication
TOKEN_URL = "/oauth2/token"
AUTH_URL = "/oauth2/authorize"

# Timeouts
DEFAULT_TIMEOUT = 30.0  # seconds
WS_TIMEOUT = 10.0  # seconds

# Environment setting
USE_SANDBOX = os.environ.get("KIWOOM_USE_SANDBOX", "false").lower() == "true"

def get_base_url() -> str:
    """Return the base URL based on environment settings"""
    if USE_SANDBOX:
        return SANDBOX_BASE_URL
    return DEFAULT_BASE_URL

def get_ws_url() -> str:
    """Return the WebSocket URL based on environment settings"""
    base_ws_url = SANDBOX_WS_URL if USE_SANDBOX else DEFAULT_WS_URL
    return f"{base_ws_url}{WS_ENDPOINT}"

def get_api_key() -> str:
    """Return the API key"""
    return API_KEY

def get_api_secret() -> str:
    """Return the API secret"""
    return API_SECRET

def get_headers(access_token: Optional[str] = None) -> dict:
    """Return common headers for API requests"""
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
    }
    
    if access_token:
        headers["Authorization"] = f"Bearer {access_token}"
    else:
        headers["appkey"] = get_api_key()
        headers["appsecret"] = get_api_secret()
    
    return headers
