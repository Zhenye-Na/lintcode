# 1070. Accounts Merge

**Description**

Given a list `accounts`, each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in *sorted* order. The accounts themselves can be returned in any order.

- The length of accounts will be in the range `[1, 1000]`.
- The length of `accounts[i]` will be in the range `[1, 10]`.
- The length of `accounts[i][j]` will be in the range `[1, 30]`.

**Example**

```
Example 1:
	Input:
	[
		["John", "johnsmith@mail.com", "john00@mail.com"],
		["John", "johnnybravo@mail.com"],
		["John", "johnsmith@mail.com", "john_newyork@mail.com"],
		["Mary", "mary@mail.com"]
	]
	
	Output: 
	[
		["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
		["John", "johnnybravo@mail.com"],
		["Mary", "mary@mail.com"]
	]

	Explanation: 
	The first and third John's are the same person as they have the common email "johnsmith@mail.com".
	The second John and Mary are different people as none of their email addresses are used by other accounts.

	You could return these lists in any order, for example the answer
	
	[
		['Mary', 'mary@mail.com'],
		['John', 'johnnybravo@mail.com'],
		['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
	]
	is also acceptable.
```

**Union Find**

这里总结一下思路：

```
1 这道题可以抽象化为图中找 connecting component 的问题，
首先，将输入的每一个用户都看成图中的一个点，由于用户的姓名可以重复，
我们用 user_id 来代表一个用户

2 如何判断两个点是存在于同一个联通块中？同一个 email 的被不同的 user_id 同时拥有，
那么这两个点 (user_id) 属于一个联通块。因此，需要构建 email_to_ids 的 HashMap,
key-value pair 的结构为: email : 拥有这个 email 的 user 的 user_id 的 list
对属于同一个 list 的 user_id 进行 union 操作，他们拥有至少一个共同的 email,
判定他们是同一个用户，属于同一个联通块

3 如何 format 题目想要的结果？每一个联通块就是一个单独的用户，每一个联通块由 user_id 代表，
user_id 同时也是 accounts list 的下标，accounts[user_id][0] 就是该联通块代表的用户的名字
同时，我们还要知道每个联通块对应的 emails, 所以还需要构建 id_to_email_set 这个 HashMap,
构建时，将属于同一个联通块的所有 email 加到这个联通块的 email_set 中
```

可以优化的点:

- `forward_index` 我用的 `defaultdict(list)` 会有重复的, 建议用 `set`

```python
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
```
