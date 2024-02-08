# 28279 덱 2
import sys
input = sys.stdin.readline

class CustumDeque:
    
    def __init__(self, max_num:int) -> None:
        self.queue = [0]* max_num
        self.first_index = 0
        self.last_index = 0
        self.l = 0
        self.max_index = max_num-1

    def insert_first(self, num:int) -> None:
        if self.l:
            if self.first_index:
                self.first_index -= 1
            else:
                self.first_index = self.max_index
        self.l +=1
        self.queue[self.first_index] = num
        
    def insert_last(self, num:int) -> None:
        if self.l:
            if self.last_index == self.max_index:
                self.last_index = 0
            else:
                self.last_index += 1
            if self.l == 0:
                self.last_index += 1
        self.l +=1
        self.queue[self.last_index] = num
    
    def pop_first(self) -> int:
        if self.l:
            num = self.queue[self.first_index]
            self.queue[self.first_index] = 0
            if self.last_index != self.first_index:
                if self.first_index == self.max_index:
                    self.first_index = 0
                else:
                    self.first_index += 1
            self.l -= 1
            return num
        else:
            return -1
    
    def pop_last(self) -> int:
        if self.l:
            num = self.queue[self.last_index]
            self.queue[self.last_index] = 0
            if self.last_index != self.first_index:
                if self.last_index == 0:
                    self.last_index = self.max_index
                else:
                    self.last_index -= 1
            self.l -= 1
            return num
        else:
            return -1
    
    def length(self) -> int:
        return self.l
    
    def is_empty(self) -> bool:
        return 0 if self.l else 1
    
    def print_first(self) -> int:
        return self.queue[self.first_index] if self.l else -1

    def print_last(self) -> int:
        return self.queue[self.last_index] if self.l else -1
        



def solution():
    N = int(input())
    cq = CustumDeque(N)
    
    for _ in range(N):
        order, *num = map(int, input().split())
        if order == 1:
            cq.insert_first(*num)
        elif order == 2:
            cq.insert_last(*num)
        elif order == 3:
            print(cq.pop_first())
        elif order == 4:
            print(cq.pop_last())
        elif order == 5:
            print(cq.length())
        elif order == 6:
            print(cq.is_empty())
        elif order == 7:
            print(cq.print_first())
        else:
            print(cq.print_last())


if __name__ == "__main__":
    solution()
