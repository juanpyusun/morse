
from itertools import combinations

morse_code_dict= {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----"
}  

reverse_morse_dict= {value: key for key, value in morse_code_dict.items()}

#Metodo para encriptar de texto a morse
def encrypt(mensaje: str) -> str:
    mensaje=mensaje.replace(" ","")
    mensaje=mensaje.upper()
    lista=[morse_code_dict[letra] for letra in mensaje]
    return " / ".join(lista)

#Metodo para desencriptar de morse a texto, si no encuentra la combinacion de raya/punto entonces 
def decrypt(mensaje: str) -> str:
    lista=[reverse_morse_dict.get(letra,"*") for letra in mensaje.split()]
    return "".join(lista)

#Metodo para desencriptar de morse a texto, brindando todas las opciones posibles
def subconjuntos(mensaje_encriptado:str)->None:
    f=open("morse.txt","w")
    
#aqui va el codigo morse mal escrito para probar todas las posibles traducciones
    cantidad_elementos=len(mensaje_encriptado)
    
    if cantidad_elementos<=5 :
        f.write(mensaje_encriptado+" "+decrypt(mensaje_encriptado))
        f.write("\n")
    
    for n in range(1,cantidad_elementos):
        posicion_coma_grupo=list(combinations(range(1,cantidad_elementos),n))
        for posicion_coma in posicion_coma_grupo:
            subconjunto=[]
            mensaje_salida=""
            inicio=0

            for single_coma_position in posicion_coma:
                mensaje_salida+=decrypt(mensaje_encriptado[inicio:single_coma_position])
                subconjunto.append(mensaje_encriptado[inicio:single_coma_position])
                inicio=single_coma_position

            subconjunto.append(mensaje_encriptado[inicio:])
            mensaje_salida+=decrypt(mensaje_encriptado[inicio:])

            #filtrando sin los *
            if "*" in mensaje_salida:
                continue

            f.write(str(subconjunto)+" "+mensaje_salida)
            f.write("\n")
    f.close()

#Menu principal
def main() -> None:
    menu = input("*****************\n1.De texto a morse\n2.De morse a texto\n3.Morse sin espacios\nque desea hacer?: ")
    if menu=='1':
        mensaje=input("ingrese su texto: ")
        print("Su mensaje encriptado queda:\n",encrypt(mensaje))
    elif menu=='2':
        mensaje=input("ingrese su codigo morse bien escrito: ")
        print("Su mensaje desencriptado queda:\n",decrypt(mensaje))
    elif menu=='3':
        mensaje=input("ingrese su codigo morse mal escrito sin espacios entre los simbolos: ")
        subconjuntos(mensaje)
        print("se ha creado el archivo morse.txt entre sus archivos con todas las combinaciones posibles")


if __name__ == "__main__":
    main()
