queue=[]
def enqueue():
    element=int(input("enter the value"))
    queue.append(element)
    print("element is insert")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("element is remov",e)
def display():
    print(queue)
while True:
    print("choose the operation 1.enqueue,2.dequeue,3.display,4.exit")
    choose=int(input())
    if choose==1:
        enqueue()
    elif choose==2:
        dequeue()
    elif choose==3:
        display()
    elif choose==4:
        exit()
    else:
        print("choose within options")
    

    