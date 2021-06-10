class my_iterator:
    def __init__(self, n):
        self.i = 0
        self.n = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration


class my_reverse_iterator:
    def __init__(self, n):
        self.i = n - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= 0:
            i = self.i
            self.i -= 1
            return i
        else:
            raise StopIteration


y = my_iterator(5)
print(f"{next(y)}")
print(f"{next(y)}")
print(f"{next(y)}")
print(f"{next(y)}")
print(f"{next(y)}")




z = my_reverse_iterator(5)
print(f"{next(z)}")
print(f"{next(z)}")
print(f"{next(z)}")
print(f"{next(z)}")
print(f"{next(z)}")
