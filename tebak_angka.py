import random

def main():
    print("Tebak satu angka antara 1 sampai 10")
    angka_acak = random.randint(1, 10)

    ketemu = False

    while not ketemu:
        tebak = input("tebakanmu : ")
        tebak = int(tebak)
        if tebak == angka_acak:
            print("Tebakanmu benar !!!")
            ketemu = True

        if tebak > angka_acak:
            print("Tebakanmu terlalu besar !!!")

        if tebak < angka_acak:
            print("Tebakanmu terlalu kecil !!!")




main()