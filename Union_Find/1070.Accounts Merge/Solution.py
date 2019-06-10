from collections import defaultdict


class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        merged = []

        if not accounts or len(accounts) == 0:
            return merged


        self.forward_index = self.create_forward_index(accounts)
        self.inverted_index = self.create_inverted_index(accounts)

        self.parents = {i : i for i in range(len(accounts)) if len(accounts[i]) >= 1}

        for email, people in self.inverted_index.items():
            if len(people) > 1:
                p1 = people[0]
                for i in range(1, len(people)):
                    self.connect(p1, people[i])

        curr = None
        for people, email in self.forward_index.items():
            if len(email) > 0:
                curr = []
                curr.append(accounts[people][0])
                curr.extend(sorted(list(set(email))))
                merged.append(curr)

        return merged


    def create_forward_index(self, accounts):
        forward_index = defaultdict(list)

        for idx, account in enumerate(accounts):
            forward_index[idx].extend(account[1:])

        return forward_index

    def create_inverted_index(self, accounts):
        inverted_index = defaultdict(list)
        for idx, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                inverted_index[email].append(idx)

        return inverted_index


    def connect(self, p1, p2):
        parent1 = self.find(p1)
        parent2 = self.find(p2)
        if parent2 != parent1:
            self.parents[parent1] = parent2
            self.forward_index[parent2].extend(self.forward_index[parent1])
            self.forward_index[parent1] = []


    def find(self, p):
        path = []
        while p != self.parents[p]:
            path.append(p)
            p = self.parents[p]

        for ppl in path:
            self.parents[ppl] = p

        return p