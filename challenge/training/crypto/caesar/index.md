## Welcome to wechall writeup Pages


```markdown
write up for Training: Crypto - Caesar I (Crypto, Training)

# visit http://www.wechall.net/challenge/training/crypto/caesar/index.php
# and knowing the challenge is about Caesar decode
# the poor code of python3 as follow:
`
#python3

def caesardecode(caesar):
	msg = ''
	for i in range(1,26):
		for a in caesar:
			if a == ' ':
				msg += ' '
				#print(a,end='')
				continue
			k = ord(a) + i
			if k > 90:
				k = k - 26
			msg += chr(k)
			#print(chr(k),end='')
		msg += "\n"
	return msg

if __name__ == '__main__':
	caesar = 'BPM YCQKS JZWEV NWF RCUXA WDMZ BPM TIHG LWO WN KIMAIZ IVL GWCZ CVQYCM AWTCBQWV QA NKXWZVIUPQXM'
	print(caesardecode(caesar))
`

# you will get the solution

THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG OF CAESAR AND YOUR UNIQUE SOLUTION IS FCPORNAMHIPE

```

