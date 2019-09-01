#python3
"""
mau ngapain stah, recode?
silahkan tapi izin dulu ke ane :v
kontak : 081230754052
"""
import os,time,sys
try:
	import requests
except ModuleNotFoundError:
	print("anda belu menginstal pip install requests")
	exit()
	
banner = """
╔══╗╔═╗╔══╗╔═╦═╗╔══╗╔═╦═╗╔══╗ Author : Ibar052
║══╣║╬║║╔╗║║║║║║║══╣║║║║║║══╣ Code   : Python3
╠══║║╔╝║╠╣║║║║║║╠══║║║║║║╠══║ Team   : 407 Authentic Exploit
╚══╝╚╝─╚╝╚╝╚╩═╩╝╚══╝╚╩═╩╝╚══╝
"""
os.system("clear")
print(banner)
def main():
    nomer = input("Masukkan Nomer(Gunakan 628xxxxxxx) : ")
    req = requests.post("https://api.grab.com/grabid/v1/phone/otp",data={"method":"msg","countryCode":"id","phoneNumber":nomer,"templateID":"pax_android_production"}).text
    if 'error' in req:
	    print("[x] GAGAL ->",nomer)
	    keluar()
    else:
	    print("[√] SUKSES ->",nomer)
	    keluar()
	    
def keluar():
    asw = input("ingin melanjutkan [Y/T] -> ")
    if asw == 't' or asw == 'T':
       os.syetem("clear")
       exit()
    else:
       if asw == 'y' or asw =='Y':
          os.system("clear")
          print(banner)
          main()
	    
if __name__ == '__main__':
      main()