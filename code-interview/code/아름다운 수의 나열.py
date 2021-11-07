#양옆의 수의 합이 제곱이 되도록 정렬
arr=[i for i in range(1,33)]
possible_num=set()
ans=[]
i=2
while i**2<arr[-1]+arr[-2]:
    possible_num.add(i**2)
    i+=1

def find(a):
    global ans
    if len(a)==31:
        for i in range(1,33):
            if i not in a and a[-1]+i in possible_num and a[0]+i in possible_num:
                ans=a+[i]
                return
    for i in range(1,33):
        if i not in a and a[-1]+i in possible_num:
            find(a+[i])

    return
find([1])
print(ans)