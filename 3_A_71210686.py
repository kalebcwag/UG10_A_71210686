#Membuat pola mendatar atau menurun

pilih=input("Mendatar/Menurun?: ")
if pilih=="Mendatar":
    kol=int(input("Masukkan kolom: "))
    print("#"*kol)
elif pilih=="Menurun":
    bar=int(input("Masukkan baris: "))
    print(("*"+"\n")*bar)
else:
    print("Pola tidak dikenali")
