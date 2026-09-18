class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            #as list is mutable and hashmaps cannot be mutable, we use tuple.
            sorted_word = tuple(sorted(word))

            if sorted_word in dic:
                dic[sorted_word].append(word)
            else:
                dic[sorted_word] = [word]
        return list(dic.values())