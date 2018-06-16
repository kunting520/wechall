## Welcome to wechall writeup Pages


```markdown
write up for Encodings: URL (Training, Encoding)

# visit http://www.wechall.net/challenge/training/encodings/url/index.php
# and knowing the challenge is about url decode
# the poor code of python3 as follow:
`
#!/usr/bin/env python3
#author: Lenka

from urllib import parse

def urldecode(urlen):
	return(parse.unquote(urlen))

if __name__ == '__main__':
	urlen='%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%63%64%70%62%6C%6C%67%62%65%69%64%61%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21'
	print(urldecode(urlen))
`

# you will get the decode content
Yippeh! Your URL is challenge/training/encodings/url/saw_lotion.php?p=cdpbllgbeida&cid=52#password=fibre_optics Very well done!

try to visit this url and will pass the challenge

```

