#Membuat kalkulator advanced sederhana

print("#"*28)
print("Kalkulator Advance Sederhana")
print("#"*28)

print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

menu=int(input("Masukkan menu yang anda pilih: "))
if menu==1:
    bil=float(input("Masukkan bilangan yang ingin dibagi: "))
    bagi=float(input("Masukkan bilangan pembagi: "))
    print("Sisa hasil bagi {} dibagi dengan {} adalah".format(bil,bagi),bil%bagi)
elif menu==2:
    bil=float(input("Masukkan bilangan yang ingin dibagi: "))
    bagi=float(input("Masukkan bilangan pembagi: "))
    bulat=round(bil/bagi)
    if bulat>(bil/bagi):
        print("Hasil pembagian {} dibagi dengan {} dibulatkan kebawah adalah".format(bil,bagi),bulat-1)
    else:
        print("Hasil pembagian {} dibagi dengan {} dibulatkan kebawah adalah".format(bil,bagi),bulat)
elif menu==3:
    kubik=float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    print("Akar kubik dari {} adalah".format(kubik),kubik//3)
else:
    print("Menu yang anda pilih tidak tersedia")
    
