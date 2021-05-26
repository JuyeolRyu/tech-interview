'''
N*N배열 90,180,270도 회전(시계방향,반시계방향)
'''
def print_arr(arr):
  for r in arr:
    print(r)
  print("=========")
def rotate90(arr):
  row,col = len(arr),len(arr[0])
  answer = [[0]*row for _ in range(col)]
  for r in range(row):
    for c in range(col):
      answer[c][row-1-r] = arr[r][c]
  return answer
def rotate180(arr):
  row,col = len(arr),len(arr[0])
  answer = [[0]*row for _ in range(col)]
  for r in range(row):
    for c in range(col):
      answer[row-1-r][col-1-c] = arr[r][c]
  return answer
def rotate270(arr):
  row,col = len(arr),len(arr[0])
  answer = [[0]*row for _ in range(col)]
  for r in range(row):
    for c in range(col):
      answer[row-1-c][r] = arr[r][c]
  return answer
  
arr = [[1,2,3],[4,5,6],[7,8,9]]
print_arr(arr)
print_arr(rotate90(arr))
print_arr(rotate180(arr))
print_arr(rotate270(arr))