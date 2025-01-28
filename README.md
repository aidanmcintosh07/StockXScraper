# StockX Scraper API

StockXScraper is an API designed for extracting product data from StockX product pages. This API uses advanced scraping techniques with fallback strategies to ensure accurate data retrieval.

---

## Features
- **Advanced Scraping Logic**: Extracts detailed product information from StockX pages.
- **Human-Like Behavior**: Introduces random delays to mimic human browsing.
- **Dynamic User-Agent**: Uses randomly generated User-Agent strings to avoid detection.
- **Robust Fallbacks**: Employs multiple strategies to parse Next.js data structures for reliability.

---

## Endpoints

### **1. Healthcheck**
- **URL**: `/healthcheck`
- **Method**: `GET`
- **Description**: Checks if the API is running.
- **Response**:
  ```json
  {
    "message": "OK",
    "status": 200
  }
  ```

### **2. Welcome Endpoint**
- **URL**: `/`
- **Method**: `GET`
- **Description**: A simple welcome endpoint.
- **Response**:
  ```json
  {
    "message": "Hello World",
    "status": 200
  }
  ```

### **3. Scrape Product**
- **URL**: `/api/scrape-product`
- **Method**: `POST`
- **Description**: Extracts detailed product data from a given StockX product page.

#### **Request Body**:
- Content-Type: `application/json`
- Required Parameter:
  ```json
  {
    "url": "<StockX Product Page URL>"
  }
  ```

#### **Response**:
- **Success** (Status Code: `200`):
  ```json
  {
    "name": "Product Name",
    "urlKey": "unique-product-identifier",
    "retailPrice": 120,
    "resaleValue": 250,
    "sizeOptions": ["7", "8", "9"]
  }
  ```
- **Error**:
  - `400 Bad Request` (Invalid Input):
    ```json
    {
      "error": "URL is required"
    }
    ```
  - `500 Internal Server Error` (Scraping Failure):
    ```json
    {
      "error": "Product data extraction failed"
    }
    ```

---

## Technologies Used
- **Flask**: Web framework for building the API.
- **httpx**: Asynchronous HTTP client for making requests.
- **fake_useragent**: Generates random User-Agent strings.
- **nested-lookup**: Searches nested dictionaries for specific keys.
- **re**: Regular expressions for parsing HTML.
- **asyncio**: Handles asynchronous operations.
- **Logging**: Provides debugging information.

---

## How It Works
1. The `/api/scrape-product` endpoint receives a StockX product page URL in the request body.
2. A random delay (`2-5 seconds`) is introduced to simulate human browsing.
3. The API fetches the page using `httpx` with a dynamic User-Agent header.
4. The product data is extracted using regular expressions and deep searches for `Next.js` data structures.
5. The parsed product information is returned in JSON format.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/StockXScraper.git
   cd StockXScraper
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7+ installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**:
   ```bash
   python app.py
   ```

4. **Test the API**:
   Use a tool like Postman or `curl` to test the endpoints.

---

## Example Usage

### **Request**:
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"url": "https://stockx.com/product-page-url"}' \
  http://127.0.0.1:5000/api/scrape-product
```

### **Response**:
```json
{
  "name": "Air Jordan 1 Retro High",
  "urlKey": "air-jordan-1-retro-high",
  "retailPrice": 170,
  "resaleValue": 300,
  "sizeOptions": ["7", "8", "9", "10"]
}
```

---

## Notes
- This project is for educational purposes only. Ensure your use complies with the terms of service of any third-party platforms you interact with.
- The API introduces delays and random User-Agent strings to reduce detection, but this does not guarantee immunity from blocking or restrictions.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
If you have any questions or need support, feel free to reach out:
- **Email**: [your-email@example.com]
- **GitHub**: [https://github.com/your-username/StockXScraper]
