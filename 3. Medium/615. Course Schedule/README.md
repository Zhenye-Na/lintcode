# 615. Course Schedule

- **Description**
    - There are a total of n courses you have to take, labeled from `0` to `n - 1`.
    - Some courses may have prerequisites, for example to take course `0` you have to first take course `1`, which is expressed as a pair: `[0,1]`
    - Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
- **Example**
    - Given `n = 2`, prerequisites = `[[1,0]]`
    - Return `true`
    - Given `n = 2`, prerequisites = `[[1,0],[0,1]]`
    - Return `false`


## Solution

**Topological Sorting (拓扑排序) + BFS + Queue**

- 根据题意，先修课程是用 `index = 1` 的 1D array 中的元素表示的；Topological Sorting 要用到 `BFS+Queue`
- 获得所有课程的 indegree，并且得到所有“相对”先修课程的后修课程
- 将 `indegree == 0` 的课程放入 `Queue` 中，进行 BFS，同时将 `poll()` 出来的课程放入 `result` 中，对于该课程的所有后修课程 `indegree--`
- 如果最后还有课程没有添加进 `queue` 中，那么相当于又换，`return false` 即可


### Code

```java
public class Solution {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // write your code here

        int[] indegree = new int[numCourses];
        List[] order = new ArrayList[numCourses];
        int remaining = numCourses;

        // Get prerequisites
        for (int i = 0; i < numCourses; i++) {
            order[i] = new ArrayList<Integer>();
        }
        
        // Update indegree of all courses
        for (int[] pair : prerequisites) {
            indegree[pair[0]]++;
            order[pair[1]].add(pair[0]);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // BFS
        while (!queue.isEmpty()) {
            
            int prerequisite = queue.poll();
            remaining--;

            
            for (Object c : order[prerequisite]) {
                int course = (int) c;

                indegree[course]--;

                if (indegree[course] == 0) {
                    queue.offer(course);
                }
    
            }

        }
        return (remaining == 0);
    }
}
```