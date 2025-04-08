def contar_frecuencia(cadena):
    cont_freq = {}
    for palabra in cadena.split(' '):
        if cont_freq.get(palabra):
            cont_freq[palabra] += 1
        else:
            cont_freq[palabra] = 1
    return cont_freq

def mayor_frecuencia(frecuencias: dict):
    llave_max = None
    valor_max = 0
    for key, value in frecuencias.items():
        if value > valor_max:
            valor_max = value
            llave_max = key
    return (llave_max, valor_max)

def main():
    cadena = input('Escriba una cadena: ').strip()
    resultado = contar_frecuencia(cadena)
    print(resultado)
    print(mayor_frecuencia(resultado))


if __name__ == '__main__':
    main()