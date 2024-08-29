class Anagram:
    def __init__(self, word):
        self.word = word
        self.word_sorted = ''.join(sorted(word.lower()))
    
    def match(self, candidates):
        anagrams = []
        for candidate in candidates:
            if self.is_anagram(candidate):
                anagrams.append(candidate)
        return anagrams
    
    def is_anagram(self, candidate):
        if self.word.lower() == candidate.lower():
            return False
        candidate_sorted = ''.join(sorted(candidate.lower()))
        return self.word_sorted == candidate_sorted