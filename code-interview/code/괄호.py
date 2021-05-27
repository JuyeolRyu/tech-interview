'''
[괄호]
() 괄호의 쌍이 제대로 되어있으면 YES 아니면 NO를 출력하기
'''
import sys
input = sys.stdin.readline
ans = []
for t in range(int(input())):
  stack = []
  for i in input().rstrip():
    if stack:
      if stack[-1] == '(' and i == ')':
        stack.pop(-1)
        continue
    stack.append(i)
  if stack:
    ans.append('NO')
  else:
    ans.append('YES')
for a in ans:
  print(a)