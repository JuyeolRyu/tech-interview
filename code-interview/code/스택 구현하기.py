'''
스택 구현하기(push,pop,top,empty,size,min)
push,pop,min 의 시간 복잡도는 O(1)이 되야 한다
'''
class stack():
  def __init__(self,n):
    self.MAX_SIZE =  n
    self.stack = []
    self.top = -1
  
  def push(self,n):
    if self.top+1 >= self.MAX_SIZE:
      return False
    else:
      if not stack:
        stack.append([num,num])
      else:
        stack.append([num,min(stack[-1][0],num)])
      self.top+=1
  def pop(self):
    if top == -1:
      return False
    num=self.stack.pop(top)[0]
    self.top-=1
    return num
  def size(self):
    return self.top+1
  def isEmpty(self):
    if self.top == -1:
      return True
    return False
  def top(self):
    return self.stack[self.top]
  def min(self):
    return self.stack[-1][1]

st = stack()
st.push(2)
st.push(6)
st.push(1)
print(st.size())
print(st.empty())
print(st.min())
print(st.pop())
print(st.min())
print(st.pop())
print(st.min())
