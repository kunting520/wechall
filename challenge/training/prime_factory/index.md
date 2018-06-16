## Welcome to wechall writeup Pages


```markdown
write up for Prime Factory (Training, Math)

# visit http://www.wechall.net/challenge/training/prime_factory/index.php
# and knowing the challenge is about url decode
# the poor code of python3 as follow:
`
#!/usr/bin/env python3
#author: Lenka

import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True 

def get_sum(num):
    total=0
    while num:
        total+=num%10
        num//=10
    return total

if __name__ == '__main__':
    j = 0
    for i in range(1000000,10000000):
        if is_prime(i) and is_prime(get_sum(i)):
            print(i)
            j = j + 1
            if j > 1 :
                break
`

# you will get the two big numbers 1000033 and 1000037
# input 10000331000037 will pass this challenge

```

