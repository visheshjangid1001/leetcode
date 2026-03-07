class Solution:
    def isPalindrome(self,s:str):
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]
    
    
if __name__ == "__main__":
      obj = Solution()
      s = input(s)
      obj.isPalindrome(s)
      
    
   