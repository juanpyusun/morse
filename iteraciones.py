# import itertools

# mylist = [1, 2, 3, 4]# this is the list from which to draw the subsets

# print (mylist)# the first subsequence of the list is the list itself
# # iterating through the possible numbers of commas to be distributed
# for n in range(1, len(mylist)):
#     comma_positions_comb = list( itertools.combinations(range(1,len(mylist)), n) )
#     # iterating through the combinations of comma positions
#     for comma_positions in comma_positions_comb:
#         subset = []
#         start_id = 0
#         # iterating through the specific comma positions in the given combination
#         for single_comma_position in comma_positions:
#             subset.append(mylist[start_id:single_comma_position])
#             start_id = single_comma_position
#         # the last bit of the list must be appended by hand
#         subset.append(mylist[start_id:])
#         print (subset)

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
f=open("morse_finalconS.txt","w")
lista="--.-..--.-...-..."
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
        if "*" in mensaje:
            continue
        if mensaje.endswith("S"):
            f.write(str(subconjunto)+" "+mensaje)
            f.write("\n")
        print(subconjunto," ",mensaje)

print([lista])   
f.close() 




