class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ex_t = [0] * n
        stack = []
        for log in logs:
            id_s, start_end_s, timestamp_s = log.split(':')
            id = int(id_s)
            is_start = start_end_s == 'start'
            timestamp = int(timestamp_s)
            if is_start:
                if stack:
                    ex_t[stack[-1][0]] += timestamp - stack[-1][1]
                stack.append([id, timestamp])
            else:
                start_timestamp = stack.pop()[1]
                ex_t[id] += timestamp - start_timestamp + 1
                if stack:
                    stack[-1][1] = timestamp + 1

        return ex_t