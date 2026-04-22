import requests
import logging
import hmac
import hashlib
import time
from urllib.parse import urlencode
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    """Binance Futures Testnet API Client"""

    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        logger.info("BinanceFuturesClient initialized")

    def _generate_signature(self, params: Dict) -> str:
        """Generate HMAC-SHA256 signature"""
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, **params) -> Dict:
        """Place an order on Binance Futures Testnet"""
        try:
            endpoint = f"{self.BASE_URL}/fapi/v1/order"

            # Add timestamp
            params['timestamp'] = int(time.time() * 1000)

            # Sign request
            signature = self._generate_signature(params)
            params['signature'] = signature

            headers = {'X-MBX-APIKEY': self.api_key}

            logger.debug(f"Sending request to {endpoint} with params: {params}")

            response = self.session.post(
                endpoint,
                params=params,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()
            result = response.json()
            logger.info(f"Order placed successfully. Response: {result}")
            return result

        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {str(e)}", exc_info=True)
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            raise