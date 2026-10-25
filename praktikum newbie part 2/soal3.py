harga_satuan = float(input("Harga satuan:Rp."))
jumlah_barang = float(input("Jumlah barang:"))
persentase_diskon = float(input("Persentase diskon:"))

subtotal = harga_satuan * jumlah_barang
nominal_diskon = subtotal * persentase_diskon / 100
total_bayar = subtotal - nominal_diskon

print("Subtotal:Rp.", subtotal)
print("Nominal diskon:Rp.", nominal_diskon)
print("Total bayar:Rp.", total_bayar)