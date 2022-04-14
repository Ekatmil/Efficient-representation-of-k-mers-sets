# Brief project specification

The goal of this project is to experimentally evaluate the use of approximation algorithms for the shortest superstring problem (SSP) for representing a set of k-mers (substrings of length k obtained from a DNA sequence). Apart from the superstring, each algorithm will also output a mask, based on which the k-mers can be decoded (to avoid false positives, i.e., substrings of length k that do not belong to the original set). This representation (superstring + mask) will be stored in a file in a bit-efficient way (that is, the aim will be to make the file as small as possible). The student will compare the outcomes from a few approximation algorithms for SSP with the current state-of-the-art methods, most notably simplitigs, on sets of k-mers corresponding to real genomic sequences. 

## Technicalities

- The chosen programming language is Python.

- The suggested algorithms for SSP to implement are Greedy and TGreedy. Later, depending on the outcomes of these two algorithms, we will consider implementing more approximation algorithms for SSP, namely, a more sophisticated algorithm based on an approximation algorithm for Maximum Asymmetric Traveling Salesman problems.

- The implementations may assume that all strings on input have length k and that the alphabet has only four characters, which may help to get a more efficient implementation.

- In addition to the superstring, the algorithms should output a mask, that will determine where the original strings on input start (that is, which substrings of length k correspond to k-mers). Eventually, the student will test more ways to store the mask.

- It will be needed to learn the file formats for k-mers or DNA sequences. [Brinda's paper on simplitigs](https://link.springer.com/article/10.1186/s13059-021-02297-z) may be helpful.