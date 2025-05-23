def transpile_ast(ast):
    lines = ["from runtime import *"]
    indent = ""
    for node in ast:
        if node[0] == "connect_wallet":
            lines.append(f'{indent}connect_wallet("{node[1]}")')
        elif node[0] == "call_contract":
            args = ", ".join(f'"{arg}"' if not arg.isdigit() else arg for arg in node[2])
            lines.append(f'{indent}call_contract("{node[1]}", [{args}])')
        elif node[0] == "print":
            lines.append(f'{indent}vibe_check("{node[1]}")')
        elif node[0] == "sleep":
            lines.append(f"{indent}hodl({node[1]})")
        elif node[0] == "if":
            lines.append(f"{indent}if {node[1]}:")
            indent = "    "
        elif node[0] == "else":
            indent = ""
            lines.append("else:")
            indent = "    "
        elif node[0] == "exit":
            lines.append(f"{indent}bail()")
    return "\n".join(lines)
