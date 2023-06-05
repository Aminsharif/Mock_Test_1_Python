def firstUniqChar(s):
    char_count = {}
    
    # Count the frequency of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first non-repeating character and return its index
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    # If no non-repeating character is found, return -1
    return -1
  
  
s = "loveleetcode"
print(firstUniqChar(s))

 
