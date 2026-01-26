class Solution:
    def checkValidString(self, s: str) -> bool:
        num_open, num_closed, num_ast, empty_ast, num_ast_left, num_ast_right = 0, 0, 0, 0, 0, 0
        for char in s:
            match char:
                case '(': num_open += 1
                case ')': num_closed += 1
                case '*': num_ast += 1
        if num_open < num_closed:
            if num_ast < num_closed - num_open: return False
            else:
                num_ast_left, empty_ast = divmod(num_ast - num_closed + num_open, 2)
                num_ast_left += num_closed - num_open
        elif num_open > num_closed:
            if num_ast < num_open - num_closed: return False
            else: num_ast_left, empty_ast = divmod(num_ast + num_closed - num_open, 2)
        else: num_ast_left, empty_ast = divmod(num_ast, 2)
        curr_num_open = 0
        for char in s:
            match char:
                case '(': curr_num_open += 1
                case ')':
                    if not curr_num_open: return False
                    curr_num_open -= 1
                case '*':
                    if num_ast_left:
                        num_ast_left -= 1
                        curr_num_open += 1
                    elif empty_ast: empty_ast -= 1
                    else:
                        if not curr_num_open:
                            return False
                        curr_num_open -= 1

        return True