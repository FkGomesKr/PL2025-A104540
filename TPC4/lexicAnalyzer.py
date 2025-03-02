import re

# padroes possiveis
Patterns_types = [
    (r"select", "SELECT"),
    (r"where", "WHERE"),
    (r"LIMIT \d+", "LIMIT"),
    (r"\?[\w]+", "VARIABLE"),
    (r"[a-zA-Z_]\w*:", "NAMESPACE"),
    (r"[a-zA-Z_]\w*", "PROPERTY"),
    (r"[{]", "START OF QUERY STATEMENTS"),
    (r"[}]", "END OF ALL QUERY STATEMENTS"),
    (r"[.]", "END OF 1 QUERY STATEMENT"),
    (r"@([a-zA-Z\-]+)", "LANG_CODE"),
    (r"\"[^\"]*\"", "STRING"),
    (r"\d+", "NUMBER"),
    (r"\s+", None),  # ignorar espaços em branco/tabs/\n
]

TOKEN_REGEX = [(re.compile(pattern), type) for pattern, type in Patterns_types]

def lexer(query):
    tokens = []
    index = 0
    while index < len(query):
        match = None
        for anyPattern, type in TOKEN_REGEX:
            match = anyPattern.match(query, index)
            if match:
                if type:  # ignorar None matches
                    tokens.append((type, match.group())) # dicionario com tipo e padrao associado
                index = match.end()
                break
        if not match:
            raise SyntaxError(f"Padrão inesperado: {query[index]}")
    return tokens

# exemplo
query = '''select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000'''

tokens = lexer(query)

for token in tokens:
    print(token)
