class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        while idx < len(s):
            # Find the position of the next delimiter '#'
            j = idx
            while s[j] != "#":
                j += 1
            
            # Extract the length of the string
            word_len = int(s[idx:j])
            
            # Extract the word based on the length
            word = s[j + 1 : j + 1 + word_len]
            decoded.append(word)
            
            # Move idx to the start of the next encoded segment
            idx = j + 1 + word_len
        return decoded