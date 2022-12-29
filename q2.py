import re
string = input("enter your txt:")
words = re.findall('[A-Z][a-z]*', string)
print(' '.join((words)))
