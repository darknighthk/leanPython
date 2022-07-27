'''Cho một số nguyên n, nhiệm vụ của bạn là tính các tổng sau:

Tổng S của n số nguyên đầu tiên (bắt đầu từ 1)
Tổng Seven  của n số nguyên chẵn (bắt đầu từ 2)
Tổng Sodd của n số nguyên lẻ đầu tiên (bắt đầu từ 1)
Tổng Ssquares của n giá trị bình phương của số nguyên đầu tiên (1, 4, 9, ...)
Tổng Scubes của n giá trị mũ 3 của số nguyên đầu tiên (1, 8, 27, ...)
Định dạng đầu vào
Dòng đầu tiên của đầu vào chứa một số nguyên T biểu thị số lượng trường hợp thử nghiệm. Tiếp theo là mô tả của T các trường hợp thử nghiệm. Mỗi trường hợp thử nghiệm được mô tả trong một dòng duy nhất chứa số nguyên «n» (1 ≤ n ≤ 104).

Định dạng đầu ra
Đối với mỗi trường hợp thử nghiệm, hãy in ra một dòng duy nhất chứa 5 số nguyên được phân tách bằng dấu cách: S Seven Sodd Ssquares Scubes

Ví dụ
Đầu vào

3
4
5
6
Đầu ra

10 20 16 30 100
15 30 25 55 225
21 42 36 91 441

Tìm các công thức tính t1,2,3,4,5 trên google 1 cách dễ dàng
'''
def solution(n):
    t1= (n+1)*n//2
    t2= (n+1)*n
    t3= n*n
    t4= n*(n+1)*(2*n+1)//6
    t5= (n*n)*(n+1)*(n+1)//4
    print(t1,t2,t3,t4,t5)
 
t=int(input())
while t>0:
    a=int(input())
    solution(a)
    t=t-1