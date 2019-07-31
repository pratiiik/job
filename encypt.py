dic = {'A':'E','B':'F','C':'G','D':'H','E':'I',
        'F':'J','G':'K','H':'L','I':'M','J':'N',
        'K':'O','L':'P','M':'Q','N':'R','O':'S',
        'P':'T','Q':'U','R':'V','S':'W','T':'X','U':'Y',
        'V':'Z','W':'A','X':'B','Y':'C','Z':'D'}

message = input("Enter your string: ").upper()
encrypted = ""

for letter in message:
    if letter in dic:
        encrypted += dic[letter]

    else:
        encrypted += letter


print(encrypted)
'chr is used to convert ASCII value into char'
'ord is used to convert chr into ASCII value.'
encrypt = ""
for let in message:
    if let == " ":
        encrypt += let
    elif ord(let) + 5 > ord('Z'):
        encrypt += chr(ord(let)+ 5 -26)

    else:
        encrypt += chr(ord(let)+5)

print(encrypt)

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mes = input("Enter your string:").upper()
enc = ""

for lett in mes:
    if lett == " ":
        enc += lett

    elif ALPHABET.index(lett) + 5 > len(ALPHABET) - 1:
        enc += ALPHABET[ALPHABET.index(lett) + 5 - 26]

    else:
        enc += ALPHABET[ALPHABET.index(lett) + 5]


print(enc)






