def bs(a,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def ip():
    for i in range(0,n):
        print("%d" % a[i], end=" ")
a=[5,4,6,3,0]
n=5
bs(a,n)
ip()