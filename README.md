# StockX Scraper API

StockXScraper is an API designed for extracting product data from StockX product pages. This API uses advanced scraping techniques with fallback strategies to ensure accurate data retrieval.

Also available on RapidAPI: https://rapidapi.com/aidanmcintosh07/api/stockx-scraper-api

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
```See example response below.```
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
   git clone https://github.com/aidanmcintosh07/StockXScraper.git
   cd StockXScraper
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.7+ installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API**:
   ```bash
   python server.py
   ```

4. **Test the API**:
   Use a tool like Postman or `curl` to test the endpoints.

---

## Example Usage

### **Request**:
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"url": "https://stockx.com/air-jordan-4-retro-black-cat-2020"}' \
  http://127.0.0.1:5000/api/scrape-product
```

### **Response**:
```json
{
	"availableSizeConversions": [
		{
			"name": "US M",
			"type": "us m"
		},
		{
			"name": "US W",
			"type": "us w"
		},
		{
			"name": "UK",
			"type": "uk"
		},
		{
			"name": "CM",
			"type": "cm"
		},
		{
			"name": "KR",
			"type": "kr"
		},
		{
			"name": "EU",
			"type": "eu"
		}
	],
	"brand": "Jordan",
	"brands": {
		"default": {
			"alias": "jordan",
			"name": "Jordan"
		}
	},
	"breadcrumbs": [
		{
			"level": 1,
			"name": "Home",
			"url": "/"
		},
		{
			"level": 2,
			"name": "sneakers",
			"url": "/sneakers"
		},
		{
			"level": 3,
			"name": "Air Jordan",
			"url": "/retro-jordans"
		},
		{
			"level": 4,
			"name": "4",
			"url": "/retro-jordans/air-jordan-4"
		},
		{
			"level": 5,
			"name": "Jordan 4 Retro Black Cat (2020)",
			"url": "/air-jordan-4-retro-black-cat-2020"
		}
	],
	"browseVerticals": [
		"sneakers"
	],
	"categories": {
		"default": [
			{
				"alias": "sneakers",
				"level": 1,
				"value": "Sneakers"
			},
			{
				"alias": "lifestyle",
				"level": 2,
				"value": "Lifestyle"
			}
		]
	},
	"condition": "New",
	"contentGroup": "sneakers",
	"defaultSizeConversion": {
		"name": "US M",
		"type": "us m"
	},
	"deleted": false,
	"description": "Jordan Brand brings back a mid-2000’s classic with the Jordan 4 Black Cat (2020), now available on StockX. Originally debuting in 2006, this is the first time the Black Cat colorway has seen a retro. The fourteen year Black Cat drought has officially ended.\n<br>\n<br>\nThis Jordan 4 is composed of a black nubuck suede upper with matching detailing. Black hardware, netting, and outsoles complete the design. These sneakers released in January of 2020 and retailed for $190.",
	"editionType": null,
	"gender": "men",
	"hazardousMaterial": {
		"lithiumIonBucket": null
	},
	"id": "e158a310-414c-40fd-b267-6e45536ed9b2",
	"listingType": "STANDARD",
	"media": {
		"all360Images": [
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img01.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img02.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img03.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img04.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img05.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img06.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img07.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img08.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img09.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img10.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img11.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img12.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img13.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img14.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img15.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img16.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img17.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img18.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img19.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img20.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img21.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img22.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img23.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img24.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img25.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img26.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img27.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img28.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img29.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img30.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img31.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img32.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img33.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img34.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img35.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304",
			"https://images.stockx.com/360/Air-Jordan-4-Retro-Black-Cat-2020/Images/Air-Jordan-4-Retro-Black-Cat-2020/Lv2/img36.jpg?fm=webp&auto=compress&w=559&q=90&dpr=2&updated_at=1635341304"
		],
		"gallery": [],
		"imageUrl": "https://images.stockx.com/images/Air-Jordan-4-Retro-Black-Cat-2020-Product.jpg?fit=fill&bg=FFFFFF&w=700&h=500&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606315877",
		"smallImageUrl": "https://images.stockx.com/images/Air-Jordan-4-Retro-Black-Cat-2020-Product.jpg?fit=fill&bg=FFFFFF&w=300&h=214&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606315877",
		"thumbUrl": "https://images.stockx.com/images/Air-Jordan-4-Retro-Black-Cat-2020-Product.jpg?fit=fill&bg=FFFFFF&w=140&h=100&fm=webp&auto=compress&q=90&dpr=2&trim=color&updated_at=1606315877",
		"verticalImages": null,
		"videos": null
	},
	"merchandising": {
		"body": "",
		"image": {
			"alt": null,
			"url": "https://images-cs.stockx.com/v3/assets/blt818b0c67cf450811/blt30ea8e21c7b69d39/661980f631ff3a5b15a40d04/Surfacing_Reviews_Landing_Page_on_PDPSurfacing_Reviews_Landing_Page_on_PDP-refresh-1.jpg"
		},
		"link": {
			"title": "StockX Reviews",
			"url": "https://stockx.com/about/reviews/",
			"urlType": "EXTERNAL"
		},
		"subtitle": "See What Our Customers Have To Say",
		"title": "StockX Ratings & Reviews",
		"trackingEvent": "2024-04-12 StockX Reviews"
	},
	"model": "Jordan 4 Retro",
	"primaryCategory": "Air Jordan",
	"primaryTitle": "Jordan 4 Retro",
	"productCategory": "sneakers",
	"secondaryTitle": "Black Cat (2020)",
	"seo": {
		"meta": [
			{
				"name": "title",
				"value": "Jordan 4 Retro Black Cat (2020) Men's - CU1110-010 - US"
			},
			{
				"name": "description",
				"value": "Buy and sell StockX Verified Jordan 4 Retro Black Cat (2020) Men's shoes CU1110-010 and thousands of other Jordan sneakers with price data and release dates."
			},
			{
				"name": "keywords",
				"value": "jordan 4 retro black cat (2020) men's, style cu1110-010, colorway black/black-light graphite"
			},
			{
				"name": "twitter:description",
				"value": "Buy and sell StockX Verified Jordan shoes on StockX including the Jordan 4 Retro Black Cat (2020) Men's and thousands of other sneakers with price data and release dates."
			},
			{
				"name": "og:description",
				"value": "Buy and sell StockX Verified Jordan shoes on StockX including the Jordan 4 Retro Black Cat (2020) Men's and thousands of other sneakers with price data and release dates."
			}
		]
	},
	"sizeAllDescriptor": "All",
	"sizeDescriptor": "Size",
	"styleId": "CU1110-010",
	"tags": [],
	"title": "Jordan 4 Retro Black Cat (2020)",
	"traits": [
		{
			"format": null,
			"name": "Style",
			"value": "CU1110-010",
			"visible": true
		},
		{
			"format": null,
			"name": "Colorway",
			"value": "Black/Black-Light Graphite",
			"visible": true
		},
		{
			"format": "currency",
			"name": "Retail Price",
			"value": "190",
			"visible": true
		},
		{
			"format": "date",
			"name": "Release Date",
			"value": "2020-01-22",
			"visible": true
		},
		{
			"format": null,
			"name": "Featured",
			"value": "false",
			"visible": false
		}
	],
	"urlKey": "air-jordan-4-retro-black-cat-2020",
	"variants": [
		{
			"group": null,
			"gtins": [],
			"hidden": false,
			"id": "6ade2f5f-da1e-4ccd-aeda-57d2484e302b",
			"sizeChart": {
				"baseSize": "4",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 4",
						"type": "us m"
					},
					{
						"size": "UK 3.5",
						"type": "uk"
					},
					{
						"size": "CM 23",
						"type": "cm"
					},
					{
						"size": "KR 230",
						"type": "kr"
					},
					{
						"size": "EU 36",
						"type": "eu"
					},
					{
						"size": "US W 5.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "4"
			}
		},
		{
			"group": null,
			"gtins": [],
			"hidden": false,
			"id": "0294b9e0-e526-4c44-bf52-110a7f398bbc",
			"sizeChart": {
				"baseSize": "4.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 4.5",
						"type": "us m"
					},
					{
						"size": "UK 4",
						"type": "uk"
					},
					{
						"size": "CM 23.5 (US M 4.5)",
						"type": "cm"
					},
					{
						"size": "KR 235 (US M 4.5)",
						"type": "kr"
					},
					{
						"size": "EU 36.5",
						"type": "eu"
					},
					{
						"size": "US W 6",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "4.5"
			}
		},
		{
			"group": null,
			"gtins": [],
			"hidden": false,
			"id": "3f1bbe5c-3861-4e66-b36f-5ef3120dc303",
			"sizeChart": {
				"baseSize": "5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 5",
						"type": "us m"
					},
					{
						"size": "UK 4.5",
						"type": "uk"
					},
					{
						"size": "CM 23.5 (US M 5)",
						"type": "cm"
					},
					{
						"size": "KR 235 (US M 5)",
						"type": "kr"
					},
					{
						"size": "EU 37.5",
						"type": "eu"
					},
					{
						"size": "US W 6.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "5"
			}
		},
		{
			"group": null,
			"gtins": [],
			"hidden": false,
			"id": "36695d55-112e-4626-9f52-468b1e17ea7c",
			"sizeChart": {
				"baseSize": "5.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 5.5",
						"type": "us m"
					},
					{
						"size": "UK 5",
						"type": "uk"
					},
					{
						"size": "CM 24 (US M 5.5)",
						"type": "cm"
					},
					{
						"size": "KR 240 (US M 5.5)",
						"type": "kr"
					},
					{
						"size": "EU 38",
						"type": "eu"
					},
					{
						"size": "US W 7",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "5.5"
			}
		},
		{
			"group": null,
			"gtins": [],
			"hidden": false,
			"id": "0fddebe3-6b8f-4ce9-9ea3-11f74452e576",
			"sizeChart": {
				"baseSize": "6",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 6",
						"type": "us m"
					},
					{
						"size": "UK 5.5",
						"type": "uk"
					},
					{
						"size": "CM 24 (US M 6)",
						"type": "cm"
					},
					{
						"size": "KR 240 (US M 6)",
						"type": "kr"
					},
					{
						"size": "EU 38.5",
						"type": "eu"
					},
					{
						"size": "US W 7.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "6"
			}
		},
		{
			"group": null,
			"gtins": [],
			"hidden": false,
			"id": "c24720e6-8de3-492b-b58b-8118866cc4c3",
			"sizeChart": {
				"baseSize": "6.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 6.5",
						"type": "us m"
					},
					{
						"size": "UK 6 (EU 39)",
						"type": "uk"
					},
					{
						"size": "CM 24.5",
						"type": "cm"
					},
					{
						"size": "KR 245",
						"type": "kr"
					},
					{
						"size": "EU 39",
						"type": "eu"
					},
					{
						"size": "US W 8",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "6.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458293",
					"type": "UPC"
				}
			],
			"hidden": false,
			"id": "7e180c7c-2126-4a92-bdbc-a14394a1cfb6",
			"sizeChart": {
				"baseSize": "7",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 7",
						"type": "us m"
					},
					{
						"size": "UK 6 (EU 40)",
						"type": "uk"
					},
					{
						"size": "CM 25",
						"type": "cm"
					},
					{
						"size": "KR 250",
						"type": "kr"
					},
					{
						"size": "EU 40",
						"type": "eu"
					},
					{
						"size": "US W 8.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "7"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458309",
					"type": "UPC"
				},
				{
					"identifier": "0193655458309",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "4af927e7-020e-45fc-901a-bdd7fb3f7a2e",
			"sizeChart": {
				"baseSize": "7.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 7.5",
						"type": "us m"
					},
					{
						"size": "UK 6.5",
						"type": "uk"
					},
					{
						"size": "CM 25.5",
						"type": "cm"
					},
					{
						"size": "KR 255",
						"type": "kr"
					},
					{
						"size": "EU 40.5",
						"type": "eu"
					},
					{
						"size": "US W 9",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "7.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458316",
					"type": "UPC"
				},
				{
					"identifier": "0193655458316",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "a6226c77-afc6-4a73-988e-3b5b5eb88161",
			"sizeChart": {
				"baseSize": "8",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 8",
						"type": "us m"
					},
					{
						"size": "UK 7",
						"type": "uk"
					},
					{
						"size": "CM 26",
						"type": "cm"
					},
					{
						"size": "KR 260",
						"type": "kr"
					},
					{
						"size": "EU 41",
						"type": "eu"
					},
					{
						"size": "US W 9.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "8"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458323",
					"type": "UPC"
				},
				{
					"identifier": "0193655458323",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "a534bb99-7440-483e-8dd8-c9f2bb8feda6",
			"sizeChart": {
				"baseSize": "8.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 8.5",
						"type": "us m"
					},
					{
						"size": "UK 7.5",
						"type": "uk"
					},
					{
						"size": "CM 26.5",
						"type": "cm"
					},
					{
						"size": "KR 265",
						"type": "kr"
					},
					{
						"size": "EU 42",
						"type": "eu"
					},
					{
						"size": "US W 10",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "8.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458330",
					"type": "UPC"
				},
				{
					"identifier": "0193655458330",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "b7562099-ba61-4c06-aa76-866b04957aef",
			"sizeChart": {
				"baseSize": "9",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 9",
						"type": "us m"
					},
					{
						"size": "UK 8",
						"type": "uk"
					},
					{
						"size": "CM 27",
						"type": "cm"
					},
					{
						"size": "KR 270",
						"type": "kr"
					},
					{
						"size": "EU 42.5",
						"type": "eu"
					},
					{
						"size": "US W 10.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "9"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458347",
					"type": "UPC"
				},
				{
					"identifier": "0193655458347",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "112589ed-dd14-4bd9-b81a-71df0d3782dd",
			"sizeChart": {
				"baseSize": "9.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 9.5",
						"type": "us m"
					},
					{
						"size": "UK 8.5",
						"type": "uk"
					},
					{
						"size": "CM 27.5",
						"type": "cm"
					},
					{
						"size": "KR 275",
						"type": "kr"
					},
					{
						"size": "EU 43",
						"type": "eu"
					},
					{
						"size": "US W 11",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "9.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458354",
					"type": "UPC"
				},
				{
					"identifier": "0193655458354",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "41b120b6-bafd-49ad-8f6f-f0455729de2f",
			"sizeChart": {
				"baseSize": "10",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 10",
						"type": "us m"
					},
					{
						"size": "UK 9",
						"type": "uk"
					},
					{
						"size": "CM 28",
						"type": "cm"
					},
					{
						"size": "KR 280",
						"type": "kr"
					},
					{
						"size": "EU 44",
						"type": "eu"
					},
					{
						"size": "US W 11.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "10"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "0193655458361",
					"type": "EAN-13"
				},
				{
					"identifier": "193655458361",
					"type": "UPC"
				}
			],
			"hidden": false,
			"id": "80940bca-ba37-438b-9902-b95aa947f619",
			"sizeChart": {
				"baseSize": "10.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 10.5",
						"type": "us m"
					},
					{
						"size": "UK 9.5",
						"type": "uk"
					},
					{
						"size": "CM 28.5",
						"type": "cm"
					},
					{
						"size": "KR 285",
						"type": "kr"
					},
					{
						"size": "EU 44.5",
						"type": "eu"
					},
					{
						"size": "US W 12",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "10.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458378",
					"type": "UPC"
				},
				{
					"identifier": "0193655458378",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "05f4d17f-f578-475b-a98a-bdc37ac58745",
			"sizeChart": {
				"baseSize": "11",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 11",
						"type": "us m"
					},
					{
						"size": "UK 10",
						"type": "uk"
					},
					{
						"size": "CM 29",
						"type": "cm"
					},
					{
						"size": "KR 290",
						"type": "kr"
					},
					{
						"size": "EU 45",
						"type": "eu"
					},
					{
						"size": "US W 12.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "11"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458385",
					"type": "UPC"
				},
				{
					"identifier": "0193655458385",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "98e11ca3-a8c9-4de1-a74b-30ba1aaa19ef",
			"sizeChart": {
				"baseSize": "11.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 11.5",
						"type": "us m"
					},
					{
						"size": "UK 10.5",
						"type": "uk"
					},
					{
						"size": "CM 29.5",
						"type": "cm"
					},
					{
						"size": "KR 295",
						"type": "kr"
					},
					{
						"size": "EU 45.5",
						"type": "eu"
					},
					{
						"size": "US W 13",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "11.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458392",
					"type": "UPC"
				},
				{
					"identifier": "0193655458392",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "b7eca66b-6e42-4e39-839d-0debf3f11a5d",
			"sizeChart": {
				"baseSize": "12",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 12",
						"type": "us m"
					},
					{
						"size": "UK 11",
						"type": "uk"
					},
					{
						"size": "CM 30",
						"type": "cm"
					},
					{
						"size": "KR 300",
						"type": "kr"
					},
					{
						"size": "EU 46",
						"type": "eu"
					},
					{
						"size": "US W 13.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "12"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458408",
					"type": "UPC"
				}
			],
			"hidden": false,
			"id": "a268c7d4-dbbe-4099-bd14-0fc3e2db8677",
			"sizeChart": {
				"baseSize": "12.5",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 12.5",
						"type": "us m"
					},
					{
						"size": "UK 11.5",
						"type": "uk"
					},
					{
						"size": "CM 30.5",
						"type": "cm"
					},
					{
						"size": "KR 305",
						"type": "kr"
					},
					{
						"size": "EU 47",
						"type": "eu"
					},
					{
						"size": "US W 14",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "12.5"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458415",
					"type": "UPC"
				},
				{
					"identifier": "0193655458415",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "ed007b6c-0b44-4ad9-938a-02b2004c0323",
			"sizeChart": {
				"baseSize": "13",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 13",
						"type": "us m"
					},
					{
						"size": "UK 12",
						"type": "uk"
					},
					{
						"size": "CM 31",
						"type": "cm"
					},
					{
						"size": "KR 310",
						"type": "kr"
					},
					{
						"size": "EU 47.5",
						"type": "eu"
					},
					{
						"size": "US W 14.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "13"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458422",
					"type": "UPC"
				},
				{
					"identifier": "0193655458422",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "d1e09b8d-56c6-4405-a2f7-7e3504ef65c7",
			"sizeChart": {
				"baseSize": "14",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 14",
						"type": "us m"
					},
					{
						"size": "UK 13",
						"type": "uk"
					},
					{
						"size": "CM 32",
						"type": "cm"
					},
					{
						"size": "KR 320",
						"type": "kr"
					},
					{
						"size": "EU 48.5",
						"type": "eu"
					},
					{
						"size": "US W 15.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "14"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458439",
					"type": "UPC"
				},
				{
					"identifier": "0193655458439",
					"type": "EAN-13"
				}
			],
			"hidden": false,
			"id": "d543150c-d816-4e0e-93b5-f6cfc35774ce",
			"sizeChart": {
				"baseSize": "15",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 15",
						"type": "us m"
					},
					{
						"size": "UK 14",
						"type": "uk"
					},
					{
						"size": "CM 33",
						"type": "cm"
					},
					{
						"size": "KR 330",
						"type": "kr"
					},
					{
						"size": "EU 49.5",
						"type": "eu"
					},
					{
						"size": "US W 16.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "15"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458446",
					"type": "UPC"
				}
			],
			"hidden": false,
			"id": "7bd04b84-0234-4e17-a7dd-fd0ac763668f",
			"sizeChart": {
				"baseSize": "16",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 16",
						"type": "us m"
					},
					{
						"size": "UK 15",
						"type": "uk"
					},
					{
						"size": "CM 34",
						"type": "cm"
					},
					{
						"size": "KR 340",
						"type": "kr"
					},
					{
						"size": "EU 50.5",
						"type": "eu"
					},
					{
						"size": "US W 17.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "16"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458453",
					"type": "UPC"
				}
			],
			"hidden": false,
			"id": "2e315908-3043-4299-b055-3ae1c31fd853",
			"sizeChart": {
				"baseSize": "17",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 17",
						"type": "us m"
					},
					{
						"size": "UK 16",
						"type": "uk"
					},
					{
						"size": "CM 35",
						"type": "cm"
					},
					{
						"size": "KR 350",
						"type": "kr"
					},
					{
						"size": "EU 51.5",
						"type": "eu"
					},
					{
						"size": "US W 18.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "17"
			}
		},
		{
			"group": null,
			"gtins": [
				{
					"identifier": "193655458460",
					"type": "UPC"
				}
			],
			"hidden": false,
			"id": "f40e531c-e9d3-4375-a575-dc437a98848f",
			"sizeChart": {
				"baseSize": "18",
				"baseType": "us m",
				"displayOptions": [
					{
						"size": "US M 18",
						"type": "us m"
					},
					{
						"size": "UK 17",
						"type": "uk"
					},
					{
						"size": "CM 36",
						"type": "cm"
					},
					{
						"size": "KR 360",
						"type": "kr"
					},
					{
						"size": "EU 52.5",
						"type": "eu"
					},
					{
						"size": "US W 19.5",
						"type": "us w"
					}
				]
			},
			"traits": {
				"size": "18"
			}
		}
	]
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
- **Email**: [aidanamcintosh@gmail.com]
- **GitHub**: [https://github.com/aidanmcintosh07/StockXScraper]
