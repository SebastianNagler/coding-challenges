class Solution:
    def simplifyPath(self, path: str) -> str:
        while path != '/' and path[-1] == '/':
            path = path[:-1]
        res = []

        for i in range(len(path)):
            curr_char = path[i]
            if curr_char == '.':
                if i == len(path) - 1 or path[i+1] == '/':
                    if res[-1] == '/':
                        res.pop()
                    elif res[-1] == '.' and res[-2] == '/':
                        res.pop()
                        res.pop()
                        while res and res[-1] != '/':
                            res.pop()
                        if res:
                            res.pop()
                    else:
                        res.append(curr_char)
                    if not res:
                        res = ['/']
                else:
                    res.append(curr_char)
            elif curr_char == '/' and res and res[-1] == '/':
                pass
            else:
                res.append(curr_char)

        return "".join(res)