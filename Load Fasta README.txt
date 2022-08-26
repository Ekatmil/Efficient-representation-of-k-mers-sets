Load Fasta file
 
Input: fasta file 
Output: text file

1) read file "one_fasta.fa" and load it into seqs
2) add all sequences of seqs to the list arr
3) (assume k = 31) split each seqence sting such as it has k characters 
4) remove the ramaining strings, where len < k
5) write to file "randomfile.txt"
	- using common Greedy algo find superstring by going through all strings in the list 
