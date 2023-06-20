import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		
		;       S P A M  S M S      ;
		
		;   Author : TOKUPENSSS COY ;   
	

PENTING CUYY! TOOL INI WORK UNTUK WARGA INDO YGY

1. SMS Gratis
2. OTP hengker epep
3. OTP hengker emel
4. OTP hengker pubege
5. OTP hengker ceoce
""")
		pilih=int(input('noobie/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.hengker epep
		elif pilih == 3:
			import src.hengker emel
		elif pilih == 4:
			import src.hengker pubege
		elif pilih == 5:
			import src.hengker ceoce
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
