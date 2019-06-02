/*
Solution 3:
optimized for space usage while keeping O(1) time operation
Original stack:             5, 4, 4, 3, 4, 2, 2, 2, ..., 2 (repeated a thousand times)
Unique min stack:           5, 4, 3, 2
Duplicate min stack:        4, 2
Duplicate min stack count:  2, 1000
*/

class MinStack {
    stack<int> original_stack;
    stack<int> unique_min_stack;
    stack<int> duplicate_min_stack;
    stack<int> duplicate_min_count;
    
public:
    /** initialize your data structure here. */
    MinStack() {

    }

    void push(int x) {
        original_stack.push(x);
        if ((unique_min_stack.empty() && duplicate_min_stack.empty()) || 
            x < getMin()) {
            // first entry or new min
            unique_min_stack.push(x); 
        } else if (x == getMin()) {
            // min we found before
            if (unique_min_stack.empty() || unique_min_stack.top() != x) {
                // min has count >= 2 before push
                int new_count = duplicate_min_count.top() + 1;
                duplicate_min_count.pop();
                duplicate_min_count.push(new_count);
            } else {
                // min has count == 1 before push
                unique_min_stack.pop();
                duplicate_min_stack.push(x);
                duplicate_min_count.push(2);
            }
        } // no else here, ignore if not a min
    }

    void pop() {
        int x = original_stack.top();
        original_stack.pop();
        if (x == getMin()) {
            // check whether the min is in unique or duplicate stack
            if (unique_min_stack.empty() || x != unique_min_stack.top()) {
                // min in duplicate stack
                int count = duplicate_min_count.top();
                duplicate_min_count.pop();
                if (count == 2) {
                    // move from duplicate to unique
                    unique_min_stack.push(duplicate_min_stack.top());
                    duplicate_min_stack.pop();
                } else {
                    // decrement count
                    duplicate_min_count.push(--count);
                }
            } else {
                // min in unique stack
                unique_min_stack.pop();
            }
        }
    }

    int top() {
        return original_stack.top();
    }

    int getMin() {
        // check both unique and duplicate stack to determine the min value
        if (!unique_min_stack.empty() && !duplicate_min_stack.empty()) {
            return min(unique_min_stack.top(), duplicate_min_stack.top());
        } else if (unique_min_stack.empty()) {
            return duplicate_min_stack.top();
        } else {
            return unique_min_stack.top();
        }
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */