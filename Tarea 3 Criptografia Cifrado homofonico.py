"""
Castrillo Ramirez Luis Enrique
Ramirez Martinez Luis Angel
Hector Yoram Quiroz Flores

Criptografia Grupo 2
Tarea 3: Cifrado homofónico
"""
import random

class HomophonicCipher:
    def __init__(self, keys):
        self.keys = [k.upper() for k in keys]
        self.homophonic_map = {}
        self.reverse_map = {}
        self._generate_mappings()
        
    def _generate_mappings(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            idx = ord(char) - ord('A')
            symbols = [key[idx] for key in self.keys]
            self.homophonic_map[char] = symbols
            
            for symbol in symbols:
                self.reverse_map[symbol] = char
    
    def encrypt(self, plaintext):
        encrypted = []
        for char in plaintext.upper():
            if char in self.homophonic_map:
                encrypted.append(random.choice(self.homophonic_map[char]))
            else:
                encrypted.append(char)
        return ''.join(encrypted)
    
def main():
    keys = [
        "lucysotnpavxqjbzmwkrdfehgi",
        "syepmfkdcbxvlqgnjrzwaiohut",
        "nvcumobifyhwzdlxergkaspqjt",
        "dltvczhspuormwxkjbafgnyeqi"
    ]
    
    cipher = HomophonicCipher(keys)
    
    text = input("\nIngresa el texto a cifrar: ")
    encrypted = cipher.encrypt(text)
    print(f"\nTexto cifrado:\n{encrypted}")

main()