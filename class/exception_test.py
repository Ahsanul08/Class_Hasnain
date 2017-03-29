#a---  syntaxError

#a + 1  nameError

#int('a') ValueError

#a= {'a':1};a['b'] KeyError

#a=[1,2];a.add(2) AttributeError

#a=[1,2];a[2] IndexError

#1/0 ZeroDivisionError


#a = [1,2,3,4]
#a = iter(a)

#print a
'''
print(next(a))

print(next(a))

print(next(a))

print(next(a))
'''


#__init__()

#__new__()


#__str__():




try:
    a = int(raw_input())
except ValueError as e:
    print e
else:
    print 'Inside else'
