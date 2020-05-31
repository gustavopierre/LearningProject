def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


word1 ='roma'
word2 = 'omir'

print(is_anagram(word1, word2))
