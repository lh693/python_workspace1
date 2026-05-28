import pickle  #프로그램이 외부에있는데 내 메모리로 불러오기 

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age 
    
    def output(self):
        print("이름 :", self.name, " 나이:", self.age) 

perList = [Person("홍길동", 23), 
           Person("장길산", 33)]

with open("person.dat", "wb") as f:
    pickle.dump(perList, f) #직렬화 

with open("person.dat", "rb") as f:
    s =pickle.load( f) #역직렬화 
    
for a in s:
    a.output()
