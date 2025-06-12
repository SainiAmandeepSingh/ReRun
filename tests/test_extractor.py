from pathlib import Path
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
try:
    from extractor import parse_products
except ModuleNotFoundError:
    pytest.skip("Required dependencies not installed", allow_module_level=True)


def test_parse_sample():
    html = Path('tests/data/sample.html').read_text()
    products = parse_products(html)
    assert len(products) == 1
    p = products[0]
    assert 'Apple' in p.name
    assert p.price == '2.99'
    assert p.discounted_price == '1.99'
    assert p.promotion == '1 + 1 free'
