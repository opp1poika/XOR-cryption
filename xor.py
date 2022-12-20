def crypt():
    L = []
    print("Insert key >>", end="")
    key = input()
    print("Insert text>>", end="")
    text = input()
    print("Crypted text<<", end="")
    k = len(key)
    t = len(text)
    for i in range(t):
        L.append(ord(text[i]) ^ ord(key[i % k]))
    print(L)
    
def encrypt():
    L = []
    print("Insert key >>", end="")
    key = input()
    print("Insert list>>", end="")
    nlist = list(map(int, input().split()))
    k = len(key)
    n = len(nlist)
    for i in range(n):
        L.append(chr(nlist[i] ^ ord(key[i % k])))
    print("Encrypted text<<", end="")
    print(*L, sep="")

def main():
    print("Crypt text (1)\nEncrypt text (2)\n>>", end="")
    function = input()
    
    if function == "1":
        crypt()
    if function == "2":
        encrypt()
    main()

main()
