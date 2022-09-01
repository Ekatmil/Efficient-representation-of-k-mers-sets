from msilib import sequence
from Bio import SeqIO
from pickle import FALSE, TRUE
from re import sub
import sys
from xml.etree.ElementTree import tostring
import time

start_time = time.time()

#Making Graph
class Vertex:
    def __init__ (self, vertex):
        self.vertex = vertex
        self.connected_to={}

    def add_connection(self, neigh, weight=0):
        self.connected_to[neigh]=weight

    def get_connection(self):
        return self.connected_to.keys()

    def get_weight(self, neigh):
        return self.connected_to[neigh]

    def __str__(self):
        return str(self.vertex)     

class Graph:
    def __init__ (self):
        self.vertex = {}
        self.numVertex = 0

    def __iter__ (self):
        return iter(self.vertex.values())

    def add_vertex(self, node):
        self.numVertex += 1
        new_node = Vertex(node)
        self.vertex[node]=new_node
        return new_node

    def add_edge(self, from_node, to_node, weight=0):
        if from_node not in self.vertex:
            self.add_vertex(from_node)
        if to_node not in self.vertex:
            self.add_vertex(to_node)
        self.vertex[from_node].add_connection(self.vertex[to_node], weight)                                 

#find max overlap of two strings
def overlap (str1, str2):
    
     maxOverlap = -sys.maxsize - 1 #default max overlap
     len1 = len(str1)
     len2 = len(str2)
    
     #Str1 is before Str2 in newStr
     for i in range (1, min(len1 +1 , len2 +1 )):
         subStr1 = str1[-i:] #prefix of str1
         subStr2 = str2[0:i] #suffix of str2
         #match
         if (subStr1 == subStr2): 
             if (maxOverlap < i): 
                 maxOverlap = i #new overlap 
                 overlapStr = subStr1
                 #newStr = str1 + str2[-(len2 - i):] #new string 
                 fix_i = i
     if (maxOverlap == -sys.maxsize -1 ):
        return ["", str1+str2, "", 0]
     if len2 == fix_i:
            return [str1[0:len1 - fix_i], overlapStr, "", maxOverlap]
     else:
        return [str1[0:len1 - fix_i], overlapStr, str2[ -(len2 - fix_i):], maxOverlap]



#functuon which outputs neighbour with largest overlap with the input vertex 
def largest_weight (v, arr):
    weight = -1
    neigh = None
    for w in v.get_connection():
        if str(w) not in arr:
            if (weight < v.get_weight(w)[3]): #how long is the overlap
                weight = v.get_weight(w)[3]
                neigh = w
    return [neigh, weight]

#find the shorthest string in array 
def shortest(arr):
    shortestStr = ""
    for i in arr:
        if (shortestStr == ""):
            shortestStr = i
            continue
        if (len(str(i)) < len(shortestStr)):
            shortestStr = i
    return shortestStr


def circle_helper (superStr, node, arr, i, cur_ov, new_ov):
    if (len(arr) == i-1):
        superStr = superStr + new_ov[2]
        return superStr
    else:
        new_node = largest_weight(node, arr)[0]

        #print ("Node to compare with is: ", new_node)
        if (cur_ov == None):
            new_str = str(node)
        else:
            new_ov = overlap(str(node), str(new_node))

            if (len(cur_ov) + new_ov[3] > len (str(node))):
                new_str = overlap(cur_ov, new_ov[1])[2]
                if (new_str == ""):
                    new_str = overlap(cur_ov, str(new_node))[2]
            else:
                    new_str = overlap (cur_ov, str(node))[2]

            #print ("New overlap: ", new_ov)
            #print ("Overlap of overlaps: ", overlap(cur_ov, new_ov[1]) )

        #print ("STRING to add: ", new_str)
        cur_ov = overlap(str(node), str(new_node))[1]
        superStr = superStr + new_str
        arr.append(str(node))
        #print ("Current overlap is: ", cur_ov)
        #print ("New superstr is: ", superStr)
        #print ("Array is: ", arr)
        return (circle_helper (superStr, new_node, arr, i, cur_ov, new_ov))

def circle (node, num):
    ar = list()
    return( circle_helper("", node, ar, num, None, None ))

def findMask (arr, str1):
    for str2 in arr:
        str3 = str1.upper()
        i = str3.find(str2)
        str1 = str1[:i] + str1[i].lower() + str1[i+1:]
    return str1

def changeCaps(str1):
        i = 0
        str2 = ""
        while i < len(str1):
            if str1[i].islower():
                str2 = str2 + str1[i].upper()
                i = i + 1
            else:
                str2 = str2 + str1[i].lower()
                i = i + 1
        return str2



fileName = "C:\\Users\\Ekaterina Milyutina\\Downloads\\test_seq.fa"
seqs = SeqIO.parse(fileName, 'fasta')

arr=[]
for record in seqs:
    arr = arr + list(record.seq)

k = 498602
#double loop -> change 
for i in range (0,len(arr) - k + 1):
    for j in range (i+1,i+k):
        print (i)
        arr[i]+=arr[j]

print (arr)
print (len (arr))
print (len(arr)-k+1)

for i in range (len(arr)-k+1, len(arr)):
    arr.pop()   

arr = list(dict.fromkeys(arr)) #remove duplicates
print (arr)
G = Graph()

for a in arr:
    G.add_vertex(a)

for i in range (0, len(arr)):
     for j in range (i+1,len(arr)):
         G.add_edge(arr[i], arr[j], overlap(arr[i], arr[j]))
         if (i != j):
             G.add_edge(arr[j], arr[i], overlap(arr[j], arr[i]))

all_arr=list()

for v in G:
    #print("-----------")
    #print ("Node is: ", str(v))
    c = circle(v, G.numVertex)
    all_arr.append(c)

superstr = changeCaps(findMask(arr, shortest(all_arr)))

with open("C:\\Users\\Ekaterina Milyutina\\Downloads\\randomfile.txt", "w") as external_file:
    print (superstr, file= external_file) 
    external_file.close()

print ("Time is: ", time.time() - start_time)
