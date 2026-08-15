class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local.split('+', 1)[0]
            if '.' in local:
                local = local.translate(str.maketrans('', '', '.'))
            addr = local + '@' + domain
            if addr not in emails_set:
                emails_set.add(addr)

        return len(emails_set)
 