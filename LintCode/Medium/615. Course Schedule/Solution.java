public class Solution {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // write your code here

        int[] indegree = new int[numCourses];
        List<Integer> order = new ArrayList<>();
        // int remaining = numCourses;

        // Update indegree of all courses
        for (int[] pair : prerequisites) {
            indegree[pair[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // BFS
        while (!queue.isEmpty()) {
            
            int course = queue.poll();
            // remaining--;
            order.add(course);
            
            for (int[] pair : prerequisites) {

                if (pair[1] == course) {
                    indegree[pair[0]]--;

                    if (indegree[pair[0]] == 0) {
                        queue.offer(pair[0]);
                    }
                }
            }

        }
        
        if (order.size() != numCourses) {
            return false;
        } else {
            return true;
        }
    }
}





public class Solution {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // write your code here

        int[] indegree = new int[numCourses];
        List[] order = new ArrayList[numCourses];  // Array of ArrayList
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