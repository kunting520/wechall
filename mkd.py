#python3
#coding=utf-8
import re
import os

num = 0
with open("index.md", "r") as f:
	for line in f:
		if 'unsolved' in line or "\n" == line:
			continue
		#print line
		matchobj = re.search(r'https://kunting520.github.io/wechall/(.*)\)', line)
		if matchobj:
			md = '/Users/kunkun/Desktop/github/wechall/' + matchobj.group(1) + '/index.md'
			print md
			os.system("touch " + md)