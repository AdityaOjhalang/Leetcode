class Solution:
    def compress(self, chars: List[str]) -> int:
        w = r = 0
        n = len(chars)

        while r < n:
            curr = chars[r]
            count = 0
            
            while r < n and chars[r] == curr:
                count += 1
                r += 1
            
            chars[w] = curr
            w += 1

            if count > 1:
                for char in str(count):
                    chars[w] = char
                    w += 1
        
        return w 