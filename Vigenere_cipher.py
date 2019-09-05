def vigenere_encrypt(plain, key):
    """
    :param plain: String -- a python input string. The plain text.
    :param key: String -- a python input string. The key.

    :return: String -- the cipher python string text.
    """
    # To do
    res = ""
    table = [[]]
    for i in range(26):
        table[0].append(chr(65 + i))
    for i in range(25):
        temp = table[i][1 : len(table[0])]
        temp.append(table[i][0])
        table.append(temp)   
    if len(key) < len(plain):
        i = 0
        num = len(key)
        while len(key) != len(plain):
            key += key[i]
            i += 1
            i %= num
    elif len(key) > len(plain):
        key = key[:len(plain)]
        print(key)
    for i in range(len(plain)):
        res += table[ord(plain[i]) - 65][ord(key[i]) - 65]
    return res
    
        
        
def vigenere_decrypt(cipher, key):
    '''
    :param cipher: String -- a python input string. The cipher text.
    :param key: String -- a python input string. The key.

    :return: String -- the plain python string text.
    '''
    # To do
    res = ""
    table = [[]]
    for i in range(26):
        table[0].append(chr(65 + i))
    for i in range(25):
        temp = table[i][1 : len(table[0])]
        temp.append(table[i][0])
        table.append(temp)
    if len(key) < len(cipher):
        i = 0
        num = len(key)
        while len(key) != len(cipher):
            key += key[i]
            i += 1
            i %= num
    elif len(key) > len(cipher):
        key = key[:len(cipher)]

    count = 0
    for i in key:
        count2 = 0
        num = ord(i) - 65
        for c in table[num]:
            #print(count, count2)
            #print(count)
            if c == cipher[count]:
                res += table[0][count2]
            count2 += 1
        count += 1
    return res


'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''
def main():
    print(vigenere_encrypt("ATTACKATDAWN", "NYUSH"))   # NRNSJXYNVHJL

    print(vigenere_encrypt("DATASTRUCTURE", "NYUSH"))   # QYNSZGPOUAHPY

    print(vigenere_encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NYUSH"))  # NZWVLSEBAQXJGFVCOLKAHTQPFM

    print(vigenere_encrypt("CUTE", "NYUSH"))  # PSNW

    print(vigenere_decrypt("NRNSJXYNVHJL", "NYUSH"))   # ATTACKATDAWN
    print(vigenere_decrypt("QYNSZGPOUAHPY", "NYUSH"))   # DATASTRUCTURE
    print(vigenere_decrypt("NZWVLSEBAQXJGFVCOLKAHTQPFM", "NYUSH"))   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(vigenere_decrypt("PSNW", "NYUSH"))  # CUTE

if __name__ == '__main__':
    main()
