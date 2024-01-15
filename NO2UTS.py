import base64
import requests

def enkripsi_caesar(teks, geser):
  teks_sandi = ""
  for i in range(len(teks)):
    karakter = teks[i]
    index_baru = ord(karakter) - geser
    if index_baru < ord("A"):
      index_baru = ord("Z") + index_baru - ord("A")
    karakter_baru = chr(index_baru)
    teks_sandi += karakter_baru
  return teks_sandi

def encode_base64(teks):
  data_biner = ''.join([format(ord(c), '08b') for c in teks])
  blok_biner = [data_biner[i:i+3] for i in range(0, len(data_biner), 3)]
  karakter_ascii = [base64.b64encode(blok).decode('utf-8') for blok in blok_biner]
  return ''.join(karakter_ascii)

def kirim_pesan_whatsapp(teks, nomor_wa):
  url = "https://api.whatsapp.com/send?phone={}".format(nomor_wa)
  data = {"text": teks}
  response = requests.post(url, data=data)
  return response.status_code == 200

teks = "Jangan lupa sholat!"
geser = 3
teks_sandi = enkripsi_caesar(teks, geser)
teks_sandi_base64 = encode_base64(teks_sandi)

hasil = kirim_pesan_whatsapp(teks_sandi_base64, "08123456789")

if hasil:
  print("Pesan berhasil dikirim!")
else:
  print("Pesan gagal dikirim!")