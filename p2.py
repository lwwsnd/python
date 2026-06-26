'''
a,b=0,1
while b<100:
    print(b,end=' ')
    a,b=b,a+b
'''

n=10
a,b=0,1
for i in range(n):
    print(b,end=' ')
    a,b=b,a+b
