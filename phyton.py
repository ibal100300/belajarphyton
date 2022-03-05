print ("""sensus penduduk kecamatan wua-wua, Kendari""")

Nama = input("nama:") 
TTL = input("TTL:")
Alamat = input("alamat:")
Nik = input("nik:")
Kelurahan = input("kelurahan:")


teks = "nama: {}\nTTL: {}\nalamat: {}\nnik: {}\nkelurahan: {}".format(Nama, TTL, Alamat, Nik, Kelurahan)

data = open("data.txt", "w")

data.write(teks)

data.close()