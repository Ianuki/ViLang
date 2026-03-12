Enum = """
    TOKEN_EOF,
    TOKEN_EOL,

    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,

    TOKEN_PUSH,
    TOKEN_SET,
    TOKEN_REPEAT,
    TOKEN_JUMP,
    TOKEN_BREAK,
    TOKEN_FUNCTION,
    TOKEN_END,
    TOKEN_IF,
    TOKEN_ASM,
    TOKEN_MACRO,
    TOKEN_LABEL,
    TOKEN_IMPORT,

    TOKEN_PLUS,
    TOKEN_MINUS,
    TOKEN_STAR,
    TOKEN_SLASH,
    TOKEN_EQ,
    TOKEN_EQEQ,
    TOKEN_NEQ,
    TOKEN_COMMA,
    TOKEN_COLON,
    TOKEN_LPAREN,
    TOKEN_RPAREN,
    TOKEN_LBRACKET,
    TOKEN_RBRACKET,
    TOKEN_EXCL
"""
enumerators = Enum.replace(",", "").split()

a = ""

for enumerator in enumerators:
    print(f"case {enumerator}: return \"{enumerator}\";")

