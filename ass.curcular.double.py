class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class cdll:
    def __init__(self):
        self.start=None
    
    def is_empty(self):
        return self.start is None
        
    def insert_first(self,data):
        n=node(data)
        if self.start==None:
            n.prev=n
            n.next=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n        
        self.start=n
    
    def insert_last(self,data):
        n=node(data)
        if self.start==None:
            n.prev=n
            n.next=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n   
    
    def insert_after(self,target,data):
        if self.start is None:
            return self.is_empty()
        n=node(data)
        current=self.start
        while True:
            if current.data==target:
                n.next=current.next
                n.prev=current
                current.next.prev=n
                current.next=n
            current=current.next
            if current is self.start:
                break
    
    def delete_first(self):
        if self.start is None:
            return self.is_empty()
        if self.start.next==self.start:
            self.start=None
        self.start.prev.next=self.start.next
        self.start.next.prev=self.start.prev
        self.start=self.start.next
    
    def delete_last(self):
        if self.start is None:
            return self.is_empty()
        if self.start.next is self.start:
            self.start = None
        self.start.prev.prev.next=self.start
        self.start.next.prev=self.start.prev.prev
    
    '''def delete_value(self,data):
        if self.start is None:
            return self.is_empty()
        current=self.start
        while True:
            if current.data==data:
                if current is self.start:
                    if current.next is self.start:
                        current=None
                    else:
                        current.next.prev = current.prev
                        current.prev.next = current.next
                        self.start=current.next
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                break
            current=current.next
            if current is self.start:
                break'''
    
    def delete_value(self, data):
        if self.start is None:
            return self.is_empty()
    
        current = self.start
        while True:
            if current.data == data:
                self._delete_node(current)
                break  # Break out of the loop after deleting the node
            
            current = current.next
            if current is self.start:
                break  # Break out of the loop when reaching the end of the list
    
    def _delete_node(self, node):
        if node.next is self.start:
            # Check if it's the only node in the list
            if node.prev is node:
                self.start = None
            else:
                node.prev.next = self.start
                self.start.prev = node.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        # Optionally, you can delete the current node
        if node is self.start:
            self.start = node.next

        del node
    
            
    def display(self):
        if self.start is None:
            return None
        current=self.start
        while True:
            print(current.data)
            current=current.next
            if current is self.start:
                break
mylist=cdll()
mylist.insert_first(5)
mylist.insert_first(0)
mylist.insert_last(10)
mylist.insert_after(10,4)
mylist.delete_first()
mylist.delete_last()
mylist.delete_value(5)
mylist.display()