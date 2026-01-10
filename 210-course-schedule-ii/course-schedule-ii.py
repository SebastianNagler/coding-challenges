class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res, indeg, stack, source_to_target = [], [0] * numCourses, [], {prereq: [] for prereq in range(numCourses)}
        for course, prereq in prerequisites:
            indeg[course] += 1
            source_to_target[prereq].append(course)
        
        for course in range(numCourses):
            if indeg[course] == 0:
                stack.append(course)

        nr = 0
        while stack:
            popped_course = stack.pop()
            res.append(popped_course)
            nr += 1
            for next_course in source_to_target[popped_course]:
                indeg[next_course] -= 1
                if indeg[next_course] == 0:
                    stack.append(next_course)

        return res if nr == numCourses else []