def somador_on_off(texto):
    soma = 0
    somar = True
    i = 0
    n = len(texto)

    while i < n:
        if texto[i:i+3].lower() == 'off':
            somar = False
            i += 3
        elif texto[i:i+2].lower() == 'on':
            somar = True
            i += 2
        elif texto[i] == '=':
            print(soma)
            i += 1
        elif somar and texto[i].isdigit():
            num_str = ''
            while i < n and texto[i].isdigit():
                num_str += texto[i]
                i += 1
            soma += int(num_str)
        else:
            i += 1


texto = input("Digite o texto no qual vamos aplicar o Somador On-Off: \n")
#texto = "On123;Off456On789= rosca20= 1d1 10=off50ds0="
somador_on_off(texto)