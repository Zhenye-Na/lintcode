# 1257. Evaluate Division

**Description**

Equations are given in the format `A / B = k`, where `A` and `B` are variables represented as strings, and `k` is a *real number* (floating point number). Given some queries, return the answers. If the answer does not exist, return `-1.0`.

The input is always valid. You may assume that evaluating the queries will result in no division by **zero** and there is no contradiction.

**Example**

```
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].
```

The input is: `vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries`, where `equations.size() == values.size()`, and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

```
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
```

解析:

[**花花酱 LeetCode 399. Evaluate Division - 刷题找工作 EP120**](https://www.youtube.com/watch?v=UwpvInpgFmo)


```python
# 并查集里的变量：
# ra, rb 代表 a 的 root, b 的 root
# a_b 代表 a/b 的值
# self.root 存的是 某个node(比如a) 的 root, 以及 a/root的值 (node / node's root)


class UnionFind:

    def __init__(self):
        self.root = {}

    # 这里 a 是分子，b是分母，这题我们总是把分母作为root
    def union(self, a, b, a_b):

        # 由于是在线问题，不能预先存好图，进来的节点不一定之前存在
        # 因为一开始，每个node的root都是自己，所以node / node's root = 1
        if a not in self.root:
            self.root[a] = [1, a]
        if b not in self.root:
            self.root[b] = [1, b]

        a_ra, root_a = self.find(a)
        b_rb, root_b = self.find(b)

        # 合并a, b，总是把a的root指向b的root
        # a_b * b_rb / a_ra 是 root_a / root_b, 也就是节点node / node's root
        # 搞清楚这个公式是这题用并查集的一个点（如果用分母做root）的话。
        self.root[root_a] = [a_b * b_rb / a_ra, root_b]

    # find 要返回输入的a经过路径压缩后的root, 以及,之前说的，node / node's root, 这里也就是 a / root_a
    def find(self, a):

        # 因为最后要找a的root, 而在路径压缩的时候会改动a，所以先把a存起来
        tmp = a

        # path: 要压缩的node
        # rate: 没压缩前，需要压缩的node的 node / node's root
        # base有点难理解，需要想一想，指的是压缩后，新的 node / node's root
        # 注意rate 里存是是没压缩的，base是压缩后的
        # 比如 a->b->c->d , 现在要压缩, rate里就是 a/b, b/c, c/d,
        # 压缩完后，对于 a, 就是 a->d, 那其实就是rate里的相乘  a/b * b/c * c/d = a/d
        path, rate, base = [], [], 1

        while self.root[a][1] != a:
            path.append(a)
            rate.append(self.root[a][0])
            base *= self.root[a][0]

            a = self.root[a][1]

        # 其实，用上面的例子，对于一次find(a), 我们不止压缩 a, b c 都会被压缩
        # 所以，base就要对应到当前需要压缩的点
        # base 在进入这个 for 循环之前，是 a/b * b/c * c/d
        # 对于 b 来说，只需要 b/c * c/d
        # 所以，当前node, a 用完base后，要除以当前的rate[i], 也就是 a/b, 来更新base给下一个node （b）用
        for i in range(len(path)):
            self.root[path[i]][1] = a
            self.root[path[i]][0] = base
            base /= rate[i]
        return self.root[tmp]


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        uf = UnionFind()
        for i in range(len(values)):
            a, b, a_b = equations[i][0], equations[i][1], values[i]
            uf.union(a, b, a_b)

        ans = []
        for u, v in queries:
            if u in uf.root and v in uf.root:
                u_ur, root_u = uf.find(u)
                v_vr, root_v = uf.find(v)

                # 如果两个node root不同，证明不能相除
                if root_u != root_v:
                    ans.append(-1.0)
                else:
                    ans.append(u_ur / v_vr)
            else:
                ans.append(-1.0)
        return ans
```
