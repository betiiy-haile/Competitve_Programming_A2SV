class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x)) 
        word_chain_lengths = {}  
        
        for word in words:
            word_chain_lengths[word] = 1

            for j in range(len(word)):
                new_word = word[:j] + word[j + 1:]  
                if new_word in word_chain_lengths and word_chain_lengths[new_word] + 1 > word_chain_lengths[word]:
                    word_chain_lengths[word] = word_chain_lengths[new_word] + 1

        return max(word_chain_lengths.values())
        