# Supermarket Flyer Extractor

This repository contains a simple script to parse supermarket flyer pages
and extract basic product information such as names, prices and promotions.

## Usage

The script reads an HTML page from a URL or local file and outputs product
data in JSON format. Because different retailers use different page
structures, you may need to adjust the CSS selectors in `parse_products`
for each site.

```
python src/extractor.py <URL-or-file> -o output.json
```

This example assumes you have exported the flyer HTML locally. Many sites
do not permit automated scraping. Review each website's terms of service
before fetching pages directly.

## Requirements

Install dependencies using pip:

```
pip install -r requirements.txt
```

The project uses `requests` for downloading HTML, `beautifulsoup4` for parsing
and `Flask` for a small web interface.

## Web Interface

Run the Flask application to try the extractor in your browser:

```
python src/app.py
```

Then open `http://localhost:5000/` and either provide a flyer URL or upload an
HTML file. The extracted JSON will be displayed on the page.

The project uses `requests` for downloading HTML and `beautifulsoup4` for
parsing.