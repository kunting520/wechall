## Welcome to wechall writeup Pages


```markdown
write up for PHP 0817 (PHP, Exploit)

# visit http://www.wechall.net/challenge/php0817/index.php
# it seems to be vulnerable to LFI.
# the following code is vulnerability:

`
<?php
if (isset($_GET['which']))
{
        $which = $_GET['which'];
        switch ($which)
        {
        case 0:
        case 1:
        case 2:
                require_once $which.'.php';
                break;
        default:
                echo GWF_HTML::error('PHP-0817', 'Hacker NoNoNo!', false);
                break;
        }
}
?>
`

#this challenge has used two features of PHP language
1.string will be transformed to int while compared with int 
2.it will run the case code untill break in switch case expression

#so get the page
https://www.wechall.net/challenge/php0817/index.php?which=solution

# you will pass the challenge

```

