from lex import *

def main():
    input = "LET foobar = 123"
    operators = "+- */ >>= = !="
    comment = "+- # This is a comment!\n */"
    string = "+- \"This is a % string\" # This is a comment!\n */"
    number = "+-123 9.8654*/"
    identAndKeyword = "IF+-123 foo*THEN/"
    lexer = Lexer(identAndKeyword)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()
