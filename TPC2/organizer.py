import re
import json

file_path = "obras.csv"

def replace_logic(match):
    if match.group() == '\"\"':
        return '"'
    elif match.group() in ('\";', ';\"'):
        return ';'

find = r'\"\"|\";|;\"'

# estruturas para armazenar os resultados
periodos_count = {} # obras por período
periodos_titles = {} # dicionário títulos das obras por período
compositores = set()  # lista compositores (sem repetição)

# dictionário para JSON final
result_json = {
    "compositores": [],
    "periodos_count": {},
    "periodos_titles": {}
}

with open(file_path, "r", encoding="utf-8") as file:
    firstLine = file.readline()
    print(firstLine) #header debug

    formatedLines = "" #string com todo o conteúdo csv
    for line in file: 
        result = re.sub(r'\s+', " ", line).strip()
        result = re.sub(find, replace_logic, result).strip()
        
        formatedLines+=result

    # dividir pelos códigos únicos
    dividedLines = re.sub(r'O\d+', r'\g<0>\n', formatedLines)
    csv_lines = dividedLines.split("\n")
    csv_lines.pop()

    j=0 # num de linhas csv
    for csv_line in csv_lines:
        j+=1
        sections = csv_line.split(";")
        diff = len(sections) - 7 # caso de existirem ';' no meio das descrições

        compositor = sections[4 + diff]
        periodo = sections[3 + diff]
        titulo = sections[0]

        # adicionar à lista de compositores
        compositores.add(compositor)
    
        # contabilizar obras por período
        if periodo not in periodos_count:
            periodos_count[periodo] = 0
        periodos_count[periodo] += 1

        # adicionar (periodo -> título de obra) no dicionário
        if periodo not in periodos_titles:
            periodos_titles[periodo] = []
        periodos_titles[periodo].append(titulo)

    print(f"Foi extraída a informação de {j} linhas \'csv\'.")

    # json formatting
    compositores_sorted = sorted(compositores)
    result_json["compositores"] = compositores_sorted

    result_json["periodos_count"] = periodos_count

    for periodo, titulos in periodos_titles.items():
        periodos_titles[periodo] = sorted(titulos)
    result_json["periodos_titles"] = periodos_titles

    # save json
    with open("resultados.json", "w", encoding="utf-8") as json_file:
        json.dump(result_json, json_file, ensure_ascii=False, indent=4)
    
    print("\nLista de Compositores Ordenada:")
    for i, compositor in enumerate(compositores_sorted, start=1):
        print(f"{i}. {compositor}")

    print("\nDistribuição das Obras por Período:")
    for periodo, count in periodos_count.items():
        print(f"{periodo}: {count} obras")

    print("\nTítulos das Obras por Período (Ordenados):")
    for periodo, titulos in periodos_titles.items():
        titulos_sorted = sorted(titulos)
        print(f"\n{periodo}:")
        for titulo in titulos_sorted:
            print(f"- {titulo}")