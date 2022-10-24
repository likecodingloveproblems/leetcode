class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters = list(pattern)
        words = s.split()
        if len(words) != len(letters):
            return False
        letter_2_word = dict()
        word_set = set()

        for letter, word in zip(letters, words):
            if letter_2_word.get(letter, False):
                if letter_2_word[letter] != word:
                    return False
            elif word in word_set:
                return False
            else:
                letter_2_word[letter] = word
                word_set.add(word)
        return True


pattern, s = "abba", "dog cat cat fish"
pattern, s = "abba", "dog cat cat dog"
pattern, s = "aaaa", "dog cat cat dog"
pattern, s = "abba", "dog dog dog dog"
r = Solution().wordPattern(pattern, s)
print(r)
