class Solution:
    def compress(self, chars: List[str]) -> int:
        i = len(chars) - 1
        while True:
            is_finished = False
            count = 0
            char = chars[i]
            for j in range(i, -1, -1):
                new_char = chars[j]
                if char != new_char:
                    i = j
                    break
                del chars[j]
                count += 1
                if j == 0:
                    is_finished = True
                    i = -1
            if count > 1:
                chars[i+1:i+1] = [char] + list(str(count))
            else:
                chars[i+1:i+1] = [char]
            if is_finished:
                return len(chars)