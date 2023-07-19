class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] == node:
            return node
        grandParent = self.find(self.parent[node])
        self.parent[node] = grandParent
        return grandParent
        
    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1 
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2 
            self.size[parent2] += self.size[parent1] 

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]: 

        emailToAccount = {} # email -> Account index
        uf = UnionFind(len(accounts))

        for i, emails in enumerate(accounts):
            for e in emails[1:]:
                if e in emailToAccount:
                    uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i

        emailGroup = defaultdict(list) # index of Account -> List of emails
        for email, idx in emailToAccount.items():
            emailGroup[uf.find(idx)].append(email)

        ans = []
        for i, emails in emailGroup.items():
            ans.append([accounts[i][0]] + sorted(emails))

        return ans