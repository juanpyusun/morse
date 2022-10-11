import itertools

morse_code_dict= {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----"
}  

reverse_morse_dict= {value: key for key, value in morse_code_dict.items()}


def encrypt(mensaje: str) -> str:
    mensaje=mensaje.replace(" ","")
    mensaje=mensaje.upper()
    lista=[morse_code_dict[letra] for letra in mensaje]
    return " / ".join(lista)


def decrypt(mensaje: str) -> str:
    lista=[reverse_morse_dict.get(letra,"*") for letra in mensaje.split()]
    return "".join(lista)


def main() -> None:
    menu = input("*****************\n1.De texto a morse\n2.De morse a texto\n3.Morse sin espacios\nque desea hacer?: ")
    if menu=='1':
        mensaje=input("ingrese su texto: ")
        print("Su mensaje encriptado queda:\n",encrypt(mensaje))
    elif menu=='2':
        mensaje=input("ingrese su codigo: ")
        print("Su mensaje encriptado queda:\n",decrypt(mensaje))
    elif menu=='3':
        mensaje=input("ingrese su codigo: ")

def subconjuntos(mensaje:str)->list:
    pass

if __name__ == "__main__":
    main()
