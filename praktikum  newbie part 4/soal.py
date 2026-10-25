soal = [
    "klub yang pernah mempermalukan MU dikandangnya sendiri adalah?",
    "klub inggris yang mempunyai gelar terbanyak adalah?",
    "klub yang mempunyai 6 trofi ucl adalah?",
    "jadi siapa klub terbaik di inggris??",
]

kunci = ["LIVERPOOL", "LIVERPOOL", "LIVERPOOL", "LIVERPOOL"]
skor = 0

for nomor in range(len(soal)):
    print(f"\nSoal {nomor + 1}: {soal[nomor]}")
    jawaban = input("jawabane koen: ")

    if jawaban.strip().lower() == kunci[nomor].lower():
        print("JELASSSSS")
        skor += 1
    else:
        print(f"BODOKK. JELAS KING {kunci[nomor]} LAH")

print(f"\nSkor akhir: {skor}/{len(soal)}")