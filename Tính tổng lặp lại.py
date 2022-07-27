'''
Tính tổng lặp lại
Hãy tính tổng bình phương của các số đã cho: a, a + 1, ..., b-1, b.

Định dạng đầu vào
Hai số: a và b cách nhau một khoảng trắng, trong đó 1≤a≤b≤100.

Định dạng đầu ra
Tính tổng: a*a + (a+1)*(a+1) + ... + (b-1)*(b-1) + b*b

Ví dụ 1
Đầu vào

1 4
Đầu ra

30
Ví dụ 2
Đầu vào

5 6
Đầu ra

61
'''
a1,b1=input().split()
a=int(a1)
b=int(b1)
print(b*(b+1)*(2*b+1)//6 - a*(a-1)*(2*a-1)//6)