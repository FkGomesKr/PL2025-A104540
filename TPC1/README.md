# Resolução do TPC1

### **Data:** 8 de Fevereiro de 2025  
### **Autor:**  
![Foto do Autor](https://avatars.githubusercontent.com/u/140913282?v=4)  
- **Nome:** Pedro Miguel Araújo Gomes 
- **Número de Aluno:** A104540

---

## Resumo
Este trabalho consistiu em criar um programa em Python capaz de processear um input textual e de realizar a soma de todos os números encontrados nesse mesmo input, tendo em conta segmentos textuais específicios que funcionam como regras para o comportamento deste leitor de input:

- *On* : Sinaliza a obrigação de somar (lido com qualquer combinação de maiúsculas ou minúsculas).
- *Off* : Sinaliza fim da obrigação de somar (lido com qualquer combinação de maiúsculas ou minúsculas).
- *=* : Sinaliza a exibição do resultado atual da soma (print).

---

## Resultados
Como resultado do programa **`somadorOnOff.py`**, como expectável, obtivemos este resultado para um dado input: 

- Input:
```
Digite o texto no qual vamos aplicar o Somador On-Off:
On123;Off456On789= rosca20= 1d1 10=off50ds0=
```
- Resultado:
```bash
912
932
944
944
```

### Como Executar o Código
1. Certifica-te de que tens Python 3.12 (ou superior) instalado.
2. Executa o programa
```bash
python somadorOnOff.py
```
3. Insere um input textual, por exemplo, "On123;Off456On789= rosca20= 1d1 10=off50ds0="
