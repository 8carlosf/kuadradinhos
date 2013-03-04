#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#by carlosf

import Image, os

ACC=250

def listaD(a):
	l=[a]
	k=0
	while(k<len(l)):
		l+=[l[k]+'/'+i for i in os.listdir(l[k]) if os.path.isdir(l[k]+'/'+i)]
		k+=1
	return l

def listaF(l):
	return [os.path.abspath(d+'/'+i)  for d in l for i in os.listdir(d) if os.path.isfile(d+'/'+i)]

def carregar(a):
	return Image.open(a).convert('L')

def tolist(im):
	b=list(im.getdata())
	return [b[i*im.size[0]:(i+1)*im.size[0]] for i in range(im.size[1])]

def delinha(m):
	return [i for i in m if sum(i)<ACC*len(m[0])]

def roda90(m):
	return map(list,zip(*m[::-1]))

def delcoluna(m):
	return roda90(roda90(roda90(delinha(roda90(m)))))

def toimg(m):
	im=Image.new("L",(len(m[0]),len(m)))
	im.putdata([i for y in m for i in y])
	return im.convert("L")

def newsize(im):
	if im.size[0]<=im.size[1]:
		return 600,int(600.0*im.size[1]/im.size[0]+.5)
	return int(800.0*im.size[0]/im.size[1]+.5),800

def resize(im):
	return im.resize(newsize(im),3)

def alterar(n):
	try:
		resize(toimg(delcoluna(delinha(tolist(carregar(n)))))).save(n)
		print "   "+n+": DONE!"
	except:
		print "   "+n+": This file is not a Image!"

if __name__=='__main__':
	a=raw_input('Main directory or image file: ')
	if (os.path.isdir(a)):
		f=listaF(listaD(a))
		k=0
		for i in f:
			k+=1
			print k,'/',len(f),': '+i
			if(os.path.isfile(i)):
				alterar(i)
	elif(os.path.isfile(a)):
		print '1/1: '+a
		alterar(a)
	else:
		print a+": No such file or directory\n"
	
	#while(True):
	#	try:
	#		a=raw_input()
	#	except (EOFError):
	#			break;
	#	alterar(a)	
