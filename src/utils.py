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

def generate_hid_code(modifier, key):
    return (modifier, 0, key, 0, 0, 0, 0, 0)

def tuple_to_hex(tup):
    return ''.join(f'0x{byte:02x} ' for byte in tup)

def combine_keys(modifier_prefix, modifier_key, key):
    combined_modifier = modifier_prefix | modifier_key
    combined_key = modifier_prefix | key
    return hex(combined_modifier), hex(combined_key)



hex1="0x80"
hex2="0x1f"
bitwise_or_result = bitwise_or_hex(hex1=hex1, hex2=hex2)
print(f"Bitwise OR: {hex1}|{hex2} = {bitwise_or_result}")
print(f"Bitwise XOR: {bitwise_or_result}^{hex1} = {bitwise_xor_hex(hex1=bitwise_or_result, hex2=hex1)}")


# Codes pour AltGr et 2
altgr_prefix = 0xe0
altgr_key = 0x38
key_2 = 0x03

# Combiner les touches
combined_modifier, combined_key = combine_keys(altgr_prefix, altgr_key, key_2)

print("Combined Modifier:", combined_modifier)  # AltGr (Right Alt)
print("Combined Key:", combined_key)            # Key 2