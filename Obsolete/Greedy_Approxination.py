# # # #GREEDY APPROXIMATE ALGORITHM FOR FINDING ANY SUPERSTRING

# # # from re import sub
# # # import sys
# # # from string_functions import *


# # # def findSuperStr(arr):

# # #     leng = len(arr)

# # #     while leng != 1:
# # #         Overlap = -sys.maxsize - 1  #max overlap
# # #         #index of strings that are in overlap
# # #         first = 0
# # #         second = 0
# # #         resultStr = ""  #the resulting string

# # #         for i in range(0, leng):
# # #             for j in range(i + 1, leng):
# # #                 [prefix, over, suffix, maxOver
# # #                  ] = overlap(arr[i],
# # #                              arr[j])  #get max overlap of two strings from arr
# # #                 result = prefix + over + suffix

# # #                 if (Overlap < maxOver):  #check for there is new max overlap
# # #                     Overlap = maxOver  #new max overlap
# # #                     resultStr = result  #new resulting string
# # #                     first = i  #first string in overlap is stored
# # #                     second = j  #second string in overlap is stored

# # #         leng = leng - 1  #last string in array will be ignored

# # #         #if there are no overlaps
# # #         if (Overlap == -sys.maxsize - 1):
# # #             arr[0] = arr[0] + arr[leng]
# # #         else:
# # #             arr[first] = resultStr  #first string is now new string
# # #             arr[second] = arr[leng]  #second string will be ignored

# # #     return arr[0]

# # # def overlap(s1, s2):
# # #     """
# # #     Returns the length of the maximum overlap between s1 and s2.
# # #     """
# # #     start = 0
# # #     while True:
# # #         start = s1.find(s2[:start+1], start)
# # #         if start == -1:
# # #             return 0
# # #         if s2.startswith(s1[start:]):
# # #             return len(s1) - start
# # #         start += 1

# # def overlap(s1, s2):
# #     """
# #     Returns the length of the maximum overlap between s1 and s2 in constant time using a hash table.
# #     """
# #     k = min(len(s1), len(s2))
# #     suffixes = {s1[i:]: i for i in range(len(s1))}
# #     prefixes = {s2[:k-i]: i for i in range(k)}
# #     for i in range(k, 0, -1):
# #         if s1.endswith(s2[:i]):
# #             return i
# #         if s2.startswith(s1[-i:]) and s1[-i:] in suffixes:
# #             return i + suffixes[s1[-i:]] - len(s1)
# #         if s1.startswith(s2[-i:]) and s2[-i:] in prefixes:
# #             return i + prefixes[s2[-i:]] - len(s2)
# #     return 0


# # def shortest_superstring(strings):
# #     """
# #     Finds the shortest superstring that contains all the input strings.
# #     """
# #     while len(strings) > 1:
# #         max_overlap = 0
# #         pair = (0, 1)
# #         for i in range(len(strings)):
# #             for j in range(i+1, len(strings)):
# #                 o1 = overlap(strings[i], strings[j])
# #                 o2 = overlap(strings[j], strings[i])
# #                 if o1 > max_overlap:
# #                     max_overlap = o1
# #                     pair = (i, j)
# #                 if o2 > max_overlap:
# #                     max_overlap = o2
# #                     pair = (j, i)
# #         i, j = pair
# #         strings[i] += strings[j][max_overlap:]
# #         del strings[j]
# #     return strings[0]

# import networkx as nx
# from Bio import pairwise2

# def shortest_superstring(strs, k):
#     strings = list(strs)
#     # Build the overlap graph
#     G = nx.DiGraph()
#     for i, s1 in enumerate(strings):
#         for j, s2 in enumerate(strings):
#             if i != j and s1[-k:] == s2[:k]:
#                 G.add_edge(i, j, weight=len(s2)-k+1)

#     # Find the longest path in the graph
#     path = nx.algorithms.dag_longest_path(G, weight='weight')

#     # Handle the case where there is no path
#     if not path:
#         return ''.join(strings)

#     # Merge the strings into a consensus sequence
#     consensus = strings[path[0]]
#     for i in range(1, len(path)):
#         s1 = strings[path[i-1]]
#         s2 = strings[path[i]]
#         overlap = pairwise2.align.globalxx(s1, s2, score_only=True)
#         consensus += s2[overlap:]

#     return consensus

import networkx as nx


def shortest_superstring(strings):
    # Create a suffix tree from the input strings
    t = SuffixTree(strings)
    
    # Create a directed acyclic graph (DAG) where each node represents a string in the suffix tree and each edge represents an overlap
    G = nx.DiGraph()
    for node in t.nodes:
        G.add_node(node)
        for child in node.children:
            G.add_edge(node, child, weight=child.edge_length())
    
    # Find the longest path in the DAG using the Bellman-Ford algorithm
    path = nx.algorithms.dag.longest_path(G)
    
    # Merge the strings in the longest path to create the superstring
    superstring = strings[path[0]]
    for i in range(1, len(path)):
        node1 = path[i-1]
        node2 = path[i]
        edge = t.edges[(node1, node2)]
        superstring += edge.label[edge.depth:]
    
    return superstring


class SuffixTree:
    def __init__(self, strings):
        # Initialize the suffix tree with the input strings
        self.root = Node()
        self.edges = {}
        for i, s in enumerate(strings):
            self.add_string(s, i)
        
    def add_string(self, s, idx):
        # Add a string to the suffix tree
        current_node = self.root
        for i, c in enumerate(s):
            if c not in current_node.children:
                # Create a new edge if the character is not in the children of the current node
                leaf = Node()
                self.edges[(current_node, leaf)] = Edge(i, len(s))
                current_node.children[c] = leaf
            else:
                # Traverse down the existing edge if the character is already in the children of the current node
                leaf = current_node.children[c]
                edge = self.edges[(current_node, leaf)]
                j = edge.start + leaf.depth(current_node)
                while j < edge.end and s[j] == s[i]:
                    j += 1
                    i += 1
                if j == edge.end:
                    # If the entire edge matches the suffix, continue to the next node
                    current_node = leaf
                else:
                    # If only part of the edge matches the suffix, split the edge and add a new leaf
                    split_node = Node()
                    new_leaf = Node()
                    self.edges[(current_node, split_node)] = Edge(edge.start, j)
                    self.edges[(split_node, leaf)] = Edge(j, edge.end)
                    self.edges[(split_node, new_leaf)] = Edge(i, len(s))
                    del self.edges[(current_node, leaf)]
                    split_node.children[edge.label[j]] = leaf
                    current_node.children[c] = split_node
                    leaf.parent = split_node
                    current_node = split_node
        current_node.suffix_index = idx
        
        
class Node:
    def __init__(self):
        self.children = {}
        self.parent = None
        self.suffix_link = None
        self.suffix_index = None
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.children})"
        

class Edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
