class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cpdomain in cpdomains:
            num_s, domain = cpdomain.split()
            num = int(num_s)
            while True:
                if domain in counts:
                    counts[domain] += num
                else:
                    counts[domain] = num
                if '.' not in domain:
                    break
                domain = domain.split('.', 1)[1]

        res = []
        for d in counts:
            res.append(str(counts[d]) + ' ' + d)

        return res