def parse_brolang(lines):
    ast = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        if line.startswith("wagmi wallet"):
            address = line.split('"')[1]
            ast.append(("connect_wallet", address))
        elif line.startswith("send_it"):
            parts = line.split('"')
            method = parts[1]
            args = parts[3].split(", ")
            ast.append(("call_contract", method, args))
        elif line.startswith("vibe_check"):
            msg = line.split('"')[1]
            ast.append(("print", msg))
        elif line.startswith("hodl"):
            secs = int(line.split()[1])
            ast.append(("sleep", secs))
        elif line.startswith("if fud:"):
            ast.append(("if", False))
        elif line.startswith("if moon:"):
            ast.append(("if", True))
        elif line.startswith("otherwise:"):
            ast.append(("else",))
        elif line.startswith("bail"):
            ast.append(("exit",))
    return ast
