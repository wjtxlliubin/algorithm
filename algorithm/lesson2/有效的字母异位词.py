class Solution:
    def isAnagram(self, s: str, t: str):
        from collections import Counter
        s_dict = Counter(s)
        t_dict = Counter(t)
        return s_dict == t_dict

if __name__ == '__main__':
    result = Solution().isAnagram("anagram","nagaram")
    print(result) 