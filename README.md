# Supermarket Flyer Extractor

This repository contains a simple script to parse supermarket flyer pages
and extract basic product information such as names, prices and promotions.

## Usage

The script reads an HTML page from a URL and outputs product data in JSON format.
Parsing is done with Python's built-in `html.parser` so no extra packages are
required. Because different retailers use different page structures, you may
need to adjust the parser logic for each site.

```
python -m extractor <URL>
```

## Requirements

Install dependencies using pip (only Streamlit is required for the web interface):

```
pip install -r requirements.txt
```

The extraction utility itself uses only the Python standard library.

## Web Interface

Run the Streamlit application to try the extractor in your browser:

```
streamlit run src/app.py
```

A small Streamlit stub is included for offline testing. Use `./streamlit run src/app.py` if the real package is unavailable.

Then open the provided local address and enter a flyer URL. The extracted JSON
will be displayed on the page.