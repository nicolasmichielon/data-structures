class Element:
  def __init__(self, value):
    self.value = value
    self.next = None

  def setNext(self, next):
    self.next = next

  def getNext(self):
    return self.next

class LinkedQueue:
  def __init__(self):
    self.head = None
    self.tail = None

  def printQueue(self):
    current = self.head
    while current != None:
      print(current.value)
      current = current.getNext()

  def enqueue(self, value):
    e = Element(value)
    if self.head == None:
      self.head = e
      self.tail = self.head
      return
    self.tail.setNext(e)
    self.tail = e

  def dequeue(self):
    if self.head == None:
      return
    self.head = self.head.getNext()
