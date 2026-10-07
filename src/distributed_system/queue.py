from collections import deque
class LocalQueue:
 def __init__(self): self.items=deque()
 def put(self,item): self.items.append(item)
 def get(self): return self.items.popleft() if self.items else None
