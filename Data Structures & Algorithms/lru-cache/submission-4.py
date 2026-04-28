class Node:
    def __init__(self, key:int=0, value: int=0):
        self.key=key
        self.value=value
        self.prev= None
        self.next= None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity= capacity
        self.cache={}
        self.dummyhead= Node()
        self.dummytail= Node()
        self.dummyhead.next= self.dummytail
        self.dummytail.prev= self.dummyhead

    def addtoend(self, node):
        prevnode= self.dummytail.prev
        prevnode.next= node
        node.prev= prevnode
        node.next= self.dummytail
        self.dummytail.prev= node

    def remove(self,node):
        prevnode= node.prev
        nextnode= node.next
        prevnode.next= nextnode
        nextnode.prev= prevnode

    def removelru(self, node):
        lru= self.dummyhead.next
        self.remove(lru)
        return lru.key

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node= self.cache[key]
        self.remove(node)
        self.addtoend(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node= self.cache[key]
            node.value= value
            self.remove(node)
            self.addtoend(node)

        else:
            if len(self.cache)== self.capacity:
                lrunode= self.dummyhead.next
                self.remove(lrunode)
                del self.cache[lrunode.key]

            newnode= Node(key,value)
            self.cache[key]= newnode
            self.addtoend(newnode)
        
