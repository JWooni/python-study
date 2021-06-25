dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

# count = 0
# for data in dataset:
#     for i in range(len(data)):
#         if data[i] == 'M':
#            count += 1

# print(count)           


# import queue
# data_queue = queue.Queue()

# data_queue.put("funcoding")
# data_queue.put(1)

# print(data_queue.qsize())
# print(data_queue.get())

# def recursive(data):
#     if data < 0:
#         print('ended')
#     else:
#         print(data)
#         recursive(data - 1)
#         print('returned', data) 

# recursive(4)          
 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def add(data):
        node = head
        while node.next:
            node = node.next
        node.next = Node(data) 

node1 = Node(1)
head = node1
for index in range(1, 10):
    add(index)
    # print(index)

node = head

while node.next:
    print(node.data)
    node = node.next
print (node.data)    