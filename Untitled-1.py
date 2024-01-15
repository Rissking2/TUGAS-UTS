def dekripsi_caesar(teks_sandi, geser):
  teks_asli = ""
  for i in range(len(teks_sandi)):
    karakter = teks_sandi[i]
    index_baru = ord(karakter) - geser
    if index_baru < ord("A"):
      index_baru = ord("Z") + index_baru - ord("A")
    karakter_baru = chr(index_baru)
    teks_asli += karakter_baru
  return teks_asli

teks_sandi = "Yzcv lbh qrphvq qvfgnhw!"
geser = 3

teks_asli = dekripsi_caesar(teks_sandi, geser)

print("Teks asli:", teks_asli)