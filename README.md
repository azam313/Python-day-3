<h1>String</h1>
String is data type that stores a sequence of chaacters.

Basic Operations
* concatination
  "hello" + "world" ---> "helloworld"

* Length of str
  len(str)
-------------------------------------------------------------------------------------------

Indexing
A z a m   S h a i k h
0 1 2 3 4 5 6 7 8 9 10

str = "Azam Shaikh"
str[0] is 'A', str[1] is 'z' ....
str[0] = 'B' #is not allowed
------------------------------------------------------------------------------------------

Slicing
Asccessing parts of a string

str = "AzamShaikh"
str[1:4} is "zam"
str[ :4] is same as str[0:4]
str[1: ] is same as str[1: len(str)]
-----------------------------------------------------------------------------------------

Slicing
Negative Index

A   z  a  m
-4 -3 -2 -1

str = "Azam"
str[-3: -1] is "za"
----------------------------------------------------------------------------------------

String Function

str = "I am a coder."
str.endsWith("er.") #return true if string ends with substr
str.capitalize() #capitalizes 1st char
str.replace(old, new) #replaces all old with new
str.find(word) #return 1st index of 1st occurrence
str.count("am) #counts the occurrence of substr in string
