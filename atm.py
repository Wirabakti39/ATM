"""
1. menentukan data/info pada setiap kartu 
	- nomor kartu
	- password kartu
	- jumlah uang	
2. input jenis kartu client
	masukan kartu
		- kartu BCA
		- kartu mandiri
		- kartu BRI	
3. berikan opsi pilihan 
	- tranfer uang
	- tarik tunai
	- tabung uang
4. algoritma dari setiap opsi pilihan	

5. output no error & last, penutupan.
"""
import fitur_atm as fitur

#1. data/info kartu	
kartu_BCA = {
'nama' : 'kartu BCA',
'nomor' : '220906',
'password' : 'dimas',
'jumlah' : 300000
}
kartu_mandiri = {
'nama' : 'kartu mandiri',
'nomor' : '193943',	#Bebas mengubah value nya asal logis
'password' : 'wirba',
'jumlah' : 250000
}
kartu_BRI = {
'nama' : 'kartu BRI',
'nomor' : '4243',
'password' : 'sma',
'jumlah' : 1500000
}

print("\twelcome to Dimaz's Bank.")
while True :
	#1. input jenis kartu
	print('\nLanjut dengan menggunakan kartu?\n1. Kartu BCA\n2. Kartu mandiri\n3. Kartu BRI')
	kartu = input('pilihan kartu anda : ')
	if kartu == '1' or kartu == 'BCA' :
		kartu = kartu_BCA
		#fitur login kartu sesuai data pada no. 1
		fitur.cekPw(kartu, kartu['nomor'], kartu['password'])	
		while fitur.salah :
			a = input("\tketik '0' untuk mencoba lagi : ")
			if a != '0' : break
			fitur.cekPw(kartu, kartu['nomor'], kartu['password'])		
		if fitur.salah == False :
			#3. opsi pilihan layanan 
			print("berikut adalah beberapa pelayanan mesin ini")
			print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")
			fitur.opsiClient(kartu, kartu_mandiri, kartu_BRI)
			break
		break	
	elif kartu == '2' or kartu == 'mandiri' :
		kartu = kartu_mandiri
		fitur.cekPw(kartu, kartu['nomor'], kartu['password'])	
		while fitur.salah :
			a = input("\tketik '0' untuk mencoba lagi : ")
			if a != '0' : break
			fitur.cekPw(kartu, kartu['nomor'], kartu['password'])		
		if fitur.salah == False :
			print("berikut adalah beberapa pelayanan mesin ini")
			print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")
			fitur.opsiClient(kartu, kartu_BCA, kartu_BRI)
			break
		break	
	elif kartu == '3' or kartu == 'BRI' :
		kartu = kartu_BRI
		fitur.cekPw(kartu, kartu['nomor'], kartu['password'])	
		while fitur.salah :
			a = input("\tketik '0' untuk mencoba lagi : ")
			if a != '0' : break
			fitur.cekPw(kartu, kartu['nomor'], kartu['password'])		
		if fitur.salah == False :
			print("berikut adalah beberapa pelayanan mesin ini")
			print("1. Transfer uang\n2. Tarik uang tunai\n3. Taruh/tabung uang")
			fitur.opsiClient(kartu, kartu_BCA, kartu_mandiri)
			break
		break	
	else :
		print("\nMaaf, permintaan anda tidak dapat kami proses.\nMohon coba lagi.")
		a = input("\n\tketik '0' untuk mencoba lagi : ")
		if a != '0' : break
#5. apapun inputan user tidak akan mengalami error.		
print("Terimakasih telah menggunkan layanan kami..\nHave a Nice Day!")
