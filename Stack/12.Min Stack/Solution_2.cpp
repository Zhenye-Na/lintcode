/*
Solution 2:
Use a second stack with size <= original stack
Same size worst case
Minimum has to be duplicated in helper_stack, otherwise we will remove the minimum too soon and won’t be able to know the correct minimum anymore
Intuition: Pick a decreasing sequence ending at the current entry in the orignal_stack to the helper_stack
Best input for space usage:
First entry is the minimum value, we only have one entry in the helper_stack!
Worst input for space usage:
Entries are is descending order, we have to keep all entries in the helper_stack! Since the intuition here is picking a decreasing sequence ending at the current entry in the orignal_stack to the helper_stack.
*/

class MinStack {
    stack<int> original_stack;
    stack<int> helper_stack;
    
public:
    /** initialize your data structure here. */
    MinStack() {

    }

    void push(int x) {
        original_stack.push(x);
        // remember to add the equal sign, we have to keep the duplicates
        // on the helper_stack!
        if (helper_stack.empty() || x <= helper_stack.top())
            helper_stack.push(x);
    }

    void pop() {
        int x = original_stack.top();
        original_stack.pop();
        if (x == helper_stack.top())
            helper_stack.pop();
    }

    int top() {
        return original_stack.top();
    }

    int getMin() {
        return helper_stack.top();
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