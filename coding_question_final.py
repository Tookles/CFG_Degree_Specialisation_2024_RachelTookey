# 2.1:

def unique(input_string):
    vowels = "aeoiu"
    clean_string = input_string.lower()
    x = [i for i in clean_string if clean_string.count(i) == 1 and i not in vowels]
    return len(x)

print(unique('cCataract'))


"""
The time complexity of this is O(n^2) 
This is because the list comprehension loops through the string (complexity: O(n)), and within that, the count method acts as a nested loops and searches through the string again (complexity O(n). 
This means the complexity is O(n * n). 
"i not in vowels", and len(x) are both complexity o(1).
The method .lower() also loops through the string O(n).
This creates O(n + n^2 + 1 + 1) 
And so, as O captures the most time consuming part of the operation, n and 2 are dropped and the final answer is O(n^2).


The space complexity is O(n) because we are creating a list 'x' that stores the unique consonants. 
The size of this will vary with the length of the input string, and so is O(n).

"""

# 2.2: Write a function that finds how many squares are in an X by X grid

def squares(side):
    if side == 1:
        return side*side
    return squares(side-1) + side*side

print(squares(4))


