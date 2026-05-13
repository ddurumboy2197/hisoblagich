def soz_soni(matn_fayli):
    try:
        with open(matn_fayli, 'r') as file:
            matn = file.read()
            sozlar = matn.split()
            return len(sozlar)
    except FileNotFoundError:
        return "Fayl topilmadi"

print(soz_soni("matn.txt"))
