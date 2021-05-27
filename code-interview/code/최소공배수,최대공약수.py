'''
최소공배수,최대공약수 구하기
'''
def gcd(a,b):
  ret = 0
  for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
      ret = i
  return ret
#유클리드 호제법 사용
def gcd2(a,b):
  if a%b == 0:
    return b
  return gcd2(b,a%b)

def lcm(a,b):
  i = 1
  while True:
    if (a*i)%b == 0:
      return a*i
    i+=1
#최소공배수가 두값의 곱을 최대공약수로 나눈값인 것을 이용
def lcm2(a,b):
  return (a*b)//gcd(a,b)
  
print(gcd(4,6))
print(gcd2(4,6))
print(lcm(4,6))
print(lcm2(4,6))