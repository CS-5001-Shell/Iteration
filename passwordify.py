"""
Write a Python program that uses a function passwordify(original: str) -> str to convert a phrase to a version of the phrase that you might use as a password. The function will take as a parameter the original phrase and will return the passwordified phrase as output. The rules for passwordification are as follows:

1. All instances of the character 's' or 'S' will be replaced with '$'
2. All instances of the character 'l' or 'L' will be replaced with 1.
3. All spaces will be replaced with '-'.
4. The word 'two' will be replaced by 2.
5. The word 'ten' will be replaced by 10.
6. The word 'three' will be replaced by 3.
7. The rules must be applied in the order they appear above. 

For full credit, you may NOT use the replace method of String. You may find it
helpful to use the find method.

Example:

input = ""sleeping in a tent"
output = "$1eeping-in-a-10t"
"""

def passwordify(original: str) -> str:
    """Converts the original string into a password where the following are
    replaced with special characters:
       s or S: replaced with $
       l or L: replaced with 1
       space: replaced with -
       two: replaced with 2
       ten: replaced with 10
       three: replaced with 3
    """
    pass

def main():
    pass

if __name__ == '__main__':
    main()