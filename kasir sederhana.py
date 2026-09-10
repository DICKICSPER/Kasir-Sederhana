print("====KASIR SEDERHANA====")
nama_barang = str(input("NAMA BARANG :"))
harga = int(input("HARGA BARANG :"))
jumlah = int(input("JUMLAH BARANG :"))

total = harga * jumlah
if total >=  100000:
 diskon = 10
elif total  >=  50000:
 diskon = 5
else:
  diskon = 0

potongan = total * diskon // 100
total_bayar = total - potongan

while True:
  uang = int(input("MASUKAN JUMLAH UANG KAMU:"))
  kembalian = uang - total_bayar
  if uang < total_bayar:
   print("""MAAF UANG TIDAK CUKUP !
  ================================= """)
  else:
   print(f"""==STRUK BELANJA ANDA==
NAMA BARANG : {nama_barang}
HARGA       : {harga}
JUMLAH      : {jumlah}
TOTAL       : {total}
DISKON      : {potongan}
TOTAL SEMUA : {total_bayar}
UANG ANDA   : {uang}
KEMBALIAN   : {kembalian}
==TERIMAKASIH SUDAH BERBELANJA==""")
   break

