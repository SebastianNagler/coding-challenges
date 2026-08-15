class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for path in paths:
            dir, files = path.split()[0], path.split()[1:]
            for file in files:
                i, j = file.find('('), file.find(')')
                content = file[i+1:j]
                name = file[:i]
                dd[content].append(dir + '/' + name)

        return [dd[key] for key in dd if len(dd[key]) > 1]