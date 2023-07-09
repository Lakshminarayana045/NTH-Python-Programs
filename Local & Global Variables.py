#====================================     Local Variable        ===================================
'''
def displays():
    a = 10
    b = 20
    c = a+b
    print(c)        # 30
displays()

#print(c)           # NameError
'''
#====================================        Global Variable    ========================================================
'''
a=10
print(a)                # 10

def dis():
    global a
    a = a+5
    print(a)            # 15
dis()

def d2():
    print(a)            # 15
d2

def d3():
    print(a)            #15
d3()

print(a)                # 15
'''
# ====================================      NonLocal Variable   ==========================================================
'''
def outer():
    a=10
    def inner():
        nonlocal a
        a = a+10
        print(a)            # 20
    inner()
    print(a)                # 20
outer()
'''
# ====================================      Return Keyword      ==========================================================
'''
def dis():
    a=10
    b=20
    c=a+b
    print(c)                # 30
    return c
x = dis()

print(x)                    # 30

print(x)                    # 30

'''
