import re
import sys
import os

def markdown_to_html(markdown):
    markdown = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)

    # bold (**texto**)
    markdown = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdown)

    # itálico (*texto*)
    markdown = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown)

    # imagens ![alt](url)
    # a substituicao por imagem tem de vir antes da substituicao dos links para nao ser ignorada
    markdown = re.sub(r'!\[(.*?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', markdown)

    # links [texto](url)
    markdown = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', markdown)


    # listas numeradas
    def convert_list(match):
        items = match.group(0).split("\n")
        list_items = "".join([f"<li>{item[3:]}</li>" for item in items if item.strip()])
        return f"<ol>\n{list_items}\n</ol>"

    markdown = re.sub(r'(^\d+\..+(\n\d+\..+)*)', convert_list, markdown, flags=re.MULTILINE)

    return markdown

# input format check
if len(sys.argv) != 2:
    print("Uso: python markdown_converter.py <caminho_do_arquivo.md>")
    sys.exit(1)

#  file.md path
md_file_path = sys.argv[1]

# ler Markdown file
try:
    with open(md_file_path, "r", encoding="utf-8") as file:
        markdown_text = file.read()

    # convert to html
    html_output = markdown_to_html(markdown_text)
    print(html_output)

    # create .html file with same name
    html_file_path = os.path.splitext(md_file_path)[0] + ".html"
    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_output)

    print(f"\nArquivo HTML gerado: {html_file_path}")

except FileNotFoundError:
    print(f"Erro: Arquivo '{md_file_path}' não encontrado.")
    sys.exit(1)
