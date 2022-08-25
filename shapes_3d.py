from math import ceil,floor

f = lambda n: [[" "*(2*n-i-1),*("/"+"  "*(i%2)+"\\"," "*(~i%2*2))*(i//2+1)]for i in range(2*n)]+[[" "*i,*("\\"+"  "*(~i%2)+"/"," "*(i%2*2))*(n-i//2)]for i in range(2*n)]

g = lambda s,n: iter([s[[i*n,-i-1][j]-k*n+k]for i,j in [(i,0)for i in range(n)]+[(i,1)for i in range(n-2,-1,-1)]for k in range(i+1)])

def getCube(n):
    a,b = getWalls(n)
    x,k = ceil(n**(1/3)),0
    s = f(x)
    for i in range(x):
        for j in range(i+1):
            p = next(a)
            s[k][j*2+1],s[k+1][j*2+1] = "/%%%%"*p+s[k][j*2+1],"/%%%%"*p+s[k+1][j*2+1]
            if i!=x-1:
                q = next(b)
                s[k+2][j*2+1],s[k+3][j*2+1] = s[k+2][j*2+1]+"::::\\"*q,s[k+3][j*2+1]+"::::\\"*q
        k += 2

    for i in range(x-1,-1,-1):
        for j in range(i+1):
            if i!=x-1:
                p = next(a)
                s[k-2][j*2+1],s[k-1][j*2+1] = s[k-2][j*2+1]+"%%%%/"*p,s[k-1][j*2+1]+"%%%%/"*p
            q = next(b)
            s[k][j*2+1],s[k+1][j*2+1] = "\::::"*q+s[k][j*2+1],"\::::"*q+s[k+1][j*2+1]
        k += 2

    return s


def getWalls(n):
    x,y,z = floor(n**(1/3)),ceil(n**(1/3)),int(n**(1/3))
    if z**3 == n: x = y = z
    elif (z+1)**3 == n: x = y = z+1

    s,t = [*([0]*(y-x)+[x]+[0]*(x-1))*(x),*([0]*(y-x)*y)],[*([0]*(y))*(x-1),*([0]*(y-x)+[x]*(x)),*([0]*(y-x)*y)]
    n -= x**3
    if n == 0: return g(s,y),g(t,y)

    for i in range(x):
        for j in range(i):
            s[j*y],s[j*y+1],t[j*y] = s[j*y]+1,s[j*y+1]-1,t[j*y]+1
            if j: t[j*y-y] = t[j*y-y]-1
            n -= 1
            if n == 0: return g(s,y),g(t,y)

        for j in range(i+1):
            s[i*y],s[i*y+1],t[i*y] = s[i*y]+1,s[i*y+1]-1,t[i*y]+1
            if i: t[i*y-y] = t[i*y-y]-1
            n -= 1
            if n == 0: return g(s,y),g(t,y)

    for i in range(x):
        for j in range(i):
            s[-j-1],t[-j-1],t[-j-y-1] = s[-j-1]+1,t[-j-1]+1,t[-j-y-1]-1
            if j: s[-j] = s[-j]-1
            n -= 1
            if n == 0: return g(s,y),g(t,y)

        for j in range(i+1):
            s[-i-1],t[-i-1],t[-i-y-1] = s[-i-1]+1,t[-i-1]+1,t[-i-y-1]-1
            if i: s[-i] = s[-i]-1
            n -= 1
            if n == 0: return g(s,y),g(t,y)

    for i in range(x):
        s[-y],s[-y+1],t[-y],t[-2*y] = s[-y]+1,s[-y+1]-1,t[-y]+1,t[-2*y]-1
        n -= 1
        if n == 0: return g(s,y),g(t,y)

    for i in range(x):
        for j in range(1,i+1):
            s[j*y-i-1],s[j*y-i],t[j*y-i-1] = s[j*y-i-1]+1,s[j*y-i]-1,t[j*y-i-1]+1
            if j>1: t[j*y-i-y-1] = t[j*y-i-y-1]-1
            n -= 1
            if n == 0: return g(s,y),g(t,y)

        for j in range(1,i+2):
            s[i*y+y-j],t[i*y+y-j] = s[i*y+y-j]+1,t[i*y+y-j]+1
            if j>1: s[i*y+y-j+1] = s[i*y+y-j+1]-1
            if i: t[i*y-j] = t[i*y-j]-1
            n -= 1
            if n == 0: return g(s,y),g(t,y)

    for i in range(x):
        s[i*y],s[i*y+1],t[i*y] = s[i*y]+1,s[i*y+1]-1,t[i*y]+1
        if i: t[i*y-y] = t[i*y-y]-1
        n -= 1
        if n == 0: return g(s,y),g(t,y)

    for i in range(1,x+1):
        s[-i],t[-i],t[-i-y] = s[-i]+1,t[-i]+1,t[-i-y]-1
        if i>1: s[-i+1] = s[-i+1]-1
        n -= 1
        if n == 0: return g(s,y),g(t,y)

    return g(s,y),g(t,y)


[print(f"N = {i}",*["".join(k for k in j)for j in getCube(i)],sep="\n",end="\n"*3)for i in range(1,18)]
