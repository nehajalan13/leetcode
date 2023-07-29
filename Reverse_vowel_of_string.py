"""Date: July 29 2023
Author : Neha Jalan
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Input: s = "hello"
Output: "holle" """

class Solution:
    def reverseVowel(self,s : str) -> str:
        i = 0
        j = len(s)-1
        s = list(s)
        while i<j :
            if self.isVowel(s[i]) and self.isVowel(s[j]):
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
            elif self.isVowel(s[j]):
                i += 1
            elif self.isVowel(s[i]):
                j -= 1
            else:
                i += 1
                j -= 1
        return "".join(s)

    @staticmethod
    def isVowel(char):
        return char.lower() in "aeiou"

def main():
    srr = input("enter a string")
    st = Solution()
    print(st.reverseVowel(srr))

if __name__ == '__main__':
    main()

