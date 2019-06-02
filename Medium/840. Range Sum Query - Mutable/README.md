# 840. Range Sum Query - Mutable

- **Description**
- Given an integer array nums, find the sum of the elements between indices `i` and `j` `(i ≤ j)`, inclusive.
- The `update(i, val)` function modifies nums by updating the element at index `i` to `val`.
    1. The array is **only modifiable by the update function**.
    2. You may assume the number of calls to `update` and `sumRange` function is distributed evenly.
- **Example**
    - Given `nums = [1, 3, 5]`

    ```java
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8
    ```


## Solution

### Fenwick Tree / Binary Indexed Tree


```cpp
class FenwickTree {
public:
    FenwickTree(int n): sums_(n + 1, 0) {}

    void update(int i, int delta) {
        while (i < sums_.size()) {
            sums_[i] += delta;
            i += lowbit(i);
        }
    }

    int query(int i) const {
        int sum = 0;
        while (i > 0) {
            sum += sums_[i];
            i -= lowbit(i);
        }
        return sum;
    }

private:
    static inline int lowbit(int x) { return x & (-x); }
    vector<int> sums_;

};



class NumArray {
public:
    NumArray(vector<int> nums): nums_(std::move(nums)), tree_(nums_.size()) {
        for (int i = 0; i < nums_.size(); ++i) {
            tree_.update(i + 1, nums_[i]);
        }
    }

    void update(int i, int val) {
        tree_.update(i + 1, val - nums_[i]);
        nums_[i] = val;
    }

    int sumRange(int i, int j) {
        return tree_.query(j + 1) - tree_.query(i);
    }

private:
    vector<int> nums_;
    FenwickTree tree_;
};


/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
```
