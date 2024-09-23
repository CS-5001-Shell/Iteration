"""
Write a Python program that implements a function count_ing_words() -> int. The function will use a while loop to read words from the user until the user enters 'quit'. Return the number of words the user entered that ended with the characters 'ing'. The last line of the output below would be printed by the main function.

Requirements and Hints:

- Your solution must be case insensitive. The function lower() can be used on a string to convert all of the characters to lower case.
- You will need to use another string function that we have not discussed in class. Refer to the String Methods portion of the Python documentation: https://docs.python.org/3/library/stdtypes.htmlLinks to an external site.

Sample output is as follows. Make sure to test thoroughly!

srollins@ada lab4 % python count_ing_words.py
Enter next word -- use 'quit' to end input: waiting
Enter next word -- use 'quit' to end input: enjoy
Enter next word -- use 'quit' to end input: happy
Enter next word -- use 'quit' to end input: working
Enter next word -- use 'quit' to end input: flying
Enter next word -- use 'quit' to end input: quit
You entered 3 words ending with 'ing'.

Your main function will call the count_ing_words function and print the result.
"""

def count_ing_words() -> int:
    """Prompts the user to enter words one at a time with quit to end input.
    Returns the number of words that the use entered that ended with ing. 
    """
    pass

def main():
    pass

if __name__ == '__main__':
    main()