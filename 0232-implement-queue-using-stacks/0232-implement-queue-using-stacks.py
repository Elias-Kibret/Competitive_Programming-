class MyQueue:

    def __init__(self):
        self.que=[]
        

    def push(self, x: int) -> None:
        # print(x)
        self.que=[x]+self.que
        

    def pop(self) -> int:
       print(self.que)
       return self.que.pop(-1)
        

    def peek(self) -> int:
       return  self.que[-1]
        

    def empty(self) -> bool:
        return len(self.que)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()