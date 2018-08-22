public class Solution {
    /**
     * @param org: a permutation of the integers from 1 to n
     * @param seqs: a list of sequences
     * @return: true if it can be reconstructed only one or false
     */
    public boolean sequenceReconstruction(int[] org, int[][] seqs) {
        // write your code here
        if (org.length == 0 && seqs.length == 0 && seqs[0].length == 0) return true;
        if (org.length != 0 && (seqs.length == 0 || seqs[0].length == 0)) return false;
        
        int n = org.length;
        List[] dependecy = new ArrayList[n + 1];
        int[] indegree = new int[n + 1];

        // Examine whether elements seqs is out of bound
        for (int i = 0; i < seqs.length; i++) {
            for (int j = 0; j < seqs[i].length; j++) {
                if (seqs[i][j] > n) return false;
            }
        }
        
        // Create dependecy
        for (int i = 1; i <= n; i++) {
            dependecy[i] = new ArrayList<Integer>();
        }

        // Collect indegree
        for(int[] array : seqs) {
            int limit = array.length - 1;
            for (int index = 0; index < limit; index++) {
                dependecy[array[index]].add(array[index + 1]);
                indegree[array[index + 1]]++;

            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int j = 1; j <= n; j++) {
            if (indegree[j] == 0) queue.offer(j);
        }

        List<Integer> result = new ArrayList<>();

        // BFS
        while (!queue.isEmpty()) {
            int size = queue.size();
            if (size != 1) return false;
            
            int number = queue.poll();
            result.add(number);

            for (Object o : dependecy[number]) {

                int num = (int) o;
                indegree[num]--;

                if (indegree[num] == 0) {
                    queue.offer(num);
                }
            }
        }

        if (result.size() != n || !isSame(result, org)) {
            return false;
        } else {
            return true;
        }

    }

    // Result is the same as org or not
    private boolean isSame(List<Integer> result, int[] org) {

        int n = org.length;
        
        for (int i = 0; i < n; i++) {
            if (result.get(i) != org[i]) {
                return false;
            }
        }
        return true;
    }

}







/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param org a permutation of the integers from 1 to n
     * @param seqs a list of sequences
     * @return true if it can be reconstructed only one or false
     */
    public boolean sequenceReconstruction(int[] org, int[][] seqs) {
        // Write your code here
        Map<Integer, Set<Integer>> map = new HashMap<Integer, Set<Integer>>();
        Map<Integer, Integer> indegree = new HashMap<Integer, Integer>();
        
        for (int num : org) {
            map.put(num, new HashSet<Integer>());
            indegree.put(num, 0);
        }

        int n = org.length;
        int count = 0;
        for (int[] seq : seqs) {
            count += seq.length;
            if (seq.length >= 1 && (seq[0] <= 0 || seq[0] > n))
                return false;
            for (int i = 1; i < seq.length; i++) {
                if (seq[i] <= 0 || seq[i] > n)
                    return false;
                if (map.get(seq[i - 1]).add(seq[i]))
                    indegree.put(seq[i], indegree.get(seq[i]) + 1);
            }
        }

        // case: [1], []
        if (count < n)
            return false;
        
        Queue<Integer> q = new ArrayDeque<Integer>();
        for (int key : indegree.keySet()) 
            if (indegree.get(key) == 0)
                q.add(key);
        
        int cnt = 0;
        while (q.size() == 1) {
            int ele = q.poll();
            for (int next : map.get(ele)) {
                indegree.put(next, indegree.get(next) - 1);
                if (indegree.get(next) == 0) q.add(next);
            }
            if (ele != org[cnt]) {
                return false;
            }
            cnt++;
        }
        
        return cnt == org.length;
    }
}