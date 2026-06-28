def a000(i):
    pass
def a010(i):
    x[i]=1
def a110(i):
    x[i]=0
    x[i+1]=1
def a011(i):
    x[i]=0
    x[i+1]=1
def a111(i):
    x[i]=1
    x[i+1]=1

def main():
    global x
    a1=int(input('请输入第一个数字：'))
    a2=int(input('请输入第二个数字：'))
    b=[int(k) for k in str(bin(a1)[2:])]#转换为二进制再转为列表
    c=[int(k) for k in str(bin(a2)[2:])]
    max_len=max(len(b),len(c))
    b=[0]*(max_len-len(b))+b#列表长度对齐
    c=[0]*(max_len-len(c))+c
    x=[0]*(max_len+1)
    b.reverse()#列表翻转
    c.reverse()
    print(b)
    print(c)
    for i in range(len(b)):
        match b[i],c[i]:
            case 0,0:
                a000(i)

            case 1,0 if x[i]==0:
                a010(i)
            case 1,0 if x[i]==1:
                a110(i)

            case 0,1 if x[i]==0:
                a010(i)
            case 0,1 if x[i]==1:
                a110(i)

            case 1,1 if x[i]==0:
                a011(i)
            case 1,1 if x[i]==1:
                a111(i)
    print(x)
    x.reverse()
    print(x)
    qw=int(''.join(map(str,x)),2)

    print(qw)
if __name__ == '__main__':
    main()

