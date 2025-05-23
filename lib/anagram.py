class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_word = sorted(self.word)
        matches = []

        for w in word_list:
            if sorted(w.lower()) == sorted_word and w.lower() != self.word:
                matches.append(w)

        return matches

