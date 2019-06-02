/*
Solution 1
Use a second stack with size equal to the original stack
Memory cost is always 2X
Let’s say we push 1 one thousand times, do we have to push all of them to the helper_stack? No!
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
        if (helper_stack.empty() || x < helper_stack.top()) {
            helper_stack.push(x);
        } else {
            helper_stack.push(helper_stack.top());
        }
    }

    void pop() {
        original_stack.pop();
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