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
