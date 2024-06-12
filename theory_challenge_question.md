

# 3.1 Design a basic hash function, keeping in mind memory constraints and how you deal with has collisions 

I would create a function that would take the input string to be hashed. 
For each character in this string, it would convert it to its DEC number. 
It would multiply its DEC number with the characters index in the string. 
It would then add up this value for each character, creating a 'unique' ID. 
This ID would be added to a dictionary (hash table) as the key. The value would be set as a list and the input string appended as a value. 
We would use chaining to manage hash collisions, by appending each value for a key to a list. 
While it would be more efficient from a time complexity perspective to use a linked list, rather than a normal array, given 
the potential memory constraints, an array would be more memory efficient (as a linked list requires space for each item plus a pointer to the next item). 


# 3.2 Walkthrough your function with an example where there is no hash collision 

* For example, if the input string was "helo123". 
* The function would be called with the input string provided as an argument 
* id value would be set as 0 
* Each character in the string would be iterated through, and the Ord() function (or language equivalent) would be used to convert it to its integer value
* This would be multiplied by the index of that value in the string.
* This would be added to the id value for each iteration
* In our example, this would be 1402
* Once finished, the id variable will now represent a 'unique' id. 
* This id will now be added to the hash table 
* First, the function will check if it is already present in the hash table 
* If not, it will add the id as a new key, and set the value as an array. It would then add the input string to the array.
* For example { 1402 : ['helo123'] }
* Depending on operational context, the function would then return either the id alone, hash table or neither. 


# 3.3 Walkthrough your function with an example of a hash collision 

* For example, if the input string was "telo123". 
* The function would be called with the input string provided as an argument 
* id value would be set as 0 
* Each character in the string would be iterated through, and the Ord() function (or language equivalent) would be used to convert it to its integer value, which would be added to the id variable
* In our example, this would be 1402. The same as for our previous example... 
* Once finished, the id variable will now represent a 'unique' id. 
* This id will now be added to the hash table
* The function will check if it is already present as a key in the table
* In this case it is. 
* So instead, the function would it would append the input string to the list already present as the key's value
* For example { 1402 : ['helo123', 'telo123'] }
* Depending on operational context, the function would then return either the id alone, hash table or neither. 


