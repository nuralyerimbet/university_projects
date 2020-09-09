
print("Decoding or encoding?\nEncoding = 0, Decoding = 1")
a=int(input())

print("Type the text:")
txt=input()
txt.lower()

import string
alpha=string.ascii_lowercase
key = "qwertzuioplkjhgfdsayxcvbnm"

def encode(text):
    text=list(text)
    for i in range(len(text)):
        if text[i] in alpha:
            x=alpha.find(text[i])
            text[i]=key[x]
        else:
            text[i]=text[i]
    encoded_text = ''.join(text)
    return encoded_text


def decode(encoded_text):
    encoded_text=list(encoded_text)
    for i in range(len(encoded_text)):
        if encoded_text[i] in key:
            x=key.find(encoded_text[i])
            encoded_text[i]=alpha[x]
        else:
            encoded_text[i]=encoded_text[i]

    text = ''.join(encoded_text)
    return text

if a==0:
    print(encode(txt))
elif a==1:
    print(decode(txt))
else:
    print("I don't understand")
    
