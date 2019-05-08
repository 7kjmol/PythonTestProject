import re
print(re.match('www', 'www.baidu.com').span())
print(re.search('com$', 'www.baidu.com'))

print(re.sub('www', 'w', 'www.baidu.com'))
print(re.sub('com', 'cn', 'www.baidu.com'))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : %s" % matchObj.group())
    print("matchObj.group(1) : %s" % matchObj.group(1))
    print("matchObj.group(2) : %s" % matchObj.group(2))
    print("matchObj.group(0) : %s" % matchObj.group(0))
else:
    print("No Match!")

