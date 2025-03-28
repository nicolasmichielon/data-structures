class Element:
  def __init__(self, value):
    self.value = value
    self.next = None

  def setNext(self, next):
    self.next = next

  def getNext(self):
    return self.next
  
  
class linkedStack:
  def __init__(self):
    self.top = None

  def push(self, value):
    e = Element(value)
    e.setNext(self.top)
    self.top = e

  def pop(self):
    if self.top == None:
      return
    self.top = self.top.getNext()
