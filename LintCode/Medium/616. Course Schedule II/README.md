# 616. Course Schedule II

- **Description**
    - There are a total of n courses you have to take, labeled from `0` to `n - 1`.
    - Some courses may have prerequisites, for example to take course `0` you have to first take course `1`, which is expressed as a pair: `[0,1]`
    - Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
    - There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
- **Example**
- Given `n = 2`, prerequisites = `[[1,0]]`
- Return `[0,1]`
- Given `n = 4`, prerequisites = `[1,0],[2,0],[3,1],[3,2]]`
- Return `[0,1,2,3]` or `[0,2,1,3]`


## Solution

跟 615 题道理一样，只不过这道题要把结果输出来。如果 `result` 最后的 `index ！= numCourses`，那么相当于 有环，直接返回空数组即可


### Code

```java
public class Solution {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: the course order
     */
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // write your code here

        int[] result = new int[numCourses];
        int[] indegree = new int[numCourses];
        List[] order = new ArrayList[numCourses];  // Array of ArrayList
        int added = 0;

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
            result[added] = prerequisite;

            
            for (Object c : order[prerequisite]) {
                int course = (int) c;

                indegree[course]--;

                if (indegree[course] == 0) {
                    queue.offer(course);
                }
    
            }
            added++;
        }

        if (added == numCourses) {
            return result;
        } else {
            return new int[0];
        }
    }
}
```