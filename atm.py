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
#start
		
kartu_BCA = {
'nomor' : '67729',
'password' : 'dimas1',
'jumlah' : 1000000
}
kartu_mandiri = {
'nomor' : '13555',
'password' : 'dimas2',
'jumlah' : 2000000
}
kartu_lainnya = {
'nomor' : '00000',
'password' : 'yunita',
'jumlah' : 500000
}

def cekPw(card, no, pw) :
	n = input(f"\n\tmasukan nomor kartu anda : ")
	p = input(f"\tmasukan password dari kartu {n} : ")
	
	global salah
	if n == no and p == pw :
		salah = False
		print(f"\nRegistrasi sukses.\nUang dalam kartu {no} berjumlah Rp. {card['jumlah']}\n")
	else :
		salah = True
		print('\n\tnomor atau password kartu anda invalid.\n')

def transfer_uang(card, card1, card2) :
	while True :
		transfer = int(input("\n\tmasukan jumlah yang akan ditransfer : Rp. "))
		tujuan = input(f"\tuang Rp. {transfer} akan di transfer ke?\n\tmasukan no. kartu yang dituju : ")
		card["jumlah"] -= transfer
		if tujuan == card1["nomor"] :
			card1["jumlah"] += transfer
			print(f'\nTransaksi ke nomor kartu {card1["nomor"]} sukses.\nRp. {transfer} telah dikurangi dari saldo anda')
			break
			return card, card1
		elif tujuan == card2["nomor"] :
			card2["jumlah"] += transfer
			print(f'\nTransaksi ke nomor kartu {card2["nomor"]} sukses.\nRp. {transfer} telah dikurangi dari saldo anda')
			break
			return card, card2
		else :
			print("\nTransaksi gagal,\nmesin ini tidak menyediakan layanan untuk nomor ", tujuan)
			z = input("\nKetik 0 untuk coba lagi : ")
			if z != "0" : break
							
def opsiClient(jenis_kartu_anda, jenis_1, jenis_2) :
	opsi = input("Silahkan pilih keperluan anda : ")
	if opsi == "1" :
			transfer_uang(jenis_kartu_anda, jenis_1, jenis_2)
			
	
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
		opsiClient(kartu, kartu_mandiri, kartu_lainnya)
		
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
		opsiClient(kartu, kartu_BCA, kartu_lainnya)

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
		opsiClient(kartu, kartu_BCA, kartu_mandiri)

else :
	print("\nMaaf, permintaan anda tidak dapat kami proses.\n\tMohon coba lagi.")
	
