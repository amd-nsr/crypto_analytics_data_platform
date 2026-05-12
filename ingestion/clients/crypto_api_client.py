import json
import requests
from datetime import datetime, timezone
from ingestion.config.settings import API_URL


def fetch_crypto_prices():

    response = requests.get(API_URL, timeout=30)

    response.raise_for_status()

    data = response.json()

    now = datetime.now(tz=timezone.utc)    
    enriched_data = {
        "symbol": data.get("symbol"),
        "price": float(data.get("price")),
        "timestamp": now.isoformat()
    }
    
    return enriched_data
