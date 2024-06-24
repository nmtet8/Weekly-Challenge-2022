def segundo_mas_grande(numeros):
    """
    input - numeros(int): lista de elementos numericos
    output - int: el segundo elemento de mayor valor numérico de la lista
    """
    primero = max(numeros)
    numeros.remove(primero)
    segundo = max(numeros)
    return segundo
