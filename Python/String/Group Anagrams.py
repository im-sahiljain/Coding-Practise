from collections import defaultdict
def group_anagrams(strs):
    anagram_dict = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] = anagram_dict[sorted_word] + [word]

        else:
            anagram_dict[sorted_word] = [word]

    return list(anagram_dict.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))