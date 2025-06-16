import random

codes = {
    'Alphanum': ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'),
    'Symbols': ('!','@','#','$','%','^','&','*','(',')','<','>','?','/','\\','|','~','_','-','+','=','{','}','[',']',';',':',',','.','`',"'",'"',' '),
    'Alphanum_ENC': ('ⴰ','ⴱ','ⴳ','ⴷ','ⴹ','ⴻ','ⴼ','ⴽ','ⵀ','ⵃ','ⵄ','ⵅ','ⵇ','ⵉ','ⵊ','ⵍ','ⵎ','ⵏ','ⵓ','ⵔ','ⵕ','ⵖ','ⵙ','ⵚ','ⵛ','ⵜ','ⵟ','ⵡ','ⵢ','ⵣ','ⵥ','ⵯ','ⴲ','ⴴ','ⴵ','ⴶ'),
    'Symbols_ENC': ('ⴰ','ⴱ','ⴳ','ⴷ','ⴹ','ⴻ','ⴼ','ⵀ','ⵃ','ⵄ','ⵅ','ⵇ','ⵊ','ⵍ','ⵎ','ⵏ','ⵓ','ⵔ','ⵕ','ⵖ','ⵙ','ⵚ','ⵛ','ⵜ','ⵟ','ⵡ','ⵢ','ⵣ','ⵥ','ⵯ','ⴲ','ⴴ','ⴵ'),
    'Alphanum_ENC_sel': ('ⴸ','ⴺ','ⴿ','ⵁ'),
    'Symbols_ENC_sel': ('ⵒ','ⵝ','ⵞ','ⵠ')
}

def encrypt(text):
    output = ''
    for letter in text:
        if letter in codes['Alphanum']:
            output += random.choice(codes['Alphanum_ENC_sel'])
            output += codes['Alphanum_ENC'][codes['Alphanum'].index(letter)]
        elif letter in codes['Symbols']:
            output += random.choice(codes['Symbols_ENC_sel'])
            output += codes['Symbols_ENC'][codes['Symbols'].index(letter)]
    return output

def decrypt(text):
    output = ''
    for i in range(int(len(text)/2)):
        if text [i*2] in codes['Alphanum_ENC_sel']:
            output += codes['Alphanum'][codes['Alphanum_ENC'].index(text[i*2+1])]
        elif text [i*2] in codes['Symbols_ENC_sel']:
            output += codes['Symbols'][codes['Symbols_ENC'].index(text[i*2+1])]
    return output

if __name__ == '__main__':
    ED = input("Encrypt or decrypt? [E/D]:")[0].lower()
    input = input("Input text to " + ("encrypt" if ED == 'e' else  "decrypt") + ":").lower()
    output = ''

    if ED == 'e':
        output = encrypt(input)
    else:
        output = decrypt(input)
        
    print(output)