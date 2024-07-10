<h1>String</h1>
<p>String is data type that stores a sequence of chaacters.</p>

<h2>Basic Operations</h2>
<h3>* concatination</h3>
  <p>"hello" + "world" ---> "helloworld"</p>

<h3>* Length of str</h3>
  <p>len(str)</p>
  <hr>

<h1>Indexing</h1>
<p>A z a m   S h a i k h</p>
<P>0 1 2 3 4 5 6 7 8 9 </P>

<p>str = "Azam Shaikh"</p>
<p>str[0] is 'A', str[1] is 'z' ....</p>
<p>str[0] = 'B' #is not allowed</p>
<hr>

<h1>Slicing<h1>
<p>Asccessing parts of a string</p>

<p>str = "AzamShaikh"</p>
<p>str[1:4} is "zam"</p>
<p>str[ :4] is same as str[0:4]</p>
<p>str[1: ] is same as str[1: len(str)]</p>
<hr>

<h1>Slicing</h1>
<p>Negative Index</p>

<p>A   z  a  m</p>
<p>-4 -3 -2 -1</p>

<p>str = "Azam"</p>
<p>str[-3: -1] is "za"</p>
<hr>

<h1>String Function</h1>

<p>str = "I am a coder."
str.endsWith("er.") #return true if string ends with substr<br>
str.capitalize() #capitalizes 1st char<br>
str.replace(old, new) #replaces all old with new<br>
str.find(word) #return 1st index of 1st occurrence<br>
str.count("am) #counts the occurrence of substr in string</p>
