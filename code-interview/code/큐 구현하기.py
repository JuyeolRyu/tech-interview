'''
[큐 구현하기]
<enqueue, dequeue, isEmpty, isFull> 기능 직접 구현해보기
'''
class queue():
  def __init__(self):
    self.MAX_SIZE =  10
    self.q = [None]*self.MAX_SIZE
    self.front = 0
    self.rear = 0
  def isEmpty(self):
    return self.front == self.rear
  def isFull(self):
    return self.front == (self.rear+1)%self.MAX_SIZE

  def enqueue(self,n):
    if not self.isFull():
      self.rear = (self.rear+1)%self.MAX_SIZE
      self.q[self.rear] = n
  def dequeue(self):
    if not self.isEmpty():
      self.front = (self.front+1)%self.MAX_SIZE
      return self.q[self.front]

q = queue()
for i in range(10):
  q.enqueue(i)
for i in range(11):
  print(q.dequeue())