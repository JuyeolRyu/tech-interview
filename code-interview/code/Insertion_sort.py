arr=[2,3,1,4,6,5]
n=len(arr)

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        else:
            break

'''
시간복잡도: O(n^2) ==> 최선의 경우 O(n)이 나올수 있다.
배열을 정렬된 부분배열과 그렇지 않은 부분배열로 나누어서 문제를 해결한다.
정렬되지 않은 배열은 인덱스 1부터 탐색한다.
만약 현재 인덱스의 값이 바로 앞의 인덱스의 값보다 작을 경우 swap한다.
'''
