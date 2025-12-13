class Solution:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}

    def evalRPN(self, tokens: List[str]) -> int:
        def recursiveEvalRPN():
            nonlocal tokens
            popped_node = tokens.pop()
            if popped_node in self.operators:
                match popped_node:
                    case '+':
                        return recursiveEvalRPN() + recursiveEvalRPN()
                    case '-':
                        return -recursiveEvalRPN() + recursiveEvalRPN()
                    case '*':
                        return recursiveEvalRPN() * recursiveEvalRPN()
                    case '/':
                        denominator = recursiveEvalRPN()
                        numerator = recursiveEvalRPN()
                        val = numerator / denominator
                        return ceil(val) if val < 0 else floor(val)
            else:
                return int(popped_node)

        return recursiveEvalRPN()