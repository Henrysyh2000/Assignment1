def anagram(string1, string2):
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """
    # To do
    dic1 = {}
    dic2 = {}
    for i in string1:
        if i.isalpha():
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 0
        else:
            continue
        
    for i in string2:
        if i.isalpha():
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 0
        else:
            continue
    if dic1 != dic2:
        return False
    return True
        
    
        
    
'''
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    string1 = "william shakespeare"
    string2 = "i am a weakish speller"
    print(anagram(string1, string2))   

    string1 = "software"
    string2 = "swear oft"
    print(anagram(string1, string2))  

if __name__ == '__main__':
    main()
