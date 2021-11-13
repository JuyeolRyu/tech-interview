def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=len(arr)//2
    left,right=[],[]
    for idx,num in enumerate(arr):
        if idx==pivot:
            continue
        if num<arr[pivot]:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left)+[arr[pivot]]+quick_sort(right)

arr=[2,3,1,4,6,5]
quick_sort(arr)
'''
시간복잡도: O(nlog2n)
배열을 분할,정복의 과정을 통해 정렬하는 방법입니다.
배열 중간 인덱스를 pivot으로 정하고 arr[pivot]보다 작은 값은 left 큰 값은 right 배열에 삽입합니다.
위의 과정을 배열의 길이가 1이하가 될때까지 분할합니다.
다시 배열을 병합하면 정렬된 배열을 얻을수 있습니다.
'''
