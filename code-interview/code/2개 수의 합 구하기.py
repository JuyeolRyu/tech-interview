#2개 수의 합 구하기
#sol1 combinations(O(n^2))

from itertools import combinations
def solution(arr,target):
    for i in combinations(arr,2):
        print(sum(i))
        if sum(i)==target:
            return [arr.index(i[0]),arr.index(i[1])]
    return 0

#sol2 이진 탐색(O(nlogn))

def solution(arr,target):
    sorted_arr=[]
    for i,n in enumerate(arr):
        sorted_arr.append([n,i])
    sorted_arr.sort()
    l,r=0,len(arr)-1
    while l<r:
        n=sorted_arr[l][0]+sorted_arr[r][0]
        if n==target:
            return [sorted_arr[l][1],sorted_arr[r][1]]
        if n>target:
            r-=1
        else:
            l+=1

#sol3 딕셔너리(O(n)))
from collections import defaultdict
def solution(arr,target):
    dic=defaultdict(list)
    for i,n in enumerate(arr):
        dic[n]=[target-n,i]

    for n in dic:
        if dic[n][0] in dic:
            return[dic[n][1],dic[dic[n][0]][1]]

    return 0
print(solution([10,3,5,7],13))
