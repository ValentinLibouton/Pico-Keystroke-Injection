def bitwise_or_hex(hex1, hex2):
    # Convertir les entrées hexadécimales en entiers
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    # Effectuer l'opération bitwise OR
    result = num1 | num2

    # Convertir le résultat en hexadécimal
    hex_result = hex(result)

    return hex_result




def bitwise_and_hex(hex1, hex2):
    # Convertir les entrées hexadécimales en entiers
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    # Effectuer l'opération bitwise AND
    result = num1 & num2

    # Convertir le résultat en hexadécimal
    hex_result = hex(result)

    return hex_result


def bitwise_xor_hex(hex1, hex2):
    # Convertir les entrées hexadécimales en entiers
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    # Effectuer l'opération bitwise XOR
    result = num1 ^ num2

    # Convertir le résultat en hexadécimal
    hex_result = hex(result)

    return hex_result

hex1="0x80"
hex2="0x1f"
bitwise_or_result = bitwise_or_hex(hex1=hex1, hex2=hex2)
print(f"Bitwise OR: {hex1}|{hex2} = {bitwise_or_result}")
print(f"Bitwise XOR: {bitwise_or_result}^{hex1} = {bitwise_xor_hex(hex1=bitwise_or_result, hex2=hex1)}")


