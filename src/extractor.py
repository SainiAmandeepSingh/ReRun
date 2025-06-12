# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 22:02:56 2025

@author: Singh
"""

from typing import List, Dict
from urllib.request import urlopen
from html.parser import HTMLParser


def fetch_html(url: str) -> str:
    """Download HTML content from a URL."""
    with urlopen(url) as resp:
        return resp.read().decode("utf-8", errors="ignore")


class ProductParser(HTMLParser):
    """Simple HTML parser for flyer product blocks."""

    def __init__(self) -> None:
        super().__init__()
        self.in_name = False
        self.in_price = False
        self.current: Dict[str, str] = {}
        self.products: List[Dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs):
        attrs = dict(attrs)
        if tag == "div" and attrs.get("class") == "product":
            self.current = {}
        elif tag == "span" and attrs.get("class") == "name":
            self.in_name = True
        elif tag == "span" and attrs.get("class") == "price":
            self.in_price = True

    def handle_endtag(self, tag: str):
        if tag == "span":
            if self.in_name:
                self.in_name = False
            if self.in_price:
                self.in_price = False
        elif tag == "div" and self.current:
            if "name" in self.current and "price" in self.current:
                self.products.append(self.current)
            self.current = {}

    def handle_data(self, data: str):
        if self.in_name:
            self.current["name"] = data.strip()
        elif self.in_price:
            self.current["price"] = data.strip()


def parse_products(html: str) -> List[Dict[str, str]]:
    """Extract product info from flyer HTML."""
    parser = ProductParser()
    parser.feed(html)
    return parser.products


def extract(url: str) -> List[Dict[str, str]]:
    html = fetch_html(url)
    return parse_products(html)


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        print("Usage: python -m extractor <URL>")
        sys.exit(1)

    url_arg = sys.argv[1]
    result = extract(url_arg)
    print(json.dumps(result, indent=2))