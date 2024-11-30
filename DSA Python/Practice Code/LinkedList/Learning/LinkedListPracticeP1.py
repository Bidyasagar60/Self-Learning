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

    def show_data(self):
        itr=self.head

        liststr=''
        while itr:
            suffix=''
            if itr.Next:
                suffix='-->'
                
            liststr+=str(itr.data)+suffix
            itr=itr.Next

        print(liststr)

    ### Problem 1 solution method
    def insert_value_after(self,data,insertdata):

        itr=self.head

        if itr.Next is None and itr.data != data:
            print(f"{data} is not present in the list.")
            return
        DataFound=False

        while itr:
            if itr.data==data:
                itr.Next=Node(insertdata,itr.Next)
                DataFound=True
                break

            itr=itr.Next

        if(DataFound is False):
            print(f"{data} is not present in the list.")


    ### Problem 2 solution methon

    def remove_by_value(self,remove_data):

        itr=self.head

        IsDataPresent=False

        if itr.Next is None :
            if itr.data==remove_data:
                self.head=self.head.Next
                return
            else:
                print(f"{remove_data} is not present in the list ")
                return
        
        while itr:
            

            if itr.Next.data==remove_data:
                #itr.Next=itr.Next.Next
                self.head=self.head.Next
                IsDataPresent=True
                break
                    
            itr=itr.Next
                
        if IsDataPresent is False:
            print(f"{remove_data} is not present in the list ")
        




if __name__=='__main__':

    root=LinkedList()
    root.insert_at_begining(50)
    # root.insert_at_begining(36)
    # root.insert_at_begining(22)
    root.insert_at_begining(42)
    root.show_data()
    #root.insert_value_after(51,500)
    root.remove_by_value(51)
    root.show_data()







"""
Problem Statement:

def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data

ListA=[10,25,26,36,66]

Q1:Insert 60 after 36

New List Looks Like [10,25,26,36,60,66]

Q2: remove 26 from the list


"""