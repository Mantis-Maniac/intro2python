import re

pattern = re.compile(r'.*')
m = pattern.match('a123cbdweifhipweiu')
print m
print m.group()


word_pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)

m = word_pattern.match('hello world haha hehe')
print m.group()


phone_number = re.compile(r'\d{10}')

m = phone_number.search('my phone number is 4158271196, his phone number is 4158769351')
print m.group()
n = phone_number.findall('my phone number is 4158271196, his phone number is 4158769351')
print n

qq_pattern = re.compile(r'[1-9][0-9]{4,}') 


#email_pattern = re.compile(r'[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?')
email_pattern = re.compile(r'\w+@\w+\.\w{2,3}')


e = email_pattern.findall("silversnyder360@gmail.com ---@--.com")
print e



ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')

i = ip_pattern.findall("127.0.0.1   8.8.8.8  a.b.c.d   114.114.1.114")
print i

id_pattern = re.compile(r'\d{6}[1,2][8,9,0]\d{10}')
ID = id_pattern.findall("686868686868686868")
print ID
