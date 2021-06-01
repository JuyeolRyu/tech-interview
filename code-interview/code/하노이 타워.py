'''
하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729
'''
n = int(input())
ans = ''
def hanoi(n,f,b,t):
  if n == 1:
    print(f,t)
  else:
    hanoi(n-1,f,t,b)
    print(f,t)
    hanoi(n-1,b,f,t)
print(2**n-1)
hanoi(n,1,2,3)