#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''NODE CLASS'''
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# In[11]:


'''Implementing linked list'''
class LinkedList:
    '''declaring the head'''
    def __init__(self):
        self.head = None
    
    '''inserting into begginning of the LL'''
    def insert_beg(self,data):
        print('inserting into the beginning')
        node = Node(data,self.head)
        print(node)
        self.head = node
        print('node::',node)
    
    '''defining the print '''
    def print(self):
        if self.head is None:
            print('The linked list is empty!!')
            return
        itr = self.head
        llist=''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
        print(llist)
        
    '''Inserting into the end'''
    def insert_end(self,data):
        print('Inserting into the end of LL')
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        '''When LL is not blank'''
        itr = self.head
        
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

            
    '''Converting a list into LL'''
    def insert_list(self,list):
        self.head = None
        for i in list:
            self.insert_beg(i)
            
    '''Giving the length of a LL'''
    def lengthLL(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    
    '''Removing an element at a particular index'''
    def remove_at(self,index):
        itr = self.head
        if index < 0 or index > self.lengthLL():
            print('Invalid index')
            return
        if index == 0:
            self.head = itr.next
            return
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1
            
    
    '''Inserting at a particular location'''
    def insert_at(self,index,data):
        if index < 0 or index > self.lengthLL():
            print('Invalid index!! cannot insert elements here')
        
        if index == 0:
            self.insert_beg(self.data)
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    temp = itr.next
                    itr.next = Node(data, temp)
                itr = itr.next
                count +=1
                
    '''Inserting after a certain value'''            
    def insert_after_value(self, data_after, data):
        itr = self.head
        while itr:
            if itr.data == data_after:
                temp = itr.next
                itr.next = Node(data,temp)
            itr = itr.next
            
    '''Removing by value in the LL'''
    def remove_by_value(self,data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next 
        
        while itr:
            
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
                    


# In[12]:


a = LinkedList()


# In[13]:


a.print()


# In[14]:


a.insert_beg(500)


# In[28]:


a.print()


# In[16]:


a.insert_end(966000)


# In[26]:


a.print()


# In[25]:


a.remove_by_value(966000)


# In[27]:


a.insert_after_value(2200,30)


# In[20]:


a.remove_at(-5)


# In[21]:


a.insert_at(1,4200)


# In[ ]:





# In[ ]:





# In[ ]:




