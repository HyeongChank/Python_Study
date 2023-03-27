"""
str = "asdasdasdasd"
flag =0
for index, ch in enumerate(str):
    if ch =='a':
        print(index)
        flag =1
if flag ==0:
    print("없음")
    
def sum(a,b):
    return a+b
def sub(a,b):
    return abs(a-b)
def mul(a,b):
    return a*b
def div(a,b):
    if a>b:
        return a/b
    else:
        return b/a
print(div(3,4))

table = {'1':sum, '2':sub, '3':mul, '4':div}

m = input("작성")
m1 = int(input("숫자1"))
m2 = int(input("숫자2"))
func = table[m]
print(func(m1,m2))


m = 'led=on&motor=off&switch=off'
led2 = m.split("&")
led3 =[]
for i in led2:
    print(i)
    led3.append(i.split("="))
print(led3)

def spl(a):
    c = []
    b = a.split("&")
    for i in b:
        c.append(i.split("="))
    print(c)
    
spl("led=on&motor")
                 
                 
class Rectangle:
    def __init__(self, width, height, q):
        self.width = width
        self.height = height
        self.q = q

    def area(self):
        return self.width * self.height * self.q
    

# 인스턴스 생성
rectangle1 = Rectangle(3, 4,2)
rectangle2 = Rectangle(5, 6,10)

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4
print(rectangle2.width) # 출력 결과: 5
print(rectangle2.height) # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle2.area()) # 출력 결과: 30


class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height

# 클래스 변수 값을 출력
print(Rectangle.count) # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
print(Rectangle.count) # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
print(Rectangle.count) # 출력 결과: 2

class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)

# 클래스 메서드 호출
Rectangle.print_count() # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
Rectangle.print_count() # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
Rectangle.print_count() # 출력 결과: 2



class Calculator:
    # 클래스 변수
    operator = '+'

    # 클래스 메서드
    @classmethod
    def set_operator(cls, new_operator):
        cls.operator = new_operator

    # 인스턴스 메서드
    def calculate(self, num1, num2):
        if Calculator.operator == '+':
            return num1 + num2
        elif Calculator.operator == '-':
            return num1 - num2
        elif Calculator.operator == '*':
            return num1 * num2
        elif Calculator.operator == '/':
            return num1 / num2
mcal = Calculator()
print(mcal.calculate(2,3))
Calculator.set_operator("*")
print(mcal.calculate(2,3))
#c = Calculator.calculate('+',3,2)
#print(c)

class Deposit:
    def __init__(initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n
        
#    def profit(self):

 
#__age, __name 은 private이라서 상속을 주려면 getter, setter를 만들어야 함
class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name        
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age        



    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))

class Teacher(People) :
    def __init__(self, age=0, name=None, school=None) :
        super().__init__(age, name)
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)
        
s = Teacher("12","d", "high")
s.showSchool()
s.introMe()


class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def getName(self): 
        print(self.name) 

    def getAge(self): 
        print(self.age) 

class Employee(Person):
    def __init__(self, name=None, age =0, employeeID = None):
        super().__init__(name,age)
        self.employeeID = employeeID
    def getID(self):
        print("my id : ", self.employeeID)

    def getAge10(self):
        print(self.age + 100)
        
    def toString(self):
        print(self.name, self.age, self.employeeID)
d = Employee("khc",23,"jsk")
d.getID()
d.getAge10()
d.toString()




class Character:
    def __init__(self, name, level, health):
        self.name = name
        self.level = level
        self.health = health
    
    def attack(self):
        print(f"{self.name} attacks with a normal attack.")

class Warrior(Character):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health)
        self.strength = strength
    
    def attack(self):
        print(f"{self.name} attacks with a mighty swing.")
    
    def smash(self):
        print(f"{self.name} smashes the ground with a powerful blow.")

class Mage(Character):
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.magic = magic
    
    def attack(self):
        print(f"{self.name} casts a magic missile.")
    
    def teleport(self):
        print(f"{self.name} teleports to a nearby location.")

w = Warrior("j",3,10,10)
w.attack()


class Game:
    def __init__(self, player_name, player_hp, player_attack, monster_name, monster_hp, monster_attack):
        self.player_name = player_name
        self.player_hp = player_hp
        self.player_attack = player_attack
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack

    def fight(self):
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"{self.player_name}의 체력: {self.player_hp}")
            print(f"{self.monster_name}의 체력: {self.monster_hp}")
            self.monster_hp -= self.player_attack
            print(f"{self.player_name}이 {self.monster_name}을 공격하여 {self.player_attack}의 데미지를 입혔습니다.")
            if self.monster_hp <= 0:
                print(f"{self.monster_name}을 물리쳤습니다.")
                break
            self.player_hp -= self.monster_attack
            print(f"{self.monster_name}이 {self.player_name}을 공격하여 {self.monster_attack}의 데미지를 입혔습니다.")
            if self.player_hp <= 0:
                print(f"{self.player_name}이 죽었습니다.")
                break
g = Game("a",30,10,"b",40,20)
g.fight()


class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_monster(self, monster):
        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다.")
        damage = self.attack
        monster.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name}이(가) {player.name}을(를) 공격했습니다.")
        damage = self.attack
        player.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")


class Game:
    def __init__(self):
        self.player = None
        self.monster = None

    def create_player(self, name, hp, attack):
        self.player = Player(name, hp, attack)

    def create_monster(self, name, hp, attack):
        self.monster = Monster(name, hp, attack)

    def fight(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player.attack_monster(self.monster)
            if self.monster.hp <= 0:
                break
            self.monster.attack_player(self.player)
            if self.player.hp <= 0:
                break
game = Game()
game.create_player("Alice", 100, 10)
game.create_monster("Goblin", 50, 5)
game.fight()

"""
class Student:
    def __init__(self, name, student_id, year, major):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
    def get_info(self):
        print(self.name, self.student_id, self.year, self.major)
s = Student('k','jsk',4,'phy')
#s.get_info()

class StudentManager:
    def __init__(self):
        self.student_list =[]
        
    def add_student(self, student):
        self.student_list.append(student)
        
    def remove_st(self,student):
        for i in student_list:
            if i ==self.name:
                self.student_list.remove(student)
    def print_st(self):
        for st in self.student_list:
            print(st.get_info())
sm = StudentManager()
student1 = Student('j','2323',2,'com')
student2 = Student('k','2323',2,'com')
sm.add_student(student1)
sm.add_student(student2)
sm.print_st()





