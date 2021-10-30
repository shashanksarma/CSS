import math

print('1) Substitution')
print('2) ROT 13')
print('3) Transpose')
print('4) Double Transposition')
print('5) Vernam Cipher')
a =int(input('Enter the cryptography method:'))

def encryptBySubstitution(text,shift = 1):
    cipher = ""
    shift = shift%26
    for letter in text:
        if(ord(letter)>96 and ord(letter)<=122):
            new_value = (ord(letter) + shift)
            if(new_value > 122):
                new_value -= 26
            cipher += chr((96 + new_value)%96 + 96)
        elif(ord(letter)>64 and ord(letter)<=90):
            new_value = (ord(letter) + shift)
            if(new_value > 90):
                new_value -= 26
            cipher += chr((65 + new_value)%65 + 65)
        else:
            cipher +=chr(ord(letter) + shift)

    return cipher


def decryptBySubstitution(text,shift = 1):
    cipher = ""
    shift = shift%26
    for letter in text:
        if(ord(letter)>96 and ord(letter)<=122):
            new_value = (ord(letter) - shift)
            if(new_value < 97):
                new_value += 26
            cipher += chr((96 + new_value)%96 + 96)
        elif(ord(letter)>64 and ord(letter)<=90):
            new_value = (ord(letter) - shift)
            if(new_value < 65):
                new_value +=26
            cipher += chr((64 + new_value)%64 + 64)
        else:
            cipher +=chr(ord(letter) - shift)
    return cipher


def encryptByVernam(text,key):
    cipher = ""
    for i in range(len(text)):
        cipher += chr(((ord(text[i])-65)^(ord(key[i])-65))+65)
    return cipher


def decryptByVernam(cipher,key):
    text = ""
    for i in range(len(cipher)):
        text += chr(((ord(cipher[i]) - 65)^(ord(key[i]) - 65)) + 65)
    return text


def encryptByTranspose(text,key):
    col = len(key)
    row = math.ceil(len(text)/col)
    # print('The dimensions are: ',row,col,text)

    matrix = []
    for i in range(0,row):
        string = []
        for j in range(0,col):
            string.append("_")
        matrix.append(string)

    # print('The constructed matrix is: ', matrix)

    text_index = 0
    for i in range(0,row):
        for j in range(0,col):
            matrix[i][j] = text[text_index]
            text_index += 1
            if(text_index >= len(text)):
                break
        if(text_index >= len(text)):
            break
    
    # print('The column matrix is: ', matrix)
    refer_key = sorted(key)
    # print('The sorted list is: ',refer_key)

    cipher = ""
    for i in range(0,col):
        iterate_col_index = key.index(refer_key[i])
        key = key[:iterate_col_index] + '-' + key[iterate_col_index+1:]
        for j in range(0,row):
            cipher += matrix[j][iterate_col_index]
    
    return cipher

def decryptByTranspose(cipher,key):
    col = len(key)
    row = math.ceil(len(cipher)/col)

    matrix = []
    for i in range(0,row):
        string = []
        for j in range(0,col):
            string.append("_")
        matrix.append(string)
    refer_key = sorted(key)    
    cipher_index = 0
    for i in range(0,col):
        iterate_col_index = key.index(refer_key[i])
        key = key[:iterate_col_index] + '-' + key[iterate_col_index+1:]
        for j in range(0,row):
            matrix[j][iterate_col_index] = cipher[cipher_index]
            cipher_index += 1
            if(cipher_index >= len(cipher)):
                break
        if(cipher_index >= len(cipher)):
            break

    text = ""
    for i in range(0,row):
        for j in range(0,col):
            # if(matrix[i][j] == "_"):
            #     continue
            text += matrix[i][j]

    return text


def filterText(text):
    string = ""
    for letter in text:
        if(letter!="_"):
            string+=letter
    return string


if a == 1:
    text = input('Enter Plain Text: ')
    key = int(input('No of position to be shifted: '))
    encrpytedText = encryptBySubstitution(text,key)
    print('Encrypted Message',encrpytedText)
    print('Decrypted Message',decryptBySubstitution(encrpytedText,key))

elif a == 2:
    text = input('Enter Plain Text to be encrypted: ')
    encrpytedText = encryptBySubstitution(text, 13)
    print('Encrypted Message', encrpytedText)
    print('Decrypted Message', decryptBySubstitution(encrpytedText, 13))

elif a == 3:
    text = input('Enter Plain Text to be encrypted: ')
    key = input('Enter key: ')
    encryptedText = encryptByTranspose(text,key)
    decryptedText = decryptByTranspose(encryptedText,key)
    print("The encrypted cipher is: ",filterText(encryptedText))
    print("The decrypted text is: ",filterText(decryptedText))

elif a == 4:
    text = input('Enter Plain Text to be encrypted: ')
    key1 = input('Enter key 1: ')
    key2 = input('Enter key 2: ')
    encryptedText1 = (encryptByTranspose(text,key1))
    encryptedText2 = (encryptByTranspose(encryptedText1,key2))
    decryptedText1 = decryptByTranspose(encryptedText2,key2)
    decryptedText2 = decryptByTranspose(encryptedText1,key1)
    print("The encrypted cipher is: ",filterText(encryptedText2))
    print("The decrypted text is: ",filterText(decryptedText2))

elif a == 5:
    text = input('Enter Plain Text to be encrypted: ')
    key = input('Enter key of the same length as the Plain Text:')
    while(len(text)!=len(key)):
        key = input('Enter key of the same length as the Plain Text: ')
    encryptedText = (encryptByVernam(text,key))
    decryptedText = decryptByVernam(encryptedText,key)
    print("The encrypted cipher is: ",(encryptedText))
    print("The decrypted text is: ",(decryptedText))
