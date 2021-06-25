class Node:                                 # 노드 클래스 생성
    def __init__(self, data, next=None):    # data, next를 받는다.
        self.data = data                    # self.data에 입력 받은 data를 넣는다.
        self.next = next                    # self.next에 

class Nodemgnt:                             # 노드 추가와 출력 클래스 생성
    def __init__(self, data):               # data, next를 받는다.
        self.head = Node(data)              # head에 node 클래스를 통해 만든 노드 값을 넣는다.

    def add(self, data):                    # 추가 함수 생성
        node = self.head                    # node 변수에 head를 넣는다.
        while node.next:                    # node.next에 값이 있으면 반복문을 실행한다.
            node = node.next                # node 변수에 node.next 값을 넣는다.
        node.next = Node(data)              # node.next 값이 없으면 node.next에 입력 받은 data값을 넣는다.

    def desc(self):                         # 출력 함수 생성
        node = self.head                    # node 변수에 head를 넣는다. 
        while node:                         # node에 값이 있으면 반복문을 실행한다.
            print(node.data)                # node의 값을 출력한다.
            node = node.next                # node 변수에 node.next를 넣는다.


linkedlist = Nodemgnt(0) 
for data in range(1, 10):
    linkedlist.add(data)
linkedlist.desc()