

a=12345
c=12345
print(a+c)


def free(a,b):
    a=a*123
    b=b/2
    return a,b

x=100
z=100
free(x,z)
print(x,z)


x=(1,2,3,4,5)
s=0
for i in x:
    s=i*i
    print(s)
