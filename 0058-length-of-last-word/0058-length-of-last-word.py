class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        val = 0
        count = 0
        val1 = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i] == " "):
                pass
            else:
                val = s[i]
                val1 = i
                break
      
    
        for j in range(val1,-1,-1):
            if(s[j] != " "):
                count = count+1
            else:
                break
                
        return count