# https://leetcode.com/problems/subdomain-visit-count/description/


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}

        for domain in cpdomains:
            [numVisits, stringdomain] = domain.split(' ')
            subdomains = stringdomain.split('.')
            for i in range(len(subdomains)):
                key = '.'.join(subdomains[i:len(subdomains)])
                if key in visits:
                    visits[key] += int(numVisits)
                else:
                    visits[key] = int(numVisits)
        
        out = []

        for key in visits:
            out.append(str(visits[key]) + ' ' + key)

        return out