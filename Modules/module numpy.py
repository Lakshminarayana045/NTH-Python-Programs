from numpy import *

#================================  Creating 0-D array  ===========================================================================
'''
a = array(10)
print(a)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.shape)
'''
#================================   Creating 1-D array   ===========================================================================

'''
# Create
a = array([10,20,30,40,50,60])

print(a)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.shape)

print(a.reshape(1,6))
print(a.reshape(6,1))


print(a.max())
print(a.min())
print(a.sum())


# indexing

print(a[1])
print(a[5])

# Slicing

print(a[1:4])
print(a[-1::-1])
print(a[4::-1])

# loop
for i in a:
    print(i)
'''    
#================================   Creating 2-D array   ===========================================================================

'''
# Create
a = array( [[10,20,30],[40,50,60]])

print(a)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.shape)

print(a.reshape(1,6))
print(a.reshape(6,1))
print(a.reshape(3,2))
print(a.reshape(2,3))


print(a.max())
print(a.min())
print(a.sum())
print(a.max(axis=0))
print(a.min(axis=1))
print(a.sum(axis=0))


# indexing

print(a[1])
print(a[1][0])
print(a[1][1])
print(a[1][2])

print(a[0])
print(a[0][0])
print(a[0][1])
print(a[0][2])

# Slicing

print(a[1][1:3])
print(a[0][1:2])
print(a[1][-1::-1])
print(a[0][-1::-1])

# loop
for i in a:
    for j in i:
        print(j)
'''

#================================   Creating 3-D array   ===========================================================================

'''
# Create
a = array([ [[10,20,30],[40,50,60]],[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]] ])

print(a)
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.shape)

print(a.reshape(9,2))
print(a.reshape(6,3))
print(a.reshape(1,18))


print(a.max())
print(a.min())
print(a.sum())
print(a.max(axis=0))
print(a.min(axis=1))
print(a.sum(axis=0))


# indexing

print(a[0])
print(a[0][0])
print(a[0][0][1])
print(a[0][1])
print(a[0][1][0])

print(a[1])
print(a[1][0])
print(a[1][0][2])
print(a[1][1])
print(a[1][1][1])


print(a[2])
print(a[2][0])
print(a[2][0][0])
print(a[2][1])
print(a[2][1][1])


# Slicing

print(a[1][-1::-1])
print(a[1][1:3])
print(a[0][1:2])
print(a[1][-1::-1])
print(a[0][-1::-1])


# loop
for i in a:
    for j in i:
        for k in j:
            print(k)
        
'''
