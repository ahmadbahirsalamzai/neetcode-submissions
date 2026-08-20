class TimeMap:
    def __init__(self):
        self.keyVS = dict()  # key=string, list of [values, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyVS:
            self.keyVS[key] = []

        self.keyVS[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.keyVS or key not in self.keyVS:
            return ""

        res = ""
        values = self.keyVS.get(key, [])

        l = 0
        r = len(values) - 1

        while l <= r:
            m = l + (r - l) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]

                # early return
                if values[m][1] == timestamp:
                    return res

                l = m + 1

            else:
                r = m - 1

        return res
