from app import app
import urllib.request,json
from .models import sources

Source = sources.Source
api_key = api_config['NEWS_API_KEY']
base_url =app.config["NEWS_API_BASE_URL"]