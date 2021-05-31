'''
split 구현하기
'''
def split(s,d):
  ans = []
  left = 0
  for i,c in enumerate(s):
    if c in d:
      ans.append(s[left:i])
      left = i+1
  
  if left < len(s):
    ans.append(s[left:])
  return ans

print(split("a cdefghd",[' ','d']))