#!/usr/bin/env python
# coding: utf-8

# In[139]:



import numpy as np


# In[52]:


def ReadFile(f):
    all_words=[]
    with open(f,"rb") as f:
        for line in f:
            #print(line)
            str2 = line.decode('utf-8')
            str2=str2.rstrip('\n')
            wordsperline=str2.split(" ")
            for i in range(len(wordsperline)):
                all_words.append(wordsperline[i])
   
    return all_words
def CreateSet(words):
    thisset = set()
    for i in range(len(words)):
        thisset.add(words[i])
    return thisset
def CreateDictionary(words):
    my_dict={}
    for i in range(len(words)):
        check=False
        for key,value in my_dict.items():
            if(key==words[i]):
                my_dict[key]= my_dict[key]+1
                check=True
        if(check==False):
            my_dict[words[i]]=1
    return my_dict


# In[53]:


words=ReadFile("C:\\Users\\silla\\OneDrive\\Documents\\Freelance work\\PythonBst\\life_of_brian.txt")
print("original Number of words: ",len(words))
setmade=CreateSet(words)
print("Words in the set: ",len(setmade))
print("---------------------------------------------set------------------------------------------")
print(setmade)
dictmade=CreateDictionary(words)
print("Words in the set: ",len(dictmade))
print("--------------------------------------------Dictionary------------------------------------")
for key,value in dictmade.items():
    print("key: ",key," Value: ",value)


# In[54]:


def SortDictionary(dictmade):
    value_key_pairs = ((value, key) for (key,value) in dictmade.items())
    sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
    return sorted_value_key_pairs
def Top10(listof):
    listapp=[]
    count=0
    for i in range(len(listof)):
        if(len(listof[i][1])>4 and count<10):
            listapp.append(listof[i])
            count+=1
    return listapp
listof=SortDictionary(dictmade)
Top10words=Top10(listof)
print("List of top 10 words in the script Life of Brian: ",Top10words)


# In[ ]:


words=ReadFile("C:\\Users\\silla\\Downloads\\swe_news(1)\\swe_news.txt")
print("original Number of words: ",len(words))
setmade=CreateSet(words)
print("Words in the set: ",len(setmade))
print("---------------------------------------------set------------------------------------------")
print(setmade)
print("---------------------------------------------Top 10 using Dictionary------------------------------------------")
dictmade=CreateDictionary(words)
listofits=SortDictionary(dictmade)
Top10wer=Top10(listofits)
print("List of top 10 words in the script sw_news: ",Top10wer)


# # BST MAP IMPLEMENTATION TO SHOW HOW DICTIONARY WORKS
# .
# .
# .
# .
# .
# .
# .

# In[129]:


from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)
    
    def __init__(self,k,val, pt,rt):
        self.key=k
        self.value=val
        self.left=pt
        self.right=rt
        
    # Insert a node
    def insert(self,node, key,value):

        # Return a new node if the tree is empty
        if node is None:
            return Node(key,value,None,None)

        # Traverse to the right place and insert the node
        if key < node.key:
            node.left = self.insert(node.left, key,value)
        elif key > node.key:
            node.right = self.insert(node.right, key,value)
        else:
            #print(node.key)
            node.value+=1

        return node
    def put(self, key, value):
        self.insert(self,key,value)

    def to_string(self):
        lst=[]
        self.Inorder(self,lst)
        str_app=""
        for i in range(len(lst)):
            str_app+=str(lst[i])
            str_app+=" "
        return str_app  # Placeholder code to avoid crash in demo program. To be replaced

    def count(self):
        lst=[]
        self.Inorder(self,lst)
        return len(lst)      # Placeholder code ==> to be replaced

    def get_it(self,node,key):
        if(node==None):
            return None
        elif node.key==key:
            print("idsjajd")
            return (node.key,node.value)
        if key>node.key:
            pt=node.get_it(node.right,key)
        elif key<node.key:
            pt=node.get_it(node.left,key)
        return pt
        
    def get(self, key):
        pt=self.get_it(self,key)
        return pt

    def maxify(self,node):
        if (node == None):
            return 0
        else :
            # compute the depth of each subtree 
            lDep = self.maxify(node.left)
            rDep = self.maxify(node.right)
  
            if (lDep > rDep):
                return (lDep + 1)
            else:
                return (rDep + 1)
        
    def max_depth(self):
        dep=self.maxify(self)
        return dep
        # Placeholder code ==> to be replaced

    def count_leafs(self):
        count = 0
        if self.left is None and self.right is None:
            count += 1
        if self.left:
            count += self.left.count_leafs() # added count +=
        if self.right:
            count +=self.right.count_leafs() # added count +=

        return count
           # Placeholder code ==> to be replaced

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def Inorder(self,node,lst):
        if node==None:
            return lst
#traverse left subtree
      
        self.Inorder(node.left,lst)
#traverse current node
        stre=(node.key , node.value)
        lst.append(stre)
        
#traverse right subtree
        
        self.Inorder(node.right,lst)  
        
    def as_list(self, lst):
        #print(self.key,"isdh")
        #print(self.left.key,"isdh")
        #print(self.left.left.key,"isdh")
        self.Inorder(self,lst)
        return lst
            # Placeholder code to avoid crash in demo program. To be replaced


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
         
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes 
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)


# In[130]:



# Program starts
# Add pairs
d = {"Ella": 39, "Owen": 40, "Fred": 44, "Zoe": 41, "Adam": 27, "Ceve": 37}
map = BstMap()
for k, v in d.items():
    map.put(k, v)
print(map.to_string())        # { (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print("Size:", map.size())    # 6

# Override existing values
print("\nOverride existing values")
map.put("Zoe", 99)
map.put("Ceve", 100)
print(map.to_string())       # { (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

# get, max_depth, count_leafs
print("\nGet(Fred):", map.get("Fred"))    # 44
print("Get(Jonas):", map.get("Jonas"))  # None
print("Max depth:", map.max_depth())     # 3
print("Count leafs:", map.count_leafs())  # 3

# Check max_depth
map.put("AA", 1)
map.put("AAA", 2)
map.put("AAAA", 3)
map.put("AAAAA", 4)

print("\nSize:", map.size())              # 10
print("Max depth:", map.max_depth())    # 6
print("Count leafs:", map.count_leafs())  # 4
print("To_string: ", map.to_string())    # { (AA,1) (AAA,2) (AAAA,3) (AAAAA,4) (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

# as_list
lst = map.as_list()
print("\nList size and element type:", len(lst), type(lst[0]))  # 10 <class 'tuple'>
print("List content:", lst)  # [('AA', 1), ('AAA', 2), ('AAAA', 3), ('AAAAA', 4), ('Adam', 27), ('Ceve', 100), ('Ella', 39), ('Fred', 44), ('Owen', 40), ('Zoe', 99)]


# In[131]:



lifeofbrian=BstMap()
words=ReadFile("C:\\Users\\silla\\OneDrive\\Documents\\Freelance work\\PythonBst\\life_of_brian.txt")
for i in range(len(words)):
    lifeofbrian.put(words[i],1)
listof=lifeofbrian.as_list()
lister=[]
for i in range(len(listof)):
    if(len(listof[i][0])>4):
        lister.append((listof[i][0],listof[i][1]))

for i in range(len(lister)):
    y=i+1
    while(y<len(lister)):
        if(lister[i][1]<lister[y][1]):
            temp=lister[i]
            lister[i]=lister[y]
            lister[y]=temp
        y=y+1
print("-------------------------------Top 10 words in life of Brian using a BST Map------------------------")        
print((lister[0:10]))
print("depth: ",lifeofbrian.max_depth())
print("leafs: ",lifeofbrian.count_leafs())
print("count of nodes: ",lifeofbrian.size())
#pres=Top10(listof)


# In[132]:


news=BstMap()
words=ReadFile("C:\\Users\\silla\\Downloads\\swe_news(1)\\swe_news.txt")
for i in range(len(words)):
    news.put(words[i],1)
listof=news.as_list()
lister=[]
for i in range(len(listof)):
    if(len(listof[i][0])>4):
        lister.append((listof[i][0],listof[i][1]))

for i in range(len(lister)):
    y=i+1
    while(y<len(lister)):
        if(lister[i][1]<lister[y][1]):
            temp=lister[i]
            lister[i]=lister[y]
            lister[y]=temp
        y=y+1
print("-------------------------------Top 10 words in sw_news using a BST Map-------------------------")        
print((lister[0:10]))
print("depth: ",news.max_depth())
print("leafs: ",news.count_leafs())
print("count of nodes: ",news.size())
#pres=Top10(listof)


# # HashSet Implementation to count the Unique words

# In[133]:


from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 8

    def init(self):
        self.size = 8
        self.buckets = [[] for i in range(8)]
        

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        #compute the value of the word
        sum_w=0
        for i in range(len(word)):
            sum_w+=ord(word[i])
        value=sum_w%self.size    
        return value    # Placeholder code ==> to be replaced

    # Doubles size of bucket list
    def rehash(self):
        check=False
        for i in range(len(self.buckets)):
            if(len(self.buckets[i])==0): #check for some buckets not being filled
                check=True
        if(check==False): #all buckets have been filled
            self.size=self.size*2
            listy=[]
            for i in range(len(self.buckets)):
                for j in range(len(self.buckets[i])):
                    listy.append(self.buckets[i][j])
            self.buckets= [[] for i in range(self.size)]
            for i in range(len(listy)):
                hash_v=self.get_hash(listy[i])
                self.buckets[hash_v].append(listy[i])
        
           # Placeholder code ==> to be replaced

    # Adds a word to set if not already added
    def add(self, word):
        if(not(self.contains(word))): #if the word isnt present in the hash set then add it
            self.rehash()
            hash_v=self.get_hash(word)
            self.buckets[hash_v].append(word)
        # Placeholder code ==> to be replaced

    # Returns a string representation of the set content
    def to_string(self):
        all_Words="{ "
        for i in range(len(self.buckets)):
            for j in range(len(self.buckets[i])):
                all_Words+=self.buckets[i][j]+" "
        all_Words+="}"
        return all_Words    # Placeholder code ==> to be replaced

    # Returns current number of elements in set
    def get_size(self):
        num_ele=0
        for i in range(len(self.buckets)):
            for j in range(len(self.buckets[i])):
                num_ele+=1
        return num_ele
        
         # Placeholder code ==> to be replaced

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hash_v=self.get_hash(word)
        if(self.buckets[hash_v]!=None):
            for i in range(len(self.buckets[hash_v])):
                if(self.buckets[hash_v][i]==word):
                    return True
        return False
        # Placeholder code ==> to be replaced

    # Returns current size of bucket list
    def bucket_list_size(self):
        return self.size
          # Placeholder code ==> to be replaced

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        hash_v=self.get_hash(word)
        for i in range(len(self.buckets[hash_v])):
            if(self.buckets[hash_v][i]==word):
                self.buckets[hash_v].remove(word)
                return True
        return False    # Placeholder code ==> to be replaced

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max_size=0
        for i in range(len(self.buckets)):
            if(len(self.buckets[i])>max_size):
                max_size=len(self.buckets[i])
        return max_size    # Placeholder code ==> to be replaced

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        num_bucks=self.size
        zero_bucks=0
        for i in range(len(self.buckets)):
            if(len(self.buckets[i])==0):
                zero_bucks+=1
        return float(zero_bucks)/float(num_bucks)    # Placeholder code ==> to be replaced


# In[134]:


Hashs=HashSet()
Hashs.init()
Hashs.add("worse")
Hashs.add("worse")
Hashs.add("worse")
Hashs.add("blue")
Hashs.add("red")
print(Hashs.get_size())
print(Hashs.bucket_list_size())
print(Hashs.zero_bucket_ratio())
print(Hashs.max_bucket_size())
print(Hashs.remove("worse"))
print(Hashs.get_size())
print(Hashs.bucket_list_size())
print(Hashs.zero_bucket_ratio())
print(Hashs.max_bucket_size())
print(Hashs.to_string())


# In[135]:


# Program starts

# Initialize word set
words = HashSet()   # Create new empty HashSet
words.init()             # Initialize with eight empty buckets

# Add names to word set. Notice: a) contains duplicate names,
# b) more than eight names ==> will trigger rehash
names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Jonas", "Amer", "David"]
for name in names:
    words.add(name)

print("\nto_string():", words.to_string())  # { Adam David Amer Ceve Owen Ella Jonas Morgan Fredrik Zoe Fred Albin Ola Simon }
print("get_size():", words.get_size())             # 14
print("contains(Fred):", words.contains("Fred"))   # True
print("contains(Bob):", words.contains("Bob"))     # False

# Hash specific data
mx = words.max_bucket_size()
print("\nmax bucket:", mx)                # 2
buckets = words.bucket_list_size()
print("bucket list size:", buckets)     # 16
zero_buckets_ratio = words.zero_bucket_ratio()
print("zero bucket ratio:", round(zero_buckets_ratio, 2))  # 0.38

# Remove elements
delete = ["Ceve", "Adam", "Ceve", "Jonas", "Ola"]
for s in delete:
    words.remove(s)
print("\nget_size:", words.get_size())   # 10
print("to_string():", words.to_string())   # { David Amer Owen Ella Morgan Fredrik Zoe Fred Albin Simon }


# ##  life of brian using Hashset

# In[136]:


lifeofbrian=HashSet()
lifeofbrian.init()
words=ReadFile("C:\\Users\\silla\\OneDrive\\Documents\\Freelance work\\PythonBst\\life_of_brian.txt")
for i in range(len(words)):
    lifeofbrian.add(words[i])
print("to_string: ",lifeofbrian.to_string())
print("get_size: ",lifeofbrian.get_size())
print("zero bucket ratio:: ",lifeofbrian.zero_bucket_ratio())
print("bucket list size: ",lifeofbrian.bucket_list_size())
print("max bucket size: ",lifeofbrian.max_bucket_size())
print("---------------------Number of unique words----------------------------")
print("get_size: ",lifeofbrian.get_size())


# ## sw_news using HashSet

# In[112]:


news=HashSet()
news.init()
words=ReadFile("C:\\Users\\silla\\Downloads\\swe_news(1)\\swe_news.txt")
for i in range(len(words)):
    news.add(words[i])
print("to_string: ",news.to_string())
print("get_size: ",news.get_size())
print("zero bucket ratio:: ",news.zero_bucket_ratio())
print("bucket list size: ",news.bucket_list_size())
print("max bucket size: ",news.max_bucket_size())
print("---------------------Number of unique words----------------------------")
print("get_size: ",news.get_size())


# In[ ]:




