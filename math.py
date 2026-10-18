K = "IIFEUVFE AREIHLER RENTSRLT EFENEEEX PTHECEUE PELMLNRT SNBSSWTE"

words = K.split()

while True:
    p = input("enter combination: ")
    for i in list(p):
        print(str(i) + ": " + words[int(i) - 1])
    if p == "exit":
        break