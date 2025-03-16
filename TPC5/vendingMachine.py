import json
from datetime import datetime

STOCK_FILE = "stock.json"

def carregar_stock():
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

def listar_produtos(stock):
    print("cod    | nome             | quantidade | preço")
    print("-----------------------------------------")
    for produto in stock:
        print(f"{produto['cod']:6} | {produto['nome']:16} | {produto['quant']:10} | {produto['preco']}€")

def inserir_moeda(saldo):
    moedas = {
        "1e": 1.0, "50c": 0.50, "20c": 0.20, "10c": 0.10, "5c": 0.05
        }
    valores = input(">> MOEDA ").split(", ")
    for moeda in valores:
        if moeda in moedas:
            saldo += moedas[moeda]
        else:
            print(f"Moeda inválida: {moeda}")
    print(f"maq: Saldo = {saldo:.2f}€")
    return saldo

def selecionar_produto(stock, saldo):
    cod = input(">> SELECIONAR ").strip()
    produto = next((p for p in stock if p["cod"] == cod), None)
    
    if not produto:
        print("maq: Produto inexistente.")
        return saldo

    if produto["quant"] == 0:
        print("maq: Produto esgotado.")
        return saldo

    if saldo < produto["preco"]:
        print(f"maq: Saldo insuficiente. Saldo = {saldo:.2f}€; Pedido = {produto['preco']}€")
        return saldo

    produto["quant"] -= 1
    saldo -= produto["preco"]
    print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
    print(f"maq: Saldo = {saldo:.2f}€")
    return saldo

def calcular_troco(saldo):
    moedas = [1.0, 0.50, 0.20, 0.10, 0.05]
    troco = {}
    
    for moeda in moedas:
        while saldo >= moeda:
            saldo = round(saldo - moeda, 2)
            troco[moeda] = troco.get(moeda, 0) + 1

    if troco:
        troco_formatado = []
        for m, v in troco.items():
            if m == 1.0:
                troco_formatado.append(f"{v}x 1e")
            else:
                troco_formatado.append(f"{v}x {int(m * 100)}c")

        print("maq: Pode retirar o troco: " + ", ".join(troco_formatado))

    print("maq: Até à próxima")

def main():
    stock = carregar_stock()
    saldo = 0.0
    # YYYY-MM-DD
    data_atual = datetime.today().strftime("%Y-%m-%d")

    print(f"maq: {data_atual}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip().upper()

        if comando == "LISTAR":
            listar_produtos(stock)
        elif comando.startswith("MOEDA"):
            saldo = inserir_moeda(saldo)
        elif comando.startswith("SELECIONAR"):
            saldo = selecionar_produto(stock, saldo)
        elif comando == "SAIR":
            calcular_troco(saldo)
            guardar_stock(stock)
            break
        else:
            print("maq: Comando inválido.")

if __name__ == "__main__":
    main()
