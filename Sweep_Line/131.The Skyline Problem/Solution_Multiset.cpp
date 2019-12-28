/**
* 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

struct Node {
    int x, h, isLeft;
    Node(int _x, int _h, int _isLeft):x(_x), h(_h),isLeft(_isLeft){}
    bool operator <(const Node &a) const {
        return x < a.x || x == a.x && isLeft < a.isLeft;
    }
};

class Solution {
public:
    /**
     * @param buildings: A list of lists of integers
     * @return: Find the outline of those buildings
     */

    vector<vector<int>> buildingOutline(vector<vector<int>> &buildings) {
        // write your code here
        multiset<int> s;
        vector<vector<int> > result;
        vector<Node> p;        
        int len = buildings.size();
        if (len == 0)
            return result;
        
        for (int i = 0; i < len; ++i) {
            p.push_back(Node(buildings[i][0], buildings[i][2], 1));
            p.push_back(Node(buildings[i][1], buildings[i][2], 0));
        }

        
        sort(p.begin(), p.end());
        
        len = 2 * len;
        int last = 0, size = 0;
        for (int i = 0; i < len; ++i) {
            if (s.empty())
                last = p[i].x;
            
            if (!s.empty() && (*s.rbegin()) <= p[i].h && last < p[i].x) {
                vector<int> tmp;
                if (size > 0 && result[size - 1][2] == (*s.rbegin()) && result[size - 1][1] == last) {
                    result[size -1][1] = p[i].x;
                } else {      
                    tmp.push_back(last);
                    tmp.push_back(p[i].x);
                    tmp.push_back(*s.rbegin());
                    result.push_back(tmp);
                    size ++;
                }
                last = p[i].x;
            }
            if (p[i].isLeft == 1)
                s.insert(p[i].h);
            else
                s.erase(s.lower_bound(p[i].h));
        }
        
        return result;
    }
};