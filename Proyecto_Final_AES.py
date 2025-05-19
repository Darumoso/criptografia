"""
Héctor Yoram Quiroz Flores
"""

s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

r_con = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

def sustituir_bytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = s_box[s[i][j]]

def mover_filas(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

def agregar_llave_ronda(s, k):
    for i in range(4):
        for j in range(4):
            s[i][j] ^= k[i][j]

xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

def mezclar_columna(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)

def mezclar_columnas(s):
    for i in range(4):
        mezclar_columna(s[i])

def bytesAmatriz(texto):
    return [list(texto[i:i+4]) for i in range(0, len(texto), 4)]

def matrizAbytes(matriz):
    return bytes(sum(matriz, []))

def pad(texto_plano):
    padding_len = 16 - (len(texto_plano) % 16)
    padding = bytes([padding_len] * padding_len)
    return texto_plano + padding

def separar_bloques(mensaje, tamanio_bloque=16):
    return [mensaje[i:i+tamanio_bloque] for i in range(0, len(mensaje), tamanio_bloque)]

class AES:
    rondas_por_tamanio_llave = {16: 10, 24: 12, 32: 14}
    
    def __init__(self, llave_principal):
        assert len(llave_principal) in AES.rondas_por_tamanio_llave
        self.n_rounds = AES.rondas_por_tamanio_llave[len(llave_principal)]
        self._llave_matriz = self._expand_key(llave_principal)

    def _expand_key(self, llave_principal):
        llave_columnas = bytesAmatriz(llave_principal)
        tamanio_interacion = len(llave_principal) // 4

        i = 1
        while len(llave_columnas) < (self.n_rounds + 1) * 4:
            palabra = list(llave_columnas[-1])

            if len(llave_columnas) % tamanio_interacion == 0:
                palabra.append(palabra.pop(0))
                palabra = [s_box[b] for b in palabra]
                palabra[0] ^= r_con[i]
                i += 1
            elif len(llave_principal) == 32 and len(llave_columnas) % tamanio_interacion == 4:
                palabra = [s_box[b] for b in palabra]

            palabra = bytes(x ^ y for x, y in zip(palabra, llave_columnas[-tamanio_interacion]))
            llave_columnas.append(palabra)

        return [llave_columnas[4*i : 4*(i+1)] for i in range(len(llave_columnas) // 4)]

    def cifrar_bloque(self, texto_plano):
        assert len(texto_plano) == 16

        plain_state = bytesAmatriz(texto_plano)

        agregar_llave_ronda(plain_state, self._llave_matriz[0])

        for i in range(1, self.n_rounds):
            sustituir_bytes(plain_state)
            mover_filas(plain_state)
            mezclar_columnas(plain_state)
            agregar_llave_ronda(plain_state, self._llave_matriz[i])

        sustituir_bytes(plain_state)
        mover_filas(plain_state)
        agregar_llave_ronda(plain_state, self._llave_matriz[-1])

        return matrizAbytes(plain_state)

    def encrypt(self, texto_plano):
        texto_plano = pad(texto_plano)
        
        bloques = []
        for texto_plano_bloque in separar_bloques(texto_plano):
            bloque = self.cifrar_bloque(texto_plano_bloque)
            bloques.append(bloque)

        return b''.join(bloques)

def obtener_entrada_usuario():
    print("\n===== Cifrado AES =====")
    
    texto_plano_entrada = input("\nIngrese el texto a cifrar: ")
    texto_plano = texto_plano_entrada.encode('utf-8')
    
    usar_llave_defecto = input("\nUsar la llave por defecto? (Y/n): ").lower()
    
    if usar_llave_defecto == 'n':
        while True:
            key_input = input("\nIngrese una llave de 16, 24, o 32 caracteres: ")
            key = key_input.encode('utf-8')
            
            if len(key) in [16, 24, 32]:
                break
            else:
                print("Error: La llave debe ser de 16, 24, or 32 caracteres")
    else:
        key = b"ProfePongameDiez"
        print(f"\nUsando llave por defecto: '{key.decode('utf-8')}'")
    
    return texto_plano, key

def main():
    texto_plano, key = obtener_entrada_usuario()
    
    aes = AES(key)
    
    texto_cifrado = aes.encrypt(texto_plano)
    
    print("\n===== Resumen del cifrado =====")
    print(f"\nTexto original: '{texto_plano.decode('utf-8')}'")
    print(f"Llave: '{key.decode('utf-8')}'")
    print("\nTexto cifrado (hex):", texto_cifrado.hex().upper())
    print("\nLongitud del texto cifrado:", len(texto_cifrado), "bytes")
        

if __name__ == "__main__":
    main()
