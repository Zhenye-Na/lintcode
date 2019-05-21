// bfs version
class Solution {
public:
    bool validTree(int n, vector<pair<int, int>>& edges) {
        vector<unordered_set<int>> g(n, unordered_set<int>());
        unordered_set<int> v;
        queue<int> q;
        q.push(0);
        v.insert(0);
        for (auto a : edges) {
            g[a.first].insert(a.second);
            g[a.second].insert(a.first);
        }
        while (!q.empty()) {
            int t = q.front(); q.pop();
            for (auto a : g[t]) {
                if (v.find(a) != v.end()) return false;
                v.insert(a);
                q.push(a);
                g[a].erase(t);
            }
        }
        return v.size() == n;
    }
};


// union find version
class Solution {
public:
    /**
     * @param n an integer
     * @param edges a list of undirected edges
     * @return true if it's a valid tree, or false
     */
    bool validTree(int n, vector<vector<int>>& edges) {
        // Write your code here
        vector<int> root(n, -1);
        for(int i = 0; i < edges.size(); i++) {
            int root1 = find(root, edges[i][0]);
            int root2 = find(root, edges[i][1]);
            if(root1 == root2)
                return false;
            root[root1] = root2;
        }
        return edges.size() == n - 1;
    }
    int find(vector<int> &root, int e) {
        if(root[e] == -1)
            return e;
        else
            return root[e] = find(root, root[e]);
    }
};