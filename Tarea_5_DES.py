"""Integrantes
Castrillo Ramirez Luis Enrique
Ramirez Martinez Luis Angel
Quiroz Flores Héctor Yoram
"""


import os
import sys
import time

# ---------------------------
# DES
# ---------------------------

# Tablas
IP = [
    57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7,
    56,48,40,32,24,16,8,0,58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6
]

IP_INV = [
    39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,
    37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,
    35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,
    33,1,41,9,49,17,57,25,32,0,40,8,48,16,56,24
]

E = [
    31,0,1,2,3,4,3,4,5,6,7,8,7,8,9,10,
    11,12,11,12,13,14,15,16,15,16,17,18,
    19,20,19,20,21,22,23,24,23,24,25,26,
    27,28,27,28,29,30,31,0
]

P = [
    15,6,19,20,28,11,27,16,0,14,22,25,
    4,17,30,9,1,7,23,13,31,26,2,8,18,
    12,29,5,21,10,3,24
]

PC1 = [
    56,48,40,32,24,16,8,0,57,49,41,33,
    25,17,9,1,58,50,42,34,26,18,10,2,
    59,51,43,35,62,54,46,38,30,22,14,6,
    61,53,45,37,29,21,13,5,60,52,44,36,
    28,20,12,4,27,19,11,3
]

PC2 = [
    13,16,10,23,0,4,2,27,14,5,20,9,
    22,18,11,3,25,7,15,6,26,19,12,1,
    40,51,30,36,46,54,29,39,50,44,32,
    47,43,48,38,55,33,52,45,41,49,35,
    28,31
]

S_BOXES = [
    [
        [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
    ],
    [
        [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
        [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
        [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
        [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
    ],
    [
        [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
        [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
        [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
        [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
    ],
    [
        [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
        [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
        [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
        [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
    ],
    [
        [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
    ],
    [
        [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
        [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
        [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
        [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
    ],
    [
        [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
        [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
        [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
        [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
    ],
    [
        [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
        [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
        [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
        [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
    ]
]

def adjust_parity(key_bits):
    adjusted = []
    for i in range(0, 64, 8):
        byte = key_bits[i:i+8]
        parity = 1 - (sum(byte[:7]) % 2)
        adjusted += byte[:7] + [parity]
    return adjusted

def permute(bits, table):
    return [bits[i] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def generate_subkeys(key_bits):
    key_bits = adjust_parity(key_bits)
    key = permute(key_bits, PC1)
    C, D = key[:28], key[28:]
    subkeys = []
    shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for shift in shifts:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkeys.append(permute(C + D, PC2))
    return subkeys

def f_function(R, subkey):
    expanded = permute(R, E)
    xor = [e ^ k for e, k in zip(expanded, subkey)]
    s_out = []
    for i in range(8):
        chunk = xor[i*6:(i+1)*6]
        row = (chunk[0] << 1) + chunk[5]
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
        s_val = S_BOXES[i][row][col]
        s_out += [s_val >> 3 & 1, s_val >> 2 & 1, s_val >> 1 & 1, s_val & 1]
    return permute(s_out, P)

def des_process(block_bits, subkeys, encrypt=True):
    block = permute(block_bits, IP)
    L, R = block[:32], block[32:]
    rounds = range(16) if encrypt else reversed(range(16))
    for i in rounds:
        new_R = [l ^ f for l, f in zip(L, f_function(R, subkeys[i]))]
        L, R = R, new_R
    return permute(R + L, IP_INV)

def bytes_to_bits(data):
    return [int(bit) for byte in data for bit in f"{byte:08b}"]

def bits_to_bytes(bits):
    byte_array = bytearray()
    for i in range(0, len(bits), 8):
        byte = sum(bit << (7-j) for j, bit in enumerate(bits[i:i+8]))
        byte_array.append(byte)
    return bytes(byte_array)

def pad(data):
    padding = 8 - (len(data) % 8)
    return data + bytes([padding]*padding)

def unpad(data):
    padding = data[-1]
    return data[:-padding]

# ---------------------------
# Interfaz
# ---------------------------

COLORS = {
    'HEADER': '\033[95m',
    'BLUE': '\033[94m',
    'CYAN': '\033[96m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'ENDC': '\033[0m',
    'BOLD': '\033[1m'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_step(message, color='CYAN'):
    print(f"{COLORS[color]}[*] {message}{COLORS['ENDC']}")

def show_progress(current, total):
    bar = '[' + '■' * current + '□' * (total - current) + ']'
    print(f"{COLORS['GREEN']}Progreso: {bar} {current}/{total}{COLORS['ENDC']}")

def des_encrypt_cli(plaintext, key):
    try:
        key_bits = bytes_to_bits(key.encode())
        subkeys = generate_subkeys(key_bits)

        print_step("Generando las subllaves")
        for i, sk in enumerate(subkeys, 1):
            print(f"Round {i:2}: {bits_to_bytes(sk).hex()[:12]}...")

        print_step("\nProcesando bloques")
        padded = pad(plaintext.encode())
        ciphertext = bytearray()
        total_blocks = len(padded) // 8

        for i in range(total_blocks):
            show_progress(i+1, total_blocks)
            block = padded[i*8:(i+1)*8]
            encrypted = des_process(bytes_to_bits(block), subkeys)
            ciphertext += bits_to_bytes(encrypted)
            time.sleep(0.1)

        print(f"\n{COLORS['GREEN']}Cifrado completado!{COLORS['ENDC']}")
        return ciphertext.hex()

    except Exception as e:
        raise ValueError(f"No se pudo cifrar el mensaje: {str(e)}")

def des_decrypt_cli(ciphertext, key):
    try:
        key_bits = bytes_to_bits(key.encode())
        subkeys = generate_subkeys(key_bits)

        print_step("Procesando bloques")
        data = bytes.fromhex(ciphertext)
        total_blocks = len(data) // 8
        plaintext = bytearray()

        for i in range(total_blocks):
            show_progress(i+1, total_blocks)
            block = data[i*8:(i+1)*8]
            decrypted = des_process(bytes_to_bits(block), subkeys, False)
            plaintext += bits_to_bytes(decrypted)
            time.sleep(0.1)

        print(f"\n{COLORS['GREEN']}Mensaje descifrado!{COLORS['ENDC']}")
        return unpad(plaintext).decode()

    except Exception as e:
        raise ValueError(f"No se pudo descifrar el mensaje: {str(e)}")

def main_menu():
    clear_screen()
    print(f"{COLORS['HEADER']}Implementacion de DES{COLORS['ENDC']}\n")

    while True:
        print(f"{COLORS['BOLD']}Menu principal:")
        print(f"1. Cifrar mensaje")
        print(f"2. Descifrar mensaje")
        print(f"3. Salir{COLORS['ENDC']}")

        choice = input("\nSeleccione una opcion (1-3): ")

        if choice == '3':
            print(f"\n{COLORS['BLUE']}Adios!{COLORS['ENDC']}")
            break
        try:
            if choice == '1':
                message = input("\nIngrese el mensaje: ")
                key = input("Ingrese la llave de 8 caracteres: ")
                if len(key) != 8:
                    raise ValueError("La llave debe ser de 8 caracteres")
                result = des_encrypt_cli(message, key)
                print(f"\n{COLORS['CYAN']}Texto cifrado: {result}{COLORS['ENDC']}")

            elif choice == '2':
                ciphertext = input("\nIngrese el texto cifrado(hex): ")
                key = input("Ingrese la llave de 8 caracteres: ")
                if len(key) != 8:
                    raise ValueError("La llave debe ser de 8 caracteres")
                result = des_decrypt_cli(ciphertext, key)
                print(f"\n{COLORS['CYAN']}Texto plano: {result}{COLORS['ENDC']}")

            input("\nPresione enter para continuar...")
            clear_screen()

        except Exception as e:
            print(f"\n{COLORS['RED']}Error: {str(e)}{COLORS['ENDC']}")
            input("Presione enter para continuar...")
            clear_screen()

if __name__ == "__main__":
    main_menu()
