import pickle 

class Student:
    def __init__(self, name="", kor=0, eng=0, mat=0):
        self.name = name 
        self.kor = kor 
        self.eng = eng 
        self.mat = mat 
        self.process()

    def process(self):
        self.total = self.kor + self.eng + self.mat 
        self.avg = self.total/3
        if self.avg>=90:
            self.grade="수"
        elif self.avg>=80:
            self.grade="우"
        elif self.avg>=70:
            self.grade="미"
        elif self.avg>=60:
            self.grade="양"
        else:
            self.grade="가"
    
    def output(self):
        print(self.name,  end="\t")
        print(self.kor,   end="\t")
        print(self.eng,   end="\t")
        print(self.mat,   end="\t")
        print(self.total, end="\t")
        print(f"{self.avg:.2f}",   end="\t")
        print(self.grade)

# s1 = Student("a", 90, 80, 70)
# s1.output()

class StudentManager:
    def __init__(self):
        self.stList = [
                            Student("a", 90, 80, 70), 
                            Student("b", 90, 90, 80), 
                            Student("c", 80, 80, 70)
                    ] 
    def output(self):
        for st in self.stList:
            st.output()

    def sort(self):
        #원본데이터는 보통 놔둔다 sorted함수
        resultList = sorted(self.stList, key = lambda ob : ob.total, reverse=True)
        for r in resultList:
            r.output()

    def searchName(self):
        name = input("찾을 이름 ?")
        #filter(콜백함수, 이터러블(반복자, list, tuple들))
        #filter 호출될 콜백함수는 매개변수가 반드시 하나이어야 하고, 반환값이 True 또는 False
        #이어야 한다. True 인 데이터만 모아준다 
        #for 안쪽이 수행되었는지를 확인하고 싶다 => 알고리즘, 자료구조 
        #numpy , pandas 깊게  numpy 파이썬의 list는 연결리스트 본래의미의 배열이 아님 
        #numpy - c의 배열, 속도가 엄청 빠르다. 벡터연산지원, 딥러닝, 머신러닝이든 
        #반드시 numpy 로 바뀌어야 한다  pandas 라이브러리에 dataframe :dict 타입과 클래스 중간
        flag=False
        for data in filter( lambda x:x.name==name, self.stList):
            data.output() 
            flag = True 
        
        if not flag:
            print(name + " 이 없습니다")

    def save(self): #저장하기 
        with open("score.dat", "wb") as ff:
            pickle.dump(self.stList, ff)

        print("저장성공")

    def load(self):
        with open("score.dat", "rb") as ff:
            self.stList = pickle.load(ff)
        print("불러오기성공")

    def menu(self):
        print("1. 출력")
        print("2. 검색")
        print("3. 정렬")
        print("4. 저장")
        print("5. 불러오기")
        print("0. 종료")
        pass 

    def main(self):
        while True: #무한루프 
            self.menu()
            sel = input("선택 : ")
            if sel=="1": 
                self.output() 
            elif sel=="2":
                self.searchName()
            elif sel=="3":
                self.sort()
            elif sel=="4":
                self.save()
            elif sel=="5":
                self.load() 
            else:
                break #while문 종료 , 
        pass 

mgr = StudentManager()
mgr.main()


"""
class Kor
class Eng
class Mat

class Student:
    Kor kor;
    Eng eng;
"""
