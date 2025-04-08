def crear_cliente(NIF: str, direccion: str, telefono: str, correo: str, preferente: bool):
    nuevo_cliente = {
        'NIF': NIF,
        'direccion': direccion,
        'telefono': telefono,
        'correo': correo,
        'preferente': preferente
    }

    return nuevo_cliente

def agregar_cliente(base_de_datos: dict, cliente: dict) -> dict:
    base_de_datos[cliente['NIF']] = cliente

    return base_de_datos

def eliminar_cliente(base_de_datos: dict, NIF: str) -> dict:
    pass

def mostrar_cliente(base_datos: dict, NIF: str) -> None:
    pass

def listar_clientes(base_de_datos: dict) -> None:
    pass

def listar_clientes_preferentes(base_de_datos: dict) -> None:
    pass


def main():
    clientes = {}
    
    mi_cliente1 = crear_cliente('RUBM031211B1', 'calle M 502, suzal', '615212', 'manuel@gmail.com', True)
    clientes = agregar_cliente(clientes, mi_cliente1)

    print(clientes)

if __name__ == '__main__':
    main()