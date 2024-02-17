# https://leetcode.com/problems/design-an-ordered-stream/description/

# class OrderedStream:

#     def __init__(self, n: int):
#         self.Orders=[None]*n

#     def insert(self, idKey: int, value: str) -> List[str]:
#         self.Orders.insert(idKey,value)
#         if idKey!=0 or self.Orders[:idKey]!=0:
#             return self.Orders[:idKey]
#         else:
#             return []

class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0 # 0-indexed 

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1 # 0-indexed 
        self.data[id] = value 
        if id > self.ptr: return [] # not reaching ptr 
        
        while self.ptr < len(self.data) and self.data[self.ptr]: self.ptr += 1 # update self.ptr 
        return self.data[id:self.ptr]
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)