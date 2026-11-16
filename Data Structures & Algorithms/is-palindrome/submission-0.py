class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Replace all letters and numbers with an empty string
        # cleaned_text = s.replace(" ", "").lower()
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(f"Cleaned Text {cleaned_text}")
        n = len(cleaned_text)

        for i in range(int(n/2)):
            if cleaned_text[i] != cleaned_text[n-i-1]:
                return False
        return True
        