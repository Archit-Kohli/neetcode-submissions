class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append((timestamp,value))
        else:
            self.hmap[key] = [(timestamp,value),]
        # print(self.hmap)

    def get(self, key: str, timestamp: int) -> str:
        # print(self.hmap)
        if key not in self.hmap:
            return ""
        find = self.hmap[key]
        start = 0
        end = len(find)-1
        out = ""
        while start<=end:
            mid = (start+end)//2
            # print(find[mid])
            if find[mid][0]==timestamp:
                return find[mid][1]
            if find[mid][0]<timestamp:
                out = find[mid][1]
                start = mid+1
            else:
                end = mid -1
        return out
        