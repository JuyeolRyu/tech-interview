'''
팩토리얼 0의 개수
https://www.acmicpc.net/status?user_id=back2225&problem_id=1676&from_mine=1
'''
import sys
input = sys.stdin.readline
n = int(input())

#sol1
num = 1
ans = 0
for i in range(1,n+1):
  num *= i

for c in list(reversed(str(num))):
  if c == '0':
    ans +=1
  else:
    break
print(ans)

#sol2 최대공약수
ans = 0
i = 1
while 5**i <= n:
  i+=1

for num in range(1,n+1):
  for j in range(i-1,0,-1):
    if num % (5**j) == 0:
      ans += j
      break

print(ans)

#sol3 최대공약수,dp
def solution(n):
    ans=0
    dp=[-1]*(n+1)
    def find(num):
        if dp[num]!=-1:
            return dp[num]
        
        if num%5==0:
            dp[num]=dp[num//5]+1
        else:
            dp[num]=0
        return dp[num]
    for i in range(1,n+1):
        find(i)
    
    ans=sum(dp[1:])
    print(ans)
    return ans
