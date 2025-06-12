import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

import bs4
import requests

@dataclass
class Product:
    name: str
    price: str
    discounted_price: Optional[str] = None
    discount_card_required: bool = False
    quantity: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    promotion: Optional[str] = None


def fetch_html(source: str) -> str:
    """Fetch HTML from a URL or read from a local file."""
    if source.startswith("http://") or source.startswith("https://"):
        resp = requests.get(source, timeout=10)
        resp.raise_for_status()
        return resp.text
    else:
        return Path(source).read_text(encoding="utf-8")


def parse_products(html: str) -> List[Product]:
    """Parse product information from HTML.

    This function uses generic CSS selectors and may need customization
    for each retailer's page structure.
    """
    soup = bs4.BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.select("article, .product"):
        name = item.get_text(strip=True)
        if not name:
            continue
        price_elem = item.select_one(".price, .normal-price")
        price = price_elem.get_text(strip=True) if price_elem else ""
        discounted_elem = item.select_one(".discount-price, .sale-price")
        discounted_price = discounted_elem.get_text(strip=True) if discounted_elem else None
        qty_elem = item.select_one(".quantity, .weight")
        quantity = qty_elem.get_text(strip=True) if qty_elem else None
        promo_elem = item.select_one(".promo, .promotion")
        promotion = promo_elem.get_text(strip=True) if promo_elem else None

        product = Product(
            name=name,
            price=price,
            discounted_price=discounted_price,
            quantity=quantity,
            promotion=promotion,
        )
        products.append(product)
    return products


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract product data from HTML")
    parser.add_argument("source", help="URL or path to HTML file")
    parser.add_argument("-o", "--output", help="Output JSON file")
    args = parser.parse_args()

    html = fetch_html(args.source)
    products = parse_products(html)

    data = [asdict(p) for p in products]
    if args.output:
        Path(args.output).write_text(json.dumps(data, indent=2), encoding="utf-8")
    else:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
