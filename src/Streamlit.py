"""Minimal stub of Streamlit CLI to run apps offline."""
import os
import runpy
import sys


def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1] == "run":
        path = sys.argv[2]
        if not os.path.exists(path):
            print(f"File not found: {path}")
            sys.exit(1)
        sys.path.insert(0, os.path.dirname(path) or ".")
        runpy.run_path(path, run_name="__main__")
    else:
        print("Streamlit stub - usage: streamlit run <file>")
        sys.exit(1)


if __name__ == "__main__":
    main()