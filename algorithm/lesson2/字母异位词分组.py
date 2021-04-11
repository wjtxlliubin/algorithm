class Solution:
    def groupAnagrams(self, strs) :
        ret = []
        d = {}
        for i in strs:
            sort_i = ''.join(sorted(i))
            if sort_i in d:
                ret[d[sort_i]].append(i)
            else:
                d[sort_i] = len(ret)
                ret.append([i])
        return ret

if __name__ == '__main__':
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)