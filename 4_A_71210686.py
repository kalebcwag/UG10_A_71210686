#artikel skor pertandingan sepak bola

artikel=input("""Artikel: """)
klub=input("Nama Klub: ")
skor=input("Skor: ")

if klub in artikel and skor in artikel:
    print("Hasil pencarian ditemukan")
elif klub in artikel and not(skor in artikel):
    print("Hanya kata {} yang ditemukan pada artikel ini".format(klub))
elif not(klub in artikel) and skor in artikel:
    print("Hanya skor {} yang ditemukan pada artikel ini".format(skor))
else:
    print("Hasil pencarian {} dan {} tidak ditemukan".format(klub,skor))
