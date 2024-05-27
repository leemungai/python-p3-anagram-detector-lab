class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        def is_anagram(word1, word2):
            return sorted(word1) == sorted(word2)
        
        match = [word for word in possible_anagrams if is_anagram(self.word, word)]
        return match