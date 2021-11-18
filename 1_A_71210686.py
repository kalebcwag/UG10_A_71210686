ug=float(input("Masukkan nilai rata-rata UG anda: "))
tts=float(input("Masukkan nilai TTS anda: "))
tas=float(input("Masukkan nilai TAS anda: "))

print("="*24)

tot=(70/100*ug)+(15/100*tts)+(15/100*tas)

print("Nilai anda : ",tot)

if tot>=85:
    print("Nilai huruf anda : A")
elif tot<85 and tot>=80:
    print("Nilai huruf anda : A-")
elif tot<80 and tot>=75:
    print("Nilai huruf anda : B+")
elif tot<75 and tot >=70:
    print("Nilai huruf anda : B")
elif tot<70 and tot>=65:
    print("Nilai huruf anda : B-")
elif tot<65 and tot>=60:
    print("Nilai huruf anda : C+")
elif tot<60 and tot>=55:
    print("Nilai huruf anda : C")
elif tot<55 and tot>=45:
    print("Nilai huruf anda : D")
elif tot<45 and tot>=0:
    print("Nilai huruf anda : E")
