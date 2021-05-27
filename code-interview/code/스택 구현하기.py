'''
스택 구현하기(push,pop,top,empty,size,min)
push,pop,min 의 시간 복잡도는 O(1)이 되야 한다
'''
class stack():
  def __init__(self):
    self.MAX_SIZE =  1000
    self.li = [0]*self.MAX_SIZE
    self.min_stack = []
    self.top = 0
  
  def push(self,n):
    if self.top+1 >= self.MAX_SIZE:
      return False
    else:
      self.li[self.top] = n
      if not self.min_stack:
        self.min_stack.append(n)
      else:
        if self.min_stack[-1] >= n:
          self.min_stack.append(n)
      self.top+=1
  def pop(self):
    self.top-=1
    ans = self.li[self.top]
    if ans == self.min_stack[-1]:
      self.min_stack.pop()
    return ans
  def size(self):
    return self.top
  def empty(self):
    if self.top == 0:
      return True
    return False
  def top(self):
    return self.li[self.top-1]
  def min(self):
    return self.min_stack[-1]

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