import fitur_atm as fitur

"""
1.input jenis kartu client
	masukan kartu
		- kartu BCA
		- kartu mandiri
		- kartu lainnya
	
2. menentukan data/info pada masing" kartu pilihan
	- nomor kartu
	- password kartu
	- jumlah uang
	
3. berikan opsi pilihan 
	- tranfer uang
	- tarik tunai
	- tabung uang

4. algoritma dari setiap opsi pilihan
	
5. output no error & last, penutupan.
"""	
kartu_BCA = {
'nomor' : '220906',
'password' : 'dimas',
'jumlah' : 300000
}
kartu_mandiri = {
'nomor' : '040307',
'password' : 'yunita',
'jumlah' : 250000
}
kartu_lainnya = {
'nomor' : '3945',
'password' : 'smp',
'jumlah' : 1500000
}

print("\twelcome to Dimaz's Bank.")
print('\nLanjut dengan menggunakan kartu?\n1. Kartu BCA\n2. Kartu mandiri\n3. Kartu lainnya -')
kartu = input('pilihan kartu anda : ')
if kartu == '1' or kartu == 'BCA' :
	kartu = kartu_BCA
	fitur.cekPw(kartu, kartu['nomor'], kartu['password'])	
	while fitur.salah :
		a = input("ketik '1' untuk mencoba lagi : ")
		if a != '1' : break
		fitur.cekPw(kartu, kartu['nomor'], kartu['password'])		
	if fitur.salah == False :
		print("berikut adalah beberapa pelayanan mesin ini")
		print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")
		fitur.opsiClient(kartu, kartu_mandiri, kartu_lainnya)
		
elif kartu == '2' or kartu == 'mandiri' :
	kartu = kartu_mandiri
	fitur.cekPw(kartu, kartu['nomor'], kartu['password'])	
	while fitur.salah :
		a = input("ketik '1' untuk mencoba lagi : ")
		if a != '1' : break
		fitur.cekPw(kartu, kartu['nomor'], kartu['password'])		
	if fitur.salah == False :
		print("berikut adalah beberapa pelayanan mesin ini")
		print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")
		fitur.opsiClient(kartu, kartu_BCA, kartu_lainnya)

elif kartu == '3' or kartu == 'lainnya' :
	kartu = kartu_lainnya
	fitur.cekPw(kartu, kartu['nomor'], kartu['password'])	
	while fitur.salah :
		a = input("ketik '1' untuk mencoba lagi : ")
		if a != '1' : break
		fitur.cekPw(kartu, kartu['nomor'], kartu['password'])		
	if fitur.salah == False :
		print("berikut adalah beberapa pelayanan mesin ini")
		print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")
		fitur.opsiClient(kartu, kartu_BCA, kartu_mandiri)

else :
	print("\nMaaf, permintaan anda tidak dapat kami proses.\n\tMohon coba lagi.")
	
