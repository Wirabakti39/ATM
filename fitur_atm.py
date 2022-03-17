
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
		elif tujuan == card["nomor"] :
			print("\nMaaf, anda tidak bisa memasukan nomor kartu anda sendiri.")
			z = input("\nKetik 0 untuk coba lagi : ")
			if z != "0" : break
		else :
			print("\nTransaksi gagal,\nmesin ini tidak menyediakan layanan untuk nomor ", tujuan)
			z = input("\nKetik 0 untuk coba lagi : ")
			if z != "0" : break												

def tarik_tunai(card) :
	while True :
		try :
			jumlah = int(input("\n\tmasukan jumlah uang yang akan ditarik : Rp "))
			card["jumlah"] -= jumlah
			print("\nPenarikan uang sejumlah ", jumlah, " berhasil.")
			break																																																																																																																																																																																																																		
		except ValueError :
			z = input("\nYang anda masukan bukan angka, coba lagi.\n\n\tketik 0 untuk coba lagi : ")
			if z != "0" : break	
																																																																																																																																																																																																																					
def opsiClient(jenis_kartu_anda, jenis_1, jenis_2) :
	opsi = input("Silahkan pilih keperluan anda : ")
	if opsi == "1" :
		transfer_uang(jenis_kartu_anda, jenis_1, jenis_2)
		print('\nSisa saldo kartu anda : Rp  ', jenis_kartu_anda["jumlah"])
	elif opsi == "2" :
		tarik_tunai(jenis_kartu_anda)
		print('\nSisa saldo kartu anda : Rp  ', jenis_kartu_anda["jumlah"])

	