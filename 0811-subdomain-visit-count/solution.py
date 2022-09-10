# 09/10/2022 14:13	Accepted	54 ms	14.1 MB	python3
# over-complex solution using a tree lol
class Solution:
    
    def visit(tree, base_domain, counts):
        counts.append([base_domain, tree['count']])
        for child in tree['children'].keys():
            Solution.visit(tree['children'][child], f'{child}.{base_domain}', counts)
    
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        roots = {}
        for cpdomain in cpdomains:
            count, domain_str = cpdomain.split(" ")
            domain = list(reversed(domain_str.split(".")))
            
            count = int(count)
            
            node = roots
            while len(domain) > 0:
                el = domain.pop(0)
                if el not in node:
                    node[el] = {'count': 0, 'children': {}}
                node[el]['count'] += count
                node = node[el]['children']
        output = []
        for root in roots.keys():
            Solution.visit(roots[root], root, output)
            
        return [f'{x[1]} {x[0]}' for x in output]
