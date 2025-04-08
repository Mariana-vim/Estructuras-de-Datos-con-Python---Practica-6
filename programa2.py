def decimal_a_binario(numero):
    s = ""
    while (numero > 0):
        r = numero % 2
        s += str(r)
        numero = numero // 2
    return s[::-1]

def binario_a_decimal(numero: str):
    res = 0
    power = 0
    for digit in reversed(numero):
        if digit == '1':
            res += 2**power
        power += 1
    return res

def main():
    numero = int(input("Teclea un numero en decimal: "))
    resultado = decimal_a_binario(numero)
    print(resultado)
    print(binario_a_decimal(resultado))


if __name__ == '__main__':
    main()