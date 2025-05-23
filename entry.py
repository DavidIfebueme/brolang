import sys
from parser import parse_brolang
from transpiler import transpile_ast
from runtime import run_script

def main():
    if len(sys.argv) != 2:
        print("Usage: python entry.py <script.brolang>")
        sys.exit(1)

    file_path = sys.argv[1]
    with open(file_path, "r") as f:
        lines = f.readlines()

    ast = parse_brolang(lines)
    python_code = transpile_ast(ast)
    run_script(python_code)

if __name__ == "__main__":
    main()
