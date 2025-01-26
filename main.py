from flask import Flask, json, request, jsonify
import asyncio
import httpx
import re
import logging
from nested_lookup import nested_lookup
import random
from fake_useragent import UserAgent

ua = UserAgent()


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = Flask(__name__)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

client = httpx.AsyncClient(
    http2=True,
    follow_redirects=True,
    headers={
        "User-Agent": ua.random,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    },
)

logger.debug(f"Request Headers: {client.headers}")


async def human_delay(min_delay=2, max_delay=5):
    await asyncio.sleep(random.uniform(min_delay, max_delay))


def extract_next_data(html: str) -> dict:
    """Multiple strategies to extract Next.js data"""
    strategies = [
        # Direct __NEXT_DATA__ script tag
        lambda h: re.search(
            r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.DOTALL),
        # Fallback to data-name attribute
        lambda h: re.search(
            r'<script data-name="query"[^>]*>(.*?)</script>', h, re.DOTALL),
        # Look for JSON-like structure with product data
        lambda h: re.search(r'\{.*"product":\s*{[^}]+}\s*\}', h, re.DOTALL)
    ]

    for strategy in strategies:
        match = strategy(html)
        if match:
            try:
                data_str = match.group(1)
                # Clean and parse JSON
                data_str = re.sub(
                    r'^\s*window\.__NEXT_DATA__\s*=\s*', '', data_str.strip())
                data_str = data_str.rstrip(';')
                return json.loads(data_str)
            except Exception as e:
                logger.warning(f"Data extraction failed: {e}")

    raise ValueError("No Next.js data found")


async def scrape_product(url: str) -> dict:
    """Advanced product scraping with multiple fallback strategies"""
    try:
        await human_delay()
        response = await client.get(url)
        response.raise_for_status()

        # Multiple data extraction attempts
        data = extract_next_data(response.text)

        # Deep search for product data
        products = nested_lookup("product", data)
        logger.debug(f"Found {len(products)} potential products")

        # More flexible product matching
        product = next((
            p for p in products
            if 'urlKey' in p and
            (p['urlKey'] in str(response.url) or url.split(
                '/')[-1] in p.get('urlKey', ''))
        ), None)

        if not product:
            logger.error("No matching product found")
            raise ValueError("Product data extraction failed")

        return product
    except Exception as e:
        logger.exception(f"Scraping failed: {e}")
        raise


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"message": "OK", "status": 200})


@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello World", "status": 200})


@app.route('/api/scrape-product', methods=['POST'])
def scrape_product_endpoint():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        product_data = loop.run_until_complete(scrape_product(url))
        return jsonify(product_data)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
