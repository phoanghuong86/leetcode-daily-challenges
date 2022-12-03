class Solution(object):
    def frequencySort(self, s):
        dict_s = {}
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        new_result = ""
        dict_s = sorted(dict_s.items(),key=lambda x : x[1],reverse=True)
        for i in range(len(dict_s)):
            new_result += dict_s[i][0] * dict_s[i][1]
        return new_result
