#Extractor de rangos IP
import sys, os.path, urllib, urllib2, re, time, socket, random, socket, json

file = open('ip_data_mx.txt', 'r+')
linea=file.readline()
file148 = open('xxx.txt', 'r+')


while linea != '':
	
 # procesar linea
 ip = linea
 parts = ip.partition(".")

 if (parts[0] == '148'):
	print 'Writting : '+ip
	file148.write(ip)
	

 linea=file.readline()

file148.close()		
file.close()
#77

