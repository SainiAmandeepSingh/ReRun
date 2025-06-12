# Minimal Streamlit stub for offline use
from typing import Any
import json as _json


def title(text: str) -> None:
    print(f"# {text}")


def text_input(label: str) -> str:
    print(f"{label}:")
    return ""


def button(label: str) -> bool:
    return True  # Always return True for simplicity


def json(obj: Any) -> None:
    print(_json.dumps(obj, indent=2))


def write(msg: str) -> None:
    print(msg)


def error(msg: str) -> None:
    print(f"Error: {msg}")