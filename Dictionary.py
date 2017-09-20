# Declaring a dictionary in python
# d = dict() or d = {}

d = dict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5
d['f'] = 6
print"printing the dict"
print d
print "printing keys"
print d.keys()
print"printing values"
print d.values()
del d['a']
print d
d = {'a': 1, 'b':  2,  'c': 3}
print d
print "check whether c exist in dictionary "
print ('c' in d)
print"length of dictonary is :",  len(d)
print "converting dictionary to string "
str1 = str(d)
print(str1[0:5:])
print "copy function"
d2 =[]
d2 =d.copy()
print"d :",d
print "d2 after copying d1 is ", d2
print "clear d1",d.clear()
print "check d1",d

# updtae function in dictionary
d1= {'Name':'Hunter','Age':20}
print d1
d2 ={'RollNo':101}
d1.update(d2)
# print(d1)

print "updated student data\n",d1


# Get Function get(arg,def_val)
print d.get('Branch','Not Present')
print  d1.get('RollNo',"Not Present")
print(d1)
"""setdefault func set the default veal for the keys"""
print d1.setdefault('Branch','Not Present')
print d1.setdefault('RollNo','Not Present')
"""this will insert the default values  """
print d1