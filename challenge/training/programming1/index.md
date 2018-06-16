## Welcome to wechall writeup Pages


```markdown
write up for Training: Programming 1 (Training, Coding)

# visit https://www.wechall.net/challenge/training/programming1/index.php
# knowing the challenge is about geting url text and put it back to the same url
# programming1 with python3 selenium or python3 requests
# the poor code of python3 as follow:
`
#!/usr/bin/env python3
#author: Lenka

from selenium import webdriver
import time

def programming1(user, passwd):
	browser = webdriver.Chrome()
	browser.get('https://www.wechall.net/')
	browser.find_element_by_name('username').send_keys(user)
	browser.find_element_by_name('password').send_keys(passwd)
	browser.find_element_by_name('bind_ip').click()
	browser.find_element_by_name('login').click()

	browser.get('https://www.wechall.net/challenge/training/programming1/index.php?action=request')
	p=browser.find_element_by_tag_name('body').text
	browser.get('https://www.wechall.net/challenge/training/programming1/index.php?answer='+p)
	
	browser.quit()

if __name__ == '__main__':
	user = 'username'
	passwd = 'password'
	programming1(user, passwd)
`

# you will pass this challenge

```

