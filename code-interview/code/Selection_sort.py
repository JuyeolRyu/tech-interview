arr=[]
n=len(arr)
for i in range(n-1):
  min_idx=i
  for j in range(i+1,n):
    if arr[j]<arr[min_idx]:
      min_idx=j
  arr[i],arr[min_idx]=arr[min_idx],arr[i]
 
'''
시간복잡도: O(n^2)
배열을 돌면서 최솟값을 찾으면 주어진 배열의 가장 앞으로 보내는 정렬방법
'''
