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