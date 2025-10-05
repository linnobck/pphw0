import sys


def find_palindromes(words):
    """
    Given a list of strings, find the ones that are palindromes.

    Palindromes are the same forward as they are backwards, such as "mom" or "racecar".

    If the same word appears more than once, it should only appear once in the output!

    Parameters:
        words: list[str] - List of words to analyze.

    Returns:
        list of words that are palindromes from the given word list, in
        alphabetical order
    """
# initialize empty array for palindromes
    palindromes = []

# loop through given list and check for palindromes
    for i in words: 
        if "".join(reversed(i)) == i:
            # only add non-dublicates to palindrome list
            if i not in palindromes:
                palindromes.append(i)

# sort the palindromes alphabetically
    palindromes = sorted(palindromes)

    return(palindromes)


def main():
    # sys.argv is a list of arguments on the command line
    # sys.argv[0] is always the program's name, so here
    # we are checking if that list only contains one element
    # and if so we print a help message and exit
    if len(sys.argv) == 1:
        print("Usage: python3 palindromes.py <words>")
        sys.exit()
    
    # if there are more than 1 parameters, use the find_palindromes
    # # function to print those that are palindromes
    for pal in find_palindromes(sys.argv[1:]):
        print(pal)

if __name__ == "__main__":
    # this statement ensures that our main function only runs if the program
    # is executed directly, we will discuss this more in class
    main()
