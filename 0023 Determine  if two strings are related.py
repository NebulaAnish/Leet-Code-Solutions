# - Make a dictionary storing number of occurrence of both word1 and word2.
# - Make a list of each counts.
# - Make sure number of occurrences are same. Eg,
#     - word1: {1,2,2,1} and {2,1,2,1} here 2 occurs 2 times and 1 occurs 2 times, so the above operations can be done these two words to obtain one another.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2):
            return False
        lettersOfFirstWord = {}
        lettersOfSecondWord ={}

        # Keep counts of each letter occurences
        for letter in word1:
            if letter not in lettersOfFirstWord:
                lettersOfFirstWord[letter]=0
            lettersOfFirstWord[letter]+=1

        for letter in word2:
            if letter not in lettersOfSecondWord:
                lettersOfSecondWord[letter]=0
            # else:
            lettersOfSecondWord[letter]+=1

        # Check if any character is swappable
        countOfLetters1 =[]
        for key in lettersOfFirstWord:
            countOfLetters1.append(lettersOfFirstWord[key])
        countOfLetters2 =[]
        for key in lettersOfSecondWord:
            countOfLetters2.append(lettersOfSecondWord[key])
        
        for i in countOfLetters1:
            if i not in countOfLetters2:
                return False
            countOfLetters2.remove(i)

        for letter in word2:
            if letter not in lettersOfFirstWord:
                return False
        for letter in word1:
            if letter not in lettersOfSecondWord:
                return False
        print(lettersOfFirstWord, lettersOfSecondWord)
        return True