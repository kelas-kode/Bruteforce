# coded by Tegar Sabila

from itertools import product
logo="""
──▄▀▀▀▄───────────────      Program BruteForce
──█───█───────────────
─███████─────────▄▀▀▄─     Author : Tegar Sabila
░██─▀─██░░█▀█▀▀▀▀█░░█░     Github : kelas-kode
░███▄███░░▀░▀░░░░░▀▀░░
"""
def CariPassword(karakter, fungsi, lihat=50, format_="%s"):
    password = None
    upaya = 0
    ukuran = 1
    berhenti = False
    while not berhenti:
        for pw in product(karakter, repeat=ukuran):
            password="".join(pw)
            if upaya % lihat == 0:
                print(format_ % password)
            if fungsi(password):
                berhenti=True
                break
            else:
                upaya+=1
        ukuran+=1
    return password, upaya

def DapatkanKarakter():
    karakter = []
    for id_ in range(ord("A"), ord("Z") + 1):
        karakter.append(chr(id_))
    for nomor in range(10):
        karakter.append(str(nomor))
    return karakter

if __name__ == "__main__":
    import time, os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    pw = input("Masukan password : ")
    print("\n")

    def tesFungsi(password):
        global pw
        if password == pw:
            return True
        else:
            return False
    karakter = DapatkanKarakter()
    waktu = time.process_time()
    password, upaya = CariPassword(karakter, tesFungsi, lihat=1000, format_="Mencoba = %s")
    print(f"\n Password Cocok :{password} \n upaya: {upaya}\n waktu: {waktu} \n")