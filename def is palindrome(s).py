def is palindrome(s):
            return s==s[::-1]
s="india"
ans=isPalindrome(s)
if ans:
       print("yes")
else:
       print("no")