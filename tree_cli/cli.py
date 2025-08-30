import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="gtree", description="Print a project directory tree"
    )
    parser.add_argument(
        "path", nargs="?", default=".", help="Path to list (default: current directory)"
    )
    args = parser.parse_args()
    print(f"gtree OK! Path recebido: {args.path}")
