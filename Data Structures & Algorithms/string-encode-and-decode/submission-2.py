class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
            

    def decode(self, s: str) -> List[str]:
        # decoding - use two-pointer method
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j].isdigit():
                j += 1
            cur_length = int(s[i:j])
            cur_word = ""
            start = j + 1
            end = j + 1 + cur_length
            for c in range(start, end):
                cur_word += s[c]
            decoded_strs.append(cur_word)
            i = end
        return decoded_strs