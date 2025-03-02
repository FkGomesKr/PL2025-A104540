# Resolução do TPC4

### **Data:** 2 de Março de 2025  
### **Autor:**  
![Foto do Autor](https://avatars.githubusercontent.com/u/140913282?v=4)  
- **Nome:** Pedro Miguel Araújo Gomes 
- **Número de Aluno:** A104540

---

## Resumo
Este trabalho prático consiste num analisador léxico para uma liguagem de query, no caso, **SPARQL** (SPARQL Protocol and RDF Query Language). Seguindo o propósito de qualquer analisador léxico, o objetivo deste trabalho passa por reconhecer padrões e palavras-chave de forma a "partir a query" em componentes e categorizar esses mesmos componentes.

---

## Resultados
Abaixo segue o resultado da execução do nosso programa ***lexicAnalyzer.py*** aplicado a uma *query* exemplo. Todos segmentos da query filtrados foram organizados por categorias como se esperava.

**Exemplo**
``` bash
query = '''select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000'''
```

**Filtragem e Categorização**
``` bash
('SELECT', 'select')
('VARIABLE', '?nome')
('VARIABLE', '?desc')
('WHERE', 'where')
('START OF QUERY STATEMENTS', '{')
('VARIABLE', '?s')
('PROPERTY', 'a')
('NAMESPACE', 'dbo:')
('PROPERTY', 'MusicalArtist')
('END OF 1 QUERY STATEMENT', '.')
('VARIABLE', '?s')
('NAMESPACE', 'foaf:')
('PROPERTY', 'name')
('STRING', '"Chuck Berry"')
('LANG_CODE', '@en')
('END OF 1 QUERY STATEMENT', '.')
('VARIABLE', '?w')
('NAMESPACE', 'dbo:')
('PROPERTY', 'artist')
('VARIABLE', '?s')
('END OF 1 QUERY STATEMENT', '.')
('VARIABLE', '?w')
('NAMESPACE', 'foaf:')
('PROPERTY', 'name')
('VARIABLE', '?nome')
('END OF 1 QUERY STATEMENT', '.')
('VARIABLE', '?w')
('NAMESPACE', 'dbo:')
('PROPERTY', 'abstract')
('VARIABLE', '?desc')
('END OF ALL QUERY STATEMENTS', '}')
('LIMIT', 'LIMIT 1000')
```

### Como Executar o Código
1. Certifica-te de que tens Python 3.12 (ou superior) instalado.
2. Executa o programa:
``` 
python .\lexicAnalyzer.py
```
3. Visualiza os resultados no terminal.