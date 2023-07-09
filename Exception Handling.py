#===========================  System Defined Exception ==============================================
# 1.Developer Time Exception
'''
a=10
b=20:
c=a+b
print(c)
'''
#2.Runtime Exception
'''
a=10
b=0
try:
    c =a/b
    print(c)
except:
    print('Error Raised')
'''
# ----- or ----
'''
a=20
b = 5
try:
    import math1
    x = math.sqrt(-25)
    print(x)
except NameError:              # undefind name
    print('name only')
except TypeError:                # 'n'
    print('type only')
except ValueError:               #  takes only  ( import ) modules
    print('value only')
except ZeroDivisionError:   # b=0
    print('Zero only')
except:                                         #
    print('Error Raised')
'''
#   else block      finally block
'''
a=10
b=3
try:
    c=a/lucky
    print(c)
except:
    print('error raised')
else:
    print('Try executed')
finally:
          print('Thank you')
'''
#===================================  User Defined Exception  =================================================
'''
class lessthenzeroerror(Exception):
    pass
class morethenzeroerror(Exception):
    pass
marks= eval(input('enter your marks: '))

if marks >= 0 and marks <= 34:
    print('Failed')
elif marks >= 35 and marks <= 100:
    print('pass')
elif marks < 0:
    raise lessthenzeroerror('you have less then maks')
else:
    raise morethenzeroerror('you have more then maks')
'''




