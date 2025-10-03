def dec_to_bin(decimal):
    decimal = int(decimal)  
    if decimal == 0:
        return "0"
    
    resultado = ""
    while decimal > 0:
        residuo = decimal % 2
        resultado = str(residuo) + resultado
        decimal = decimal // 2
    return resultado

def dec_to_oct(decimal):
    decimal = int(decimal)
    if decimal == 0:
        return "0"
    
    resultado = ""
    while decimal > 0:
        residuo = decimal % 8
        resultado = str(residuo) + resultado
        decimal = decimal // 8
    return resultado

def dec_to_hex(decimal):
    decimal = int(decimal)
    if decimal == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    resultado = ""
    while decimal > 0:
        residuo = decimal % 16
        resultado = hex_chars[residuo] + resultado
        decimal = decimal // 16
    return resultado