    def search_from_head(self, data):   # search_from_head 함수 생성
        if self.head == None:           # head 값이 없으면 false를 리턴
            return False
    
        node = self.head                # node 변수에 head를 담는다.
        while node:                     
            if node.data == data:       # node 변수(head)에 데이터 값이 입력 받은 데이터 값과 같으면 조건문 실행
                return node             # node 변수를 리턴한다.
            else:                       # node 변수에 데이터 값이 입력 받은 데이터 값과 다르면
                node = node.next        # node 변수에 다음 node의 주소 값을 담는다.
        return False                
    
    def search_from_tail(self, data):   # search_from_tail 함수 생성
        if self.head == None:           # head 값이 없으면 false를 리턴
            return False
    
        node = self.tail                # node 변수에 tail을 담는다.
        while node:             
            if node.data == data:       # node 변수(tail)에 데이터 값이 입력 받은 데이터 값과 같으면 조건문 실행
                return node             # node 변수를 리턴한다.
            else:                       # node 변수에 데이터 값이 입력 받은 데이터 값과 다르면
                node = node.prev        # node 변수에 다음 node의 주소 값을 담는다.
        return False
    
    def insert_before(self, data, before_data): # 입력하려는 데이터 값과 입력하려는 값의 next 데이터를 받는 insert_before 함수 생성
        if self.head == None:                   # head가 없으면
            self.head = Node(data)              # 입력 받은 값으로 head를 선언
            return True
        else:                                   # head가 있으면
            node = self.tail                    # node 변수에 tail 노드를 담는다.
            while node.data != before_data:     # node 변수에 값과 before_data이 다르면
                node = node.prev                # node 변수에 node.prev를 담는다.
                if node == None:                # node 변수에 값이 없으면 false를 리턴한다.
                    return False
            new = Node(data)                    # new 변수에 입력 받은 데이터를 노드로 만들어 담는다.  (ex. data = 7)
            before_new = node.prev              # before_new 변수에 before_data의 prev 주소를 담는다. (ex. before_new = 8.prev = 6)
            before_new.next = new               # before_new.next 변수에 new 변수를 담는다. (ex. 7)
            new.prev = before_new               # new.prev 변수에 before_new를 담는다. (ex. 8.prev = 6)
            new.next = node                     # new.next 변수에 node를 담는다 (ex.8)
            node.prev = new                     # node.prev 변수에 new를 담는다 (7)
            return True
