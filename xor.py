#Establish a cryption function
def crypt():
    #Create a list where we store crypted ord() values of chars
    L = []
    
    #User key ipnut
    print("Insert key >>", end="")
    key = input()
    
    #User text input
    print("Insert text>>", end="")
    text = input()
    
    #Store lengths of key and text
    k = len(key)
    t = len(text)
    
    #'XOR' each letter in text with the corresponding key char modulo len(key)
    for i in range(t):
        L.append(ord(text[i]) ^ ord(key[i % k]))
    
    #Print crypted list of numbers
    print("Crypted text<<", end="")
    print(L)
    
#Establish a decryption function
def encrypt():
    #Create a list where we store encrypted chars
    L = []
    
    #User key input
    print("Insert key >>", end="")
    key = input()
    
    #User list input
    print("Insert list>>", end="")
    nlist = list(map(int, input().split()))
    
    #Store lenghts of key and list
    k = len(key)
    n = len(nlist)
    
    #'XOR' each element of list with ord() of key modulo len(key)
    for i in range(n):
        L.append(chr(nlist[i] ^ ord(key[i % k])))
        
    #Print encrypted data
    print("Encrypted text<<", end="")
    print(*L, sep="")

def main():
    #Ask for user selection
    print("Exit program (0)\nCrypt text (1)\nEncrypt text (2)\n>>", end="")
    function = input()
    
    #If statements to decide which function to use
    if function == "0":
        return 0
    if function == "1":
        crypt()
    if function == "2":
        encrypt()
    
    #Call back to main menu
    main()

#Call main menu
main()
