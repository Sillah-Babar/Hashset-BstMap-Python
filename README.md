# Introduction
The project takes into account the imperability of data analysis when it comes to huge files. In this particular project, the unique word count of a specific file and the frequency of words occuring are taken into account. The Top 10 words are extracted from each file. The statistics itself can help us to analyze the document and the importance of words in the given document. For this task Python has certain inbuilt structures that can help us to compute these values within seconds.

## Sets:
Sets in python is a structure that can hold a list of elements given that it wont add an element that already exists in the set. This particular quality of the set structure can be used to count the number of unique elements in a data file.

## Dictionary:
Another important in built python structure is a dictionary that exists as a list of key , value pairs whereby one key can have many values associated with it. This particular quality of the dictionary can help us compute the frequency of each word occurring , that is each word can be added as a key. If the word occurs again then the value of the word is incremented , thereby maintaining the frequency of the word. We use both these inbuilt structures to compute the unique words and frequency. Above this we also use data structures that we have learnt in our courses to compute the same values. The data strcutures we will be creating is the Binary Search tree which will serve as a dictionary and Hashset which will serve the purpose of the set. The datastructures core goal is to reduce the processing time .

## Hashset
We have created a hash set , where we create a list of lists in which each bucket is a hashed index which stores a number of strings in each bucket. 

## Bst
The bst is created where the strings are used as keys and the value is the frequency of how many times that word has occured in the file. Every time a collision of word occurs the value is incremented.
