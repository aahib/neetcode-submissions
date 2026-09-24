class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(left < right):

            #data cleaning(Removing spaces and special characters)
            if not s[left].isalnum():
                left = left + 1
                continue
            if not s[right].isalnum():
                right = right - 1
                continue

            #Condition to check strings from both sides
            if s[left].lower() != s[right].lower():
                return False

            #increament in left pointer
            left += 1
            #decreament in right pointer
            right -= 1
        return True