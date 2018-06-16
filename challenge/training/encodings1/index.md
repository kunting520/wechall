## Welcome to wechall writeup Pages


```markdown
write up for Training: Encodings I (Training, Encoding)

# visit https://www.wechall.net/challenge/training/encodings1/index.php
# challenge note: The message is most likely in english
# so it may be bin of ascii 
# the poor code of python3 as follow:
`
#!/usr/bin/env python3
#author: Lenka

def decoding(code):
	l = len(b)
	msg = ''
	for i in range(0, l, 7):
		a = b[i:i+7]
		c = int(a,2)
		#print(c)
		msg += chr(int(a,2))
	return msg

if __name__ == '__main__':
	b = """101010011010001101001111001101000001110100110010111110001110100010000011010011110011010000001101110101101110001011010011110100010000011001011101110110001111011111100100110010111001000100000110000111100111100011110100111010010101110010000010110011101111111010111100100100000111000011000011110011111001111101111101111111001011001000100000110100111100110100000110010111000011110011111100111100111110100110000111100101110100110010111100100101110"""
	print(decoding(b))
`

# you will get the solution
This text is 7-bit encoded ascii. Your password is easystarter.

```

