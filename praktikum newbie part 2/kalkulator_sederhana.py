# Program kalkulator sederhana
print("=== Kalkulator Sederhana ===")
angka1 = int(input("Masukan angka pertama: "))
operator = input("Masukan operator(+,-,*,/)")
angka2 = int(input("Masukan angka kedua: "))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    hasil ="Operator tidak dikenali"
print("Hasil:", hasil)
