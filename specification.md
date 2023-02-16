# Brief project specification

The goal of this project is to experimentally evaluate the use of approximation algorithms for the shortest superstring problem (SSP) for representing a set of k-mers (substrings of length k obtained from a DNA sequence). For simplicity, we will consider the unidirectional model, in which a k-mer and its [reverse complement](https://www.bioinformatics.org/sms/rev_comp.html) are *not* considered equivalent. Apart from the superstring, each algorithm will also output a mask, based on which the k-mers can be decoded (to avoid false positives, i.e., substrings of length k that do not belong to the original set). This representation (superstring + mask) will be stored in a file in a bit-efficient way (that is, the aim will be to make the file as small as possible). The student will compare the outcomes from a few well-known approximation algorithms for SSP with the current state-of-the-art methods, most notably simplitigs, on sets of k-mers corresponding to real genomic sequences. 

Specifically, the goals are:

- To develop linear-time implementations of Greedy (using [Ukkonen's paper](https://link.springer.com/article/10.1007/BF01840391), TGreedy, and simplitigs (using [Brinda's paper on simplitigs](https://link.springer.com/article/10.1186/s13059-021-02297-z)). For TGreedy,a linear-time implementation has not been described yet (up to my best knowledge). Time linear in the number of k-mers is basically needed due to large data size; on the other hand, the value of k will be small, at most 20 or so (this is sufficient for bacterial and viral genomes).
- To experimentally compare superstrings and masks output by the three algorithms on bacterial and viral genome datasets. Various properties will be compared (depending on the chosen algorithm, the value of *k*, and the underlying genome): the length of the superstring, the computation time and memory requirements, the size of the whole representation when compressed using a standard tool like `xz`.

## Technicalities

- The chosen programming language is Python.

- The suggested algorithms for SSP to implement are Greedy and TGreedy. Later, depending on the outcomes of these two algorithms, we will consider implementing more approximation algorithms for SSP, namely, a more sophisticated algorithm based on an approximation algorithm for Maximum Asymmetric Traveling Salesman problems.

- The implementations may assume that all strings on input have length k and that the alphabet has only four characters, which may help to get a more efficient implementation.

- In addition to the superstring, the algorithms should output a mask, that will determine where the original strings on input start (that is, which substrings of length k correspond to k-mers). Eventually, the student will test more ways to store the mask.

- It will be needed to learn the file formats for k-mers or DNA sequences. [Brinda's paper on simplitigs](https://link.springer.com/article/10.1186/s13059-021-02297-z) may be helpful.
