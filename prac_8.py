#stack using the class and objects
#ID: 20CE045
#NAME: Yashvi Kotadiya
class stack:
    def __init__(self):
        self.items=[]

    def push(self,a):
        self.items.append(a)

    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items==[]

s=stack()
while True:
    print('push <value>')
    print('pop')
    print('quit')
    what_to_do=input('what do you want to do: ').split()

    opr=what_to_do[0].strip().lower()
    if opr=='push':
        s.push(int(what_to_do[1]))
    elif opr=='pop':
        if s.isempty():
            print("stack is empty")
        else:
            print('poped element is' , s.pop())

    elif opr=='quit':
        break