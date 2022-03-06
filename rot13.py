#ROT13 is a simple letter substitution cipher that replaces a letter with
#the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

import string

def rot13(message):
    alphabet = [string.ascii_lowercase*2, string.ascii_uppercase*2, string.ascii_letters]
    new_message = []
    for i in message:
        if i not in alphabet[2]:
            new_message.append(i)
        else:
            if i in alphabet[0]:
                new_message.append(alphabet[0][alphabet[0].index(i)+13])
            else:
                new_message.append(alphabet[1][alphabet[1].index(i)+13])
    final_result = ''
    for i in new_message:
        final_result += i
    print(final_result)
    return final_result

rot13('My name is not known and still encoded')

def de_rot13(ms):
    alphabet = [string.ascii_lowercase*2, string.ascii_uppercase*2, string.ascii_letters]
    print(alphabet)
    new_message = []
    for i in ms:
        if i not in alphabet[2]:
            new_message.append(i)
        else:
            if i in alphabet[0]:
                new_message.append(alphabet[0][alphabet[0].index(i)-13])
            else:
                new_message.append(alphabet[1][alphabet[1].index(i)-13])
    final_result = ''
    for i in new_message:
        final_result += i
    print(final_result)
    return final_result

de_rot13('Zl anzr vf abg xabja naq fgvyy rapbqrq')