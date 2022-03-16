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
'nomor' : '111',
'password' : 'satu1',
'jumlah' : 1000000
}
kartu_mandiri = {
'nomor' : '222',
'password' : 'dua2',
'jumlah' : 2000000
}
kartu_lainnya = {
'nomor' : '12345',
'password' : 'lain_else',
'jumlah' : 500000
}

def cekPw(card, no, pw) :
	n = input("\n\tmasukan nomor kartu anda : ")
	p = input(f"\tmasukan password dari kartu {n} : ")
	
	global salah
	if n == no and p == pw :
		salah = False
		print(f"\n\tregister succes.\n\tuang dalam kartu {no} berjumlah Rp. {card['jumlah']}\n")
	else :
		salah = True
		print('\n\tnomor atau password kartu anda invalid.\n')
	
print("\twelcome to Dimaz's Bank.")
print('\nLanjut dengan menggunakan kartu?\n1. Kartu BCA\n2. Kartu mandiri\n3. Kartu lainnya -')
kartu = input('pilihan kartu anda : ')
if kartu == '1' or kartu == 'BCA' :
	kartu = kartu_BCA
	cekPw(kartu, kartu['nomor'], kartu['password'])	
	while salah :
		a = input("ketik '1' untuk mencoba lagi : ")
		if a != '1' : break
		cekPw(kartu, kartu['nomor'], kartu['password'])		
	if salah == False :
		print("berikut adalah beberapa pelayanan mesin ini")
		print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")

elif kartu == '2' or kartu == 'mandiri' :
	kartu = kartu_mandiri
	cekPw(kartu, kartu['nomor'], kartu['password'])
	while salah :
		a = input("ketik '1' untuk mencoba lagi : ")
		if a != '1' : break
		cekPw(kartu, kartu['nomor'], kartu['password'])		
	if salah == False :
		print("berikut adalah beberapa pelayanan mesin ini")
		print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")

elif kartu == '3' or kartu == 'lainnya' :
	kartu = kartu_lainnya
	cekPw(kartu, kartu['nomor'], kartu['password'])
	while salah :
		a = input("ketik '1' untuk mencoba lagi : ")
		if a != '1' : break
		cekPw(kartu, kartu['nomor'], kartu['password'])		
	if salah == False :
		print("berikut adalah beberapa pelayanan mesin ini")
		print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")

else :
	print("\nMaaf, permintaan anda tidak dapat kami proses.\n\tMohon coba lagi.")
	



