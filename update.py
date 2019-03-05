#!/bin/env python2
#XignCode = "Jinxpro.id"
#
import urllib2
import os

ver = open("version.txt", "r")
version = ver.read()
ver.close()

up = urllib2.urlopen("https://raw.githubusercontent.com/diahadi/explorer/master/version.txt").read()
if version != up:
	print ""
	print "[+] Pembaruan Tersedia"
	print ""
	x = raw_input("Apakah kamu ingin Update ? y/n: ")
	if x == "y":
		os.remove("jinxpro.py")
		diahadi = "https://raw.githubusercontent.com/diahadi/explorer/master/jinxpro.py"
		update = urllib2.urlopen(diahadi).read()
		
		jinxpro = open("jinxpro.py", "w")
		jinxpro.write(update)
		jinxpro.close()

		os.remove("version.txt")
		ver = open("version.txt", "w")
		ver.write(up)
else:
	print ""
	print "[-] Tidak ada pembaruan"
	print ""
