# Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]
a = [1, 2, 3, 4, 5, 6]
print(a[1:5])

# Check if string palindrome or not “ab”, “abc”, “aba”

def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

a = ["ab", "abc", "aba"]
for input in a:
    if palindrome(input):
        print(f"{input}: it is a palindrome")
    else:
        print(f"{input}: not a palindrome")

# Check if string contains repeated characters “aab”, “abc”, “def”

def check(string):
    repeat = set()
    
    for char in string:
        if char in repeat:
            return True
        repeat.add(char)
        
    return False

a = ["aab", "abc", "def"]
for string in a:
    if check(string):
        print(f"{string}: it has repeated characters")
    else:
        print(f"{string}: it doesn't have repeated characters")

# Convert all the above to a function which can work on a variadic number of arguments

def check_palindrome_and_repeated_characters(*args):
    for string in args:
        palindrome_result = palindrome(string)
        repeated_characters_result = check(string)
        print(f"{string}: Palindrome={palindrome_result}, Repeated Characters={repeated_characters_result}")

check_palindrome_and_repeated_characters("ab", "abc", "aba", "aab", "def")
