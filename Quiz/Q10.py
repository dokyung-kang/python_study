# 내가 푼 문제

class Calculator:
    def __init__(self, arr):
        self.arr = arr

    def sum(self):
        total = 0
        for n in self.arr:
            total += n
        return total

    def avg(self):
        total = 0
        for n in self.arr:
            total += n
        average = total / len(self.arr)
        return average

cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())