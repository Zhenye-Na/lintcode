# 12. Min Stack

**Description**

Implement a stack with following functions:

- `push(val)` push val into the stack
- `pop()` pop the top element and return it
- `min()` return the smallest number in the stack
- All above should be in `O(1)` cost.

```
min() will never be called when there is no number in the stack.
```

**Example**

Example 1:

```
Input:
  push(1)
  pop()
  push(2)
  push(3)
  min()
  push(1)
  min()
Output:
  1
  2
  1
```

Example 2:

```
Input:
  push(1)
  min()
  push(2)
  min()
  push(3)
  min()
Output:
  1
  1
  1
```

**4 种解法**

https://www.youtube.com/watch?v=5h42eila268


**解法 1**

用到了两个栈的数据结构, 跟第二种解法比较相似, 但是不同的点是:

- `push()`
    - 只有当 `helper_stack` 为空 或者 `helper_stack` 的栈顶元素比 `push` 进来的元素 (`x`) **大**的时候, 在 `helper_stack` 添加 `x`
    - 反之, 再次把 `helper_stack.top()` 压栈
- `pop()`
    - `helper_stack` 和 `original_stack` 都要同时 `pop()`



```cpp
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
```

**解法 2**

- push()
    - 只有当 `min_stack` 为空 或者 `min_stack` 的栈顶元素比 `push` 进来的元素 (`x`) **大于等于**的时候, 在 `min_stack` 添加 `x`
- pop()
    - 正常 `value_stack.pop()`, 针对 `min_stack` 多了一点操作, 就是如果从 `value_stack` 的栈顶元素正好跟 `min_stack` 的栈顶元素相等, 那么就要把 `min_stack` 一起 `pop` 掉

```python
class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.value_stack = []
        self.min_stack = []


    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.value_stack.append(number)
        if len(self.min_stack) == 0 or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        element = self.value_stack.pop()
        if element == self.min_stack[-1]:
            self.min_stack.pop()
        return element

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_stack[-1]
```


**解法 3**

> 视频中的解法 4

4 个栈

```cpp
/*
Solution 3:
optimized for space usage while keeping O(1) time operation
Original stack:             5, 4, 4, 3, 4, 2, 2, 2 ... 2 (repeated a thousand times)
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
```


**解法 4**

暂无代码

思路:

跟 解法3 类似, 但是用一个 HashMap 来记录最小值出现的次数 `{4:2, 2:1000}`, 然后用 HashMap 模拟 `stack<int> duplicate_min_count` 的功能

缺点:

如果元素 近似于 uniform distribution 会很费空间, HashMap, Hash 的时间也不小
