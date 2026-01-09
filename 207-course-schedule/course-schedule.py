import graphlib
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        try:
            graph = {course: set() for course in range(numCourses)}
            for course, prereq in prerequisites:
                graph[course].add(prereq)
            order = list(graphlib.TopologicalSorter(graph).static_order())
        except graphlib.CycleError:
            return False
        return True
        """

        indeg, stack, source_to_target = [0] * numCourses, [], {prereq: [] for prereq in range(numCourses)}
        for course, prereq in prerequisites:
            indeg[course] += 1
            source_to_target[prereq].append(course)
        
        for course in range(numCourses):
            if indeg[course] == 0:
                stack.append(course)

        nr = 0
        while stack:
            popped_course = stack.pop()
            nr += 1
            for next_course in source_to_target[popped_course]:
                indeg[next_course] -= 1
                if indeg[next_course] == 0:
                    stack.append(next_course)

        return nr == numCourses