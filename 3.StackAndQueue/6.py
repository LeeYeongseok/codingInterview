
import sys
from collections import deque

class animal:
    
    def __init__(self):
        self.cat = deque()
        self.dog = deque()
        self.order = 0
    
    def enqueue(self, kind, name):
        if kind == 1:
            self.cat.append([self.order, name])
        elif kind == 2:
            self.dog.append([self.order, name])
        else:
            print("유효하지 않은 종류입니다")
            return
        self.order += 1
    
    def dequeueDog(self):
        if len(self.dog) == 0:
            return "강아지가 없음"
        return self.dog.popleft()[1]
    
    def dequeueCat(self):
        if len(self.cat) == 0:
            return "고양이가 없음"
        return self.cat.popleft()[1]
        
    def dequeueAny(self):
        if len(self.cat) and not len(self.cat):
            return self.dequeueCat()
        if not len(self.cat) and len(self.cat):
            return self.dequeueDog()
        #강아지가 먼저 들어왔을때
        if self.cat[0][0] > self.dog[0][0]:
            return self.dequeueDog()
        #고양이가 먼저 들어왔을때
        else:
            return self.dequeueCat()
        
shelter = animal()

while True:
    print("1. 동물 유기하기, 2. 동물 입양하기")
    c = int(input())
    if c == 1 :
        print("1. 고양이, 2. 강아지 (ex) 2 뽀삐)")
        kind, name = sys.stdin.readline().split()
        kind = int(kind)
        shelter.enqueue(kind, name)
    elif c ==2 :
        print("1. 고양이, 2. 강아지 3. 아무거나")
        getAnimal = int(input())
        if getAnimal == 1:
            print(shelter.dequeueCat())
        elif getAnimal == 2:
            print(shelter.dequeueDog())
        elif getAnimal == 3:
            print(shelter.dequeueAny())
    else:
        break
    print(shelter.cat)
    print(shelter.dog)