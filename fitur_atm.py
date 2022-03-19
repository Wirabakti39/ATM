#4. Algoritma, function/method di balik layar.

#fungsi ngecek nomor + password kartu pilihan
def cekPw(card, no, pw) :
	n = input(f'\n\tmasukan nomor dari {card["nama"]} anda : ')
	p = input(f'\tmasukan password dari {card["nama"]} anda : ')
	
	global salah
	if n == no and p == pw :
		salah = False
		print(f"\nRegistrasi sukses.\nUang dalam kartu {no} berjumlah Rp. {card['jumlah']}\n")
	else :
		salah = True
		print('\nNomor / password tidak cocok dengan ', card["nama"], ' anda.\n')

#fungsi dari fitur transfer uang
def transfer_uang(card, card1, card2) :
	while True :
		try :
			transfer = int(input("\n\tmasukan jumlah yang akan ditransfer : Rp. "))
			tujuan = input(f"\tuang Rp. {transfer} akan di transfer ke?\n\tmasukan nomor kartu yang dituju : ")
			if transfer > card["jumlah"] :
				print(f'\nTransfer gagal, isi saldo {card["nama"]} anda tidak mencukupi')
				z = input("\n\tketik 0 untuk coba lagi : ")															
				if z != "0" : break
			else :
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
				elif tujuan == card["nomor"] :
					print("\nMaaf, anda tidak bisa memasukan nomor kartu anda sendiri.")
					z = input("\n\tKetik 0 untuk coba lagi : ")
					if z != "0" : break
				else :
					print("\nTransaksi gagal,\nmesin ini tidak menyediakan layanan untuk nomor ", tujuan)
					z = input("\n\tKetik 0 untuk coba lagi : ")
					if z != "0" : break	
		except ValueError :
			z = input("\nYang anda masukan bukan angka, coba lagi.\n\n\tketik 0 untuk coba lagi : ")
			if z != "0" : break							

#fungsi dari fitur tarik tunai
def tarik_tunai(card) :
	while True :
		try :
			jumlah = int(input("\n\tmasukan jumlah uang yang akan ditarik : Rp "))
			if jumlah > card["jumlah"] :
				print(f'\nPenarikan gagal, isi saldo {card["nama"]} anda tidak mencukupi')
				z = input("\n\tketik 0 untuk coba lagi : ")															
				if z != "0" : break	
			else :
				card["jumlah"] -= jumlah
				print("\nPenarikan uang sejumlah Rp. ", jumlah, " berhasil.")
				break		
				return card																																																																																																																																																																																																																
		except ValueError :
			z = input("\nYang anda masukan bukan angka, coba lagi.\n\n\tketik 0 untuk coba lagi : ")
			if z != "0" : break	

#fungsi dari fitur tabung uang			
def tabung_uang(card) :
	while True :
		try :
			uang = int(input("\n\tuang yang anda pegang berjumlah? : Rp "))
			nabung = int(input("\tmasukan jumlah uang yg akan ditabung : Rp "))
			if uang >= nabung :
				card["jumlah"] += nabung																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																								
				uang -= nabung																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																								
				print(f'\nBerhasil, jumlah uang yg anda pegang sekarang Rp. {uang}\nRp. {nabung} berhasil ditambahkan ke {card["nama"]} ({card["nomor"]}) anda.')	
				break
				return card
			else :					
				print("Proses menabung gagal.\nJumlah uang yang anda pegang ( < ) jumlah yang akan ditabung")										
				z = input("\n\tketik 0 untuk coba lagi : ")															
				if z != "0" : break																			
		except ValueError :																																	
			print("\nProses menabung gagal.\nYang anda masukan bukan angka, atau anda memasukan angka desimal.")
			z = input("\n\tketik 0 untuk coba lagi : ")															
			if z != "0" : break

#fungsi untuk memilih fitur yang akan digunakan																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										
def opsiClient(kartu_anda, kartu_1, kartu_2) :
	while True :
		opsi = input("Silahkan pilih keperluan anda : ")
		if opsi == "1" :
			transfer_uang(kartu_anda, kartu_1, kartu_2)
			print(f'\nSisa saldo {kartu_anda["nama"]} ({kartu_anda["nomor"]}) anda : Rp. {kartu_anda["jumlah"]}')
			break
		elif opsi == "2" :
			tarik_tunai(kartu_anda)
			print(f'\nSisa saldo {kartu_anda["nama"]} ({kartu_anda["nomor"]}) anda : Rp. {kartu_anda["jumlah"]}')
			break
		elif opsi == "3" :
			tabung_uang(kartu_anda)
			print(f'\nSisa saldo {kartu_anda["nama"]} ({kartu_anda["nomor"]}) anda : Rp. {kartu_anda["jumlah"]}')
			break
		else :
			print("\nMaaf, mesin ini tidak menyediakan permintaan anda.")
			z = input("\n\tketik 0 untuk coba lagi : ")
			print("\n")
			if z != "0" : break
