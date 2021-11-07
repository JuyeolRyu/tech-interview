#누적합
arr=[1,2,3,4,5,6,7]
command=[[0,6],[2,5],[5,6],[0,6],[1,3]]
sum_arr=[0,arr[0]]
for i in range(1,len(arr)):
    sum_arr.append(sum_arr[-1]+arr[i])

print(sum_arr)
for idx1,idx2 in command:
    print(sum_arr[idx2+1]-sum_arr[idx1])