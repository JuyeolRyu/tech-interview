def merge(left_arr,right_arr):
    l,r=0,0
    arr=[]
    while l<len(left_arr) and r<len(right_arr):
        if left_arr[l]<right_arr[r]:
            arr.append(left_arr[l])
            l+=1
        else:
            arr.append(right_arr[r])
            r+=1
    
    while l<len(left_arr):
        arr.append(left_arr[l])
        l+=1
    while r<len(right_arr):
        arr.append(right_arr[r])
        r+=1

    return arr
def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left_arr=merge_sort(arr[:mid])
    right_arr=merge_sort(arr[mid:])

    return merge(left_arr,right_arr)
arr=[2,3,1,4,6,5]
merge_sort(arr)
'''
시간복잡도: O(nlog2n)
배열을 분할,정복,결합의 과정을 통해 정렬하는 방법입니다.
우선 배열의 길이가 1이 될때까지 분할합니다.
그리고 다시 병합할때 두 배열을 반복문을 돌면서 순서대로 병합합니다.
위의 병합과정을 거치면 정렬된 배열을 얻을수 있습니다.
'''
