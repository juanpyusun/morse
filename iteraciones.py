from itertools import combinations

morse_code_dict= {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."
}  

reverse_morse_dict= {value: key for key, value in morse_code_dict.items()}

def decrypt(mensaje: str) -> str:
    lista=[reverse_morse_dict.get(letra,"*") for letra in mensaje.split()]
    return "".join(lista)

f=open("morse.txt","w")

lista="--.-..--.-...-..." #aqui va el codigo morse mal escrito para probar todas las posibles traducciones
cantidad_elementos=len(lista)

for n in range(1,cantidad_elementos):
    posicion_coma_grupo=list(combinations(range(1,cantidad_elementos),n))
    
    for posicion_coma in posicion_coma_grupo:
        subconjunto=[]
        mensaje=""
        inicio=0
        
        for single_coma_position in posicion_coma:
            mensaje+=decrypt(lista[inicio:single_coma_position])
            subconjunto.append(lista[inicio:single_coma_position])
            inicio=single_coma_position
        subconjunto.append(lista[inicio:])
        mensaje+=decrypt(lista[inicio:])
        
        #filtrando sin los *
        if "*" in mensaje:
            continue
        
        f.write(str(subconjunto)+" "+mensaje)
        f.write("\n")
        
f.close() 




