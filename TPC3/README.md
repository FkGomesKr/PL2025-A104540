# Resolução do TPC3

### **Data:** 24 de Fevereiro de 2025  
###  **Autor:**  
![Foto do Autor](https://avatars.githubusercontent.com/u/140913282?v=4)  
- **Nome:** Pedro Miguel Araújo Gomes 
- **Número de Aluno:** A104540

---

## Resumo
Este trabalho prático é um pequeno conversor de **MarkDown** para **HTML** feito em **Python**. Este conversor está aplicado a alguns elementos básicos:
- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto";
- Bold: pedaços de texto entre "**";
- Itálico: pedaços de texto entre "*";
- Lista numerada;
- Link: [texto](endereço URL);
- Imagem: ![texto alternativo](path para a imagem).

---

## Resultados
Abaixo seguem os ficheiros resultantes deste TPC, foram gerados tanto em ficheiro **HTML** como em **"raw code"** *printed* no terminal. Para reproduzir estes resultados foram criados, necessariamente, 2 ficheiros **MarkDown** a ser convertidos:

1. **`example1.html`**
```
<h1>Exemplo 1</h1>
<h2>Subtítulo 1</h2>
<h3>Este é um <b>exemplo</b> de <i>Markdown</i>.</h3>

<ol>
<li>Item 1</li><li>Item 2</li><li>Item 3</li>
</ol>

Veja mais em <a href="https://www.google.com">Google</a>.


Arquivo HTML gerado: .\example1.html
```

3. **`example2.html`**  
```
<h1>Exemplo 2</h1>
<h3>Subtítulo 2</h3>
Aqui está uma imagem:

<img src="cat.jpg" alt="Um gato"/>

Texto <b>negrito</b> e <i>itálico</i> misturados.


Arquivo HTML gerado: .\example2.html
```

---

### Como Executar o Código
1. Certifica-te de que tens Python 3.12 (ou superior) instalado.
2. Executa o programa e dá algum ficheiro **MarkDown** como argumento, por exemplo:
```
python mdHtmlConverter.py example1.md
```
