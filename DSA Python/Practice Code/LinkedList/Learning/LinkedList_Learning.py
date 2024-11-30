class Node:
    def __init__(self,data=None,Next=None):
        self.data=data
        self.Next=Next

class LinkedList:

    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def print(self):
        itr=self.head
        #print(self.head.Next.Next.data)
        listr=''
        while itr:
            suffix=''
            if itr.Next:
                suffix='-->'
            listr+=str(itr.data)+suffix
            itr=itr.Next
        print(listr)

    def length_of_list(self):
        idx=0
        itr=self.head
        while itr:
            idx+=1
            itr=itr.Next

        #print(f"lenght of list: ",idx)
        return idx

    def insert_at_the_end(self,data):
        node=Node(data)

        if self.head is None:
            self.head=node
            return

        itr=self.head
        while itr:
            if(itr.Next==None):
                itr.Next=node
                break
                
            itr=itr.Next   


    def insert_at(self,index,data):
        if index < 0 or index > self.length_of_list():
            raise Exception("Invalid Index")

        if index==0:
            insert_at_begining(data)
        
        counter=0
        itr=self.head
        
        while itr:

            if(counter==index-1):
                itr.Next=Node(data,itr.Next)
                break
                
            counter+=1
            itr=itr.Next


    def remove_at(self,index):
        if index < 0 or index > self.length_of_list():
            raise Exception("Invalid Index")

        if index==0 :

            self.head=self.head.Next
            return
        

        
        counter=0

        itr=self.head

        while itr:
            if counter == index-1:
                itr.Next=itr.Next.Next
                break

            counter+=1
            itr=itr.Next
            

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_the_end(data)

            


if __name__ == '__main__':
    
    root=LinkedList()
    root.insert_at_begining(15)
    root.insert_at_begining(25)
    root.insert_at_begining(16)
    root.insert_at_begining(168)
    #root.print()
    #root.length_of_list()
    # root.insert_at_the_end(204)
    # root.insert_at_the_end(444)
    # root.insert_at_the_end(850)
    # root.insert_at_begining(54)
    # root.insert_at_the_end(6)
    # root.print()
    # print("++++++ Before Insert +++++++")
    # #root.insert_at(4,75)
    # root.remove_at(2)
    # root.print()


    NewList=LinkedList()
    NewList.insert_values([12,23,4,5,55])
    NewList.print()

### Execution Explanation ###
"""

root=LinkedList() --> root is the LinkedList created

root.insert_at_begining(15) --> 

def insert_at_begining(self,data=15):
        node=Node(data=15,self.head)   [data=15,Next=None]
        self.head=node  #currentNode=[15,None] Here 15 is Data and None next Node

def insert_at_begining(self,data=25):
        node=Node(data=25,NextNode=[15,None])   [data=15,Next=None]
        self.head=node  #CurrentNode=[25,[15,None]]  Here 25 is data 15 is next node

def insert_at_begining(self,data=16):
        node=Node(data=16,NextNode=[25,None])   [data=25,Next=[15,None]]
        self.head=node  #CurrentNode=[16,[25,15]]  Here 16 is data 25 is next node


"""