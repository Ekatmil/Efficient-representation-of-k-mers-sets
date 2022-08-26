TGREEDY:
1) classes Vertex and Graph are created
2) function ovelap takes two strings and outputs in format: [a, b, c, i], where
	a - 1st string without the overlaped part
	b - overlap
	c - 2nd string without the overlaped part
	i - length of the overlap
3) get the list of strings. Create graph G, where vertices are strings of list and between each of them is directed weighted edge, where weight is overlap information
4) function largest_weight takes one vertex and its neighbours and outputs neighbour with the largest overlap with the current vertex
5) function circle:
	Input:
		a) superStr - superstring 
		b) node - current vertex
		c) arr - list of used verices
		d) i - number of verices of the graph 
		c) cur_ov - overlap[1] of the previous two vertices
		d) new_ov - overlap of current two vertices
	Algorithm:
		a) if all vertices are used in the path, then stop
		b) new_node is a adjacent to the current node vertex with the largest overlap
		c) if current node is the starting vertex, then new string is the vertex itself
		d) else get new overlap and new string is overlap of previous overlap and new overlap 
		e) new_ov[2] is now current overlap (cur_ov)
		f) get new superstring by addition to the initial superstring new string
		g) add to arr used vertex
		h) recursively repeat function
	Output:
		super string for the current node
6) for all vertices of the G run circle function. Add results to the list all_arr
7) output the shortest string from the all_arr  