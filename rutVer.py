def calcular_digito_verificador(rut):
    rut = rut.replace('.', '').replace('-', '')  

    rut_lista = [int(digito) for digito in rut[::-1]]

    factores = [2, 3, 4, 5, 6, 7]

    suma = 0
    factor_index = 0

    for digito in rut_lista:
        suma += digito * factores[factor_index]
        factor_index = (factor_index + 1) % len(factores)

    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        return 'K'
    elif digito_verificador == 11:
        return '0'
    else:
        return str(digito_verificador)

rut = "15432920-"
digito_verificador = calcular_digito_verificador(rut)
rut_completo = rut + digito_verificador
print("El RUT completo con dígito verificador es:", rut_completo)