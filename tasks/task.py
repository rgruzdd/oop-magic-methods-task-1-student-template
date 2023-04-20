from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, b):
        num = []
        for i in self.values:
            num.append(str(i) + ' ' + b)
        return num





counter = Counter([1, 2, 3]) + "mississippi"
print(counter)
# ["1 mississippi", "2 mississippi" , "3 mississippi"]
