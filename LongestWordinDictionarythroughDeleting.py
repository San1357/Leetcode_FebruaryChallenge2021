'''Problem : Longest Word in Dictionary through Deleting'''


#CODE :

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def helper(s,target):
            i = 0
            j = 0
            while i<len(s) and j<len(target):
                if s[i] == target[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            return j==len(target)
               d.sort(key=lambda x: [-len(x),x])
        for c in d:
            if helper(s,c):
                return c
        return ''
