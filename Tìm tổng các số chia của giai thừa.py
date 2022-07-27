'''
Tìm tổng các số chia của giai thừa
Cho một số, hãy tìm tổng số các ước số của giai thừa của số đó. Vì đáp án có thể rất lớn, hãy in ra là modulo 109+7.

Định dạng đầu vào
Dòng đầu tiên chứa T, số lượng trường hợp thử nghiệm.
T dòng sau, mỗi dòng chứa số N.
Điều kiện
1≤T≤500
0≤N≤50000
Định dạng đầu ra
In ra T dòng của kết quả đầu ra, mỗi dòng chứa 1 đáp án.

Ví dụ
Đầu vào

3
2
3
4
Đầu ra

2
4
8 

Tham khảo video sau để hiểu hơn:
https://www.youtube.com/watch?v=RS-TblI0uL8

'''

def degree(n,p):
    ans=0
    i=p
    while i<=n:
        ans +=n//i
        i*=p;
    return ans
    
    
def is_prime(n):
    if n<=3:
        if n>1: return 1
        else: return 0
    if n%2 == 0 or n%3 == 0:
        return 0
    i=5
    while i*i<=n:
        if n%i ==0 or n%(i+2)==0:
            return 0
        i+=6
    return 1
    
    
def solution(n):
    res=1
    for i in range(2,n+1):
        if is_prime(i)==1:
            res=(res*(degree(n,i)+1))%1000000007
    return res
 
 
t=int(input())
while t>0:
    a=int(input())
    print(solution(a))
    t=t-1