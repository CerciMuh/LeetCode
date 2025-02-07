class TimeMap:

    def __init__(self):
        self.struct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.struct:
            self.struct[key]=[]
        self.struct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.struct:
            return ""
        left = 0 
        right = len(self.struct[key])-1
        if key in self.struct:
            while (left<=right):

                middle = (left+right)//2
                if self.struct[key][middle][0] == timestamp:
                    return self.struct[key][middle][1]
                elif self.struct[key][middle][0] < timestamp:
                    left = middle+1
                else:
                    right= middle - 1
            return self.struct[key][right][1] if right >= 0 else ""     
              
        else:
            return ""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)