import re, csv

# num = '123123123,423123'
# pat = re.compile(r'[abcd]+')
# # pat2 = re.compile(r',')
# m = pat.search('bad')
# print(m)
# str1 = pat2.sub('', num)
# str2 = pat2.split(num)
# print(str1)

# str3 = 'Monica : asdfasdfaslkclksdlkfdklsdlkfj \nJoey : sakldfjlasdf \nMonica : slkjcv \nPheobe : slkcjxvlksd'
# pat3 = re.compile(r'(Monica :.+)')
# m2 = pat3.finditer(str3)
# for i in m2:
#     print(i.group())

# f = open('a.txt', 'w')
# f.write(str3)
# f.close()
#
# f = open('a.txt', 'r')
# m = f.read()
# print(m)
# listdata = []
# f = open('new.csv', 'w')
# a = csv.writer(f)
# a.writerows(listdata)
# f.close()

str1 = 'iPhone5 or iPhone3'
str1 = re.findall('[a-z5]+', str1)
print(str1)
