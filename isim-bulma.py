#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Türkçe karakter sorununu çözene kadar")
print("ö için ö., ş için ş. yazın")
array = []
array.append("aby"); #0
array.append("def"); #1
array.append("öçi"); #2


def rakamAl(harf):
		for i in range(0,2):
			if harf in array[i]:
				soz=array[i].index(harf)
				#print("var")
				print(i)
			else:
				print(-1)
			
var=input("dasdad: \n");
#harf=str(var);
rakamAl(str(var));


print(array[2])
