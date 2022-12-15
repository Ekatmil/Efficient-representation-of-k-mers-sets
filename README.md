# README.md

## MAIN
### [main.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/main.py)
``Usage: main.py [-h] [-k K] [-s] [-gh] [-g] [-a] [-b] -i INPUT [-o OUTPUT]``
	
 - -h/--help - help
 - -k K/--kmer K - is the length of each kmer. Not required. Default is k = 31.
 - -s/--simplitig - call for simplitig algorithm. Not required.
 - -gh/--hamiltonian - call for greedyHamiltonian. Not requited. NOTE: not implemented.
 - -g/--greedy - call for GreedyApproximation algorithm. Not requited.
 - -a/--aho-corasick - call for Aho_Corasick algorithm. Not required.
 - -b/--bitstring_mask - mask will be saved in form of 1-0. Not requitred. Default is mask with capital-small letters
 - -i INPUT/--input INPUT - input fasta file. Required
 - -o OUTPUT/--output OUTPUT - output file. Not required. If not givven, then standard output
	
#### Algotithm [main]:
		1) Check if any algorithm is chosen, if not then Error message.
		2) Load Fasta file into the set of kmers
		3) Run chosen algorithm on the set 
		4) Check if bitstring mask is chosen. Apply mask accordingly
		5) Check if output file is chosen. Output accordingly 
		6) Call for Test function 
 **Output**:
 Superstring and its mask as standard output or output file.

### [Load_fasta.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/Load_fasta.py)
***NOTE***: BioPython is required .
Contains function ***def load(k, fileName)***, where *k* is the parsed integer k and *fileName* is INPUT fasta file.
#### Algorithm[Load_fasta]:
		1) Load fasta file with SeqIO into the sequence where each record starts with a “>” line.
		2) For each record in sequence: record is split into kmers 
		3) Add each obtained kmer to the dictionary 
 **Output**:
 Dictionary of kmers obtained from the input fasta file.

### [mask.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/mask.py)
Script for finding the corresponding mask.
Mask provides the position of the original kmers in the superstring.


- [***def findMask(Kset, str1, k)***](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/mask.py#L1), where
  - *Kset* is the set of kmers obrained by Load_fasta.py
  - *str1* is superstring obtained by chosen algorithm
  - *k* is the integer k
 ##### Algorithm [findMask]:
			1) Split superstring into the list of chars l1
			2) For each char in subset of superstring (superstring without last k-1 characters) obtain another substring that starts in the current char and has length of k
			3) If substring is in Kset then the current char is now small char in list l1
			4) End of  for loop (2): convert list l1 into the string
			4) Character is added to the StrMask, which is the superstring together with the mask
			5) StrMask is the string. Switch case for the StrMask
  **Output**:
  Superstring with applied mask, such that characters that represent the beginning of the existing kmer are capital and characters that are not in Kset are small.
			
- [***def findMaskBinary (Kset, str1, k)***](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/mask.py#L1), where
	- *Kset* is the set of kmers obrained by Load_fasta.fa
	- *str1* is superstring obtained by chosen algorithm
	- *k* is the integer k

 ##### Algorithm [findMaskBinary]:
		    1) For loop over each char of the superstring
			2) Obtain substring which starts from the current char and has length k
			3) If substring is in Kset, then append 1 into the list
			4) Append 0 otherwise
			5) End for loop (1): convert list of integers 1-0 into the string StrMask
  **Output**:
  Bitstring that has the same length as Superstring.
	
### [testStr.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/testStr.py)
Script to check the correctness of the output of main.py
	
- [**def allKmers (st, lst)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/testStr.py#L1), where
 - *st* is superstring
 - *lst* is list of kmers 
		
 To check if all kmers are precented in the mask.
 ##### Algorithm [allKmers]:
		1) Helper variables:
			st_helper is superstring with all its characters being capital
			checker is boolian checker for the precense of all kmers in superstring. Set to True
			notFound is a list of all not found kmers
		2) For each kmer find it in the superstring (with capital chars)
		3) If not found, then checker is False and kmer is added into notFound list
		4) If the strating char of the kmer is small letter in the Superstring then print about error in the mask (kmer is precent but mask is not correct)
		5) End of for loop (2): print message according to the checker
			
  **Output**:
   True if all kmers are presented and False otherwise.
		
- [**def noDifferentStr (st, lst, k)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/testStr.py#L22), where
 - *st* is superstring
 - *lst* is list of kmers
 - *k* is integer k
		
 To check if there are no false kmers in the superstring.
  ##### Algorithm [noDifferentStr]:
		1) Set checker to True
		2) For all characters in subset of superstring (superstring without last k - 1 chars) run:
		3) If char is capital, then word is the string stating with char and having length k. Set word to be capitalized
		4) If word is not in list of kmers, then checker is False
		5) End of for loop (2): print message according to the checker
			
- [**def applyMask (st, bn)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/testStr.py#L37), where
 - *st* is superstring
 - *bn* is bitstring
		
 To create superstring with default mask from the bitstring mask.
 ##### Algorithm [applyMask]:
 		Lower all chars of st that are represented by 0 in the bn 
		
  **Output**:
 Superstring with default mask.
			
- [**def testAll (st, lst, k, *bn)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/testStr.py#L48), where
	- *st* is superstring 
	- *lst* is list of kmers
	- *k* is integer k 
	-  **bn* is bitstring. Not Required
		
 To tests everything. Called in main.py.
 ##### Algorithm [testAll]:
		1) Check if bn is given. If given, then applyMask (st, bn)
		2) run allKmers (st, lst)
		3) run noDifferentStr (st, lst, k)
		
  **Output**:
  Messages with the information about correctness of the superstring and its mask.
		


## ALGORITHMS

### [Aho-Corasick](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/literature/A%20Linear-Time%20Algorithm%20for%20Finding%20Approximate%0AShortest%20Common%20Superstrings.pdf)
A Linear-Time Algorithm for Finding Approximate Shortest Common Superstrings.
Called in main.py with algumener -a/--aho-corasick.
	

#### [Automaton_Class.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/Automaton_Class.py)
Creation of the automaton from the given set of word with goto function and fail function.
	
 - [**def goto_function (self)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/Automaton_Class.py#L28)
	Goto function is dictionary in form goto(A,B) : C, where
	 - *A* is start state
	 - *C* is the end state
	 - *B* is the character as a weight of the edge between A and C
			
	##### Algorithm [goto_function]:
			1) Set new_state to be 0 
			2) For kmer in the kmers: state = 0 and j = 0
			3) For character in kmer: result =  goto(state, char)
			4) If result is -1 (fail) then break
			5) State is now result and j is successor of j 
			6) End of for loop (3)
			6) For character in substring of kmer (kmer without first j characters) new_state is successor of new_state; goto(state, char) = new_state and state = new_state
			7) End of for loop (6)
			8) End of for loop (2) 
	Algorithm 2 [page 336](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/literature/Efficient%20String%20Matching:%20An%20Aid%20to%20Bibliographic%20Search.pdf)
	
- [**def fail_function (self)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/Automaton_Class.py#L55)
	Fail function is fictionary in form fail(A) : B, where
	- *A* is current state
	- *B* is state where A is failing
	##### Algorithm [fail_function]:
			1) Store all states which represent the beginning of kmers that are not substrings of anyother kmers, into the queue. All of these states fail to state 0
			2) While queue is not empty take the first state from queue (queue_state)
			3) Check if goto function from this state exists
			4) If exists then append the end state into the queue 
			5) State is the fail from the popped queue_state
			6) While True: goto function (state, ['A', 'C', 'T', 'G']) 
			7) If goto function did not fail, then break 
			8) State is now fail from state 
			9) End of while loop (6)
			10) Fail of goto (queue_state, char) is goto (state, chat)
			11) End of for loop (3) 
			12) End of while loop (2) 
	Algorithm 3 [page 336](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/literature/Efficient%20String%20Matching:%20An%20Aid%20to%20Bibliographic%20Search.pdf)
			
- [**def isLeaf (self, state)**:](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/Automaton_Class.py#L11)
	Function to check if the state is a leaf in automaton.
		
	##### Algorithm [isLeaf]:
		1) For all character ['A', 'C', 'T', 'G'] result = goto (state, char)
		2) if result is not -1 (fail) then return False
		3) End of for loop (1). Return True
		
	**Output**:
	 True if state is leaf and False o/w.
	 
#### [AhoCorasick.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/AhoCorasick.py)
Algorithm that finds the shortest superstring using Aho-Corasick machine.
	
 ##### [PREPROCESSING](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/AhoCorasick.py#L12)
 Algorithm 1 [page 319](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/literature/A%20Linear-Time%20Algorithm%20for%20Finding%20Approximate%0AShortest%20Common%20Superstrings.pdf)
 
 **def preprocessing (kmers, automaton),** where
	- *kmers* is list of kmers 
	- *automaton* is Aho-Corasick machine created from kmers
		
 Is a preprocessing phase that augments the usual AC machine with the necessary additional functions.
		
**Output**:
 -  *list_L* : dictionary of the supporters for each state. In form a:b, where
	- *a* is state 
	- *b* is a list of indeces of words which have path through the state *a*
 -  *link_B* : dictionary which represents the linked list. Reversed breadth-first ordering of the states. For each state *s*, this is represented by a link *b(s)* giving the successor of s in this order
 - *pointer_B* : integer, that gives the first state in this chain
 - *state_F* : dictionary in form a:b, where
	- *a* is index of word in the set 
	- *b* is finit state of the word 

##### [HAMILTONIAN](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/AhoCorasick.py#L67) 
Algorithm 2 [page 320](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/literature/A%20Linear-Time%20Algorithm%20for%20Finding%20Approximate%0AShortest%20Common%20Superstrings.pdf)

**def hamiltonian (list_L, link_B, pointer_B, state_F, automaton, m)**, where
- *list_L* : dictionary, obtained from preprocessing 	
- *link_B*: dictionary, obtained from preprocessing 
- *pointer_B* : integer, obtained from preprocessing 
- *state_F* : dictionary, obtained from preprocessing 
- *automaton* : Aho-Corasick machine created from kmers
- *m* : length of the kmers list 
		
 Function implements the actual greedy heuristics. Construction of *H* path.
**Output**:
	A Hamiltonian path H is the overlap string of reduced kmers set.
			 
##### [FINDING SUPERSTRING](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/AhoCorasick.py#L137) 
Three functions which provide the output superstring.
		
 - **def initialization (a)**, which takes list a of kmers
	###### Algorithm [initialization]:
		1) Create Aho-Corasick machine
		2) Run preprocessing
		3) Run hamiltonian
	**Output**:
	Path H (output of def hamiltomian).
		
- **def SuperStrhelper (a, sorted_list)**, where *a* is list of kmers and sorted_list obtained from HamiltonianSort function (HelperFunction_Automaton.py) and is list of ordered strings from *H*.
		
	###### Algorithm [SuperStrhelper]:
		1) For each string in sorted_list (not including the last one) overlap with the successor string using overlap function (string_functions.py)
		2) Get the merge string of two strings 
		3) Change the second taken string in the kmers to the merge string 
		4) End of for loop (1)
				
	**Output**:
	Superstring.
		
- **def FindSuperStr (arr)**, where *arr* is set of kmers
	This function is called from main.py
			
	###### Algorithm [FindSuperStr]:
		1) Set arr into list 
		2) Obtain sorted_list by HamiltonianSort(initialization( list(arr)))
		3) Obtain resultStr by SuperStrhelper (list(arr), sorted_list) 
	**Output**:
	Superstring
				
		
 ### Greedy
 Greddy Algorithm to find any superstring from given set of kmers.
 Called in main.py with algumener -g/--greedy.
	
##### [GreedyApproximation.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/Greedy_Approxination.py)
Contains function finsSuperStr(arr), which takes the set *arr*, obtained from the compute_simplitig(kmerSet, k) (simplitig.py)
	
###### Algorithm [findSuperStr]:
	1) While length of the arr is not 1
	2) Set Overlap to be minimum and set variables first and second to be 0 (they are indices of strings in overlap)
	3) For each string str1 in arr find overlap with str2, such that str2 under larger index in arr than str1
	4) If their overlap is larger than Overlap (setted before) then Overlap is new overlap; resulted overlap strings added to the resulting superstring; first = i and so first string in overlap is strored; second = j and so the second string in overlap is stored
	5) End of for loop (3). Reduce the length of arr
	6) If there are no overlaps then set arr[0] to be arr[0] + arr[leng]
	7) Else arr[first] is now resulting superstring and arr[second] is arr[leng] and will be now ignored
	8) End of while loop (1)
		
 **Output**: 
	The first element of *arr* which is superstring.

### [Simplitig](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/literature/Simplitigs%20as%20an%20efficient%20and%20scalable%0Arepresentation%20of%20de%20Bruijn%20graphs.pdf)


## HELPER FUNCTIONS

### [HelperFunction_Automaton.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/HelperFunction_Automaton.py)
 Helper Functions for the AhoCorasick.py
 
- [**def addMultipleValues (dict, key, value)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/HelperFunction_Automaton.py#L2) 
	Function to store multiple values with one key (for example, list_L).
	Takes dictionary, key and value.
	#### Algorithm [addMultipleValues]:
		1) If key is not in dictionary then add key to dictionary with empty list as value
		2) If type of input values is list, then append each element to the list corresponding to key 
		3) Else add value to the list corresponding to the key
	**Output**: 
	Dictionary.
	
- [**def sortDict (dict)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/HelperFunction_Automaton.py#L14)  
	Function to sort dictionary by key in reverse order.
	Takes dictionary as input. 
	Returns sorted dictionary. 
	***NOTE***: not used. 
	
- [**def initializeForbidden (dict, m)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/HelperFunction_Automaton.py#L22) 
	Helper function for def HamiltonianSort.
	Stores False value to every key in dictionary. 
	Returns dictionary.
		
- [**def HamiltonianSort (H)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/HelperFunction_Automaton.py#L54) 
	Input: Hamiltonian path *H*.
	Function sorts Hamiltonian path according to merge order of strings.  
	Used in AhoCorasick.py def FindSuperStr.
		
  ##### Algorithm [HamiltonianSort]:
		1) Set values:
			sorted_list : empty list
			pair : first key-value pair from H
			saved : the key of the pair 
			to_add : the value of the pair
		2) Add saved and to_add into the sorted_list and remove pair from the H
		3) While H is not empty:
		4) If there is pair in H such that to_add is key and its value is to_add_helper then add to sorted_list new obtained value, delete from the H this pair and set to_add to be to_add_helper
		5) Else: 
		6) Set still_going to False. It is indicator that we can still follow the path (kmers still overlap)
		7) Find such a key in H pair, that its value is equal to the saved (first taken key). Insert found key into the sorted_list such that it is in front of element saved
		8) Set saved to be new key and delete pair from H 
		9) Set still_going to True and break 
		10) End of for loop (6) 
		11) If still-going is False then there is only new path and repeat steps 1 and 2 (without creating of new sorted_list)
		12) End of else (5)
		13) End of while loop (3)
			
 **Output**:
	Sorted list.
### [string_functions.py](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/772d5909407619f60cda4c5ccce04437798a898b/main/string_functions.py)
Script with overlap functions.
	
- [**def overlap (str1, str2)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/string_function.py#L4), where *str1* and *str2* are two strings. 
		
	THE ORDER OF STRINGS IN INPUT IS IMPORTANT.
		
	##### Algorithm [overlap]:
		1) Set maxOverlap to minimum
		2) For loop over i in range (min(len1 + 1, len2 + 1), 0, -1)
		3) Get prefix of str1 and suffix of str2 of length i 
		4) If prefix is equal to suffix, then check if current i is larger than maxOverlap 
		5) If True then set maxOverlap to i and fix i 
		6) End of for loop (2)
		7) Output according to one of the possible situations:
			a) strings do not have overlap 
			b) str2 is substring of str1 
			c) o/w
		
	**Output**:
	List [prefix, overlap, suffix, maxOverlap], where
	- *prefix* + *overlap* + *suffix* is the overlaped string of *str1* and *str2*
	- *prefix* + *overlap* = *str1*
	- *overlap* + *suffix* = *str2*
	- *maxOverlap* is integer, len(overlap)
				
- [**def betterOverlap (str1, str2)**](https://github.com/Ekatmil/Efficient-representation-of-k-mers-sets/blob/main/main/string_function.py#L31)
	THE ORDER OF THE STRINGS IN INPUT IS NOT IMPORTANT
	
	##### Algorithm [betterOverlap]:
		Function calls overlap(str1, str2) and overlap(str2, str1) and compares their maxOverlap in order to choose the larger one
		
	**Output**:
	Result of overlap (str1, str2) is its larger of equal then overlap (str2, str1) and reslut of overlap (str2, str1) o/w


