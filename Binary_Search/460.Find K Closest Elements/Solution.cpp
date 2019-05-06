class Solution
{
  public:
    /**
     * @param A an integer array
     * @param target an integer
     * @param k a non-negative integer
     * @return an integer array
     */
    vector<int> kClosestNumbers(vector<int> &A, int target, int k)
    {
        // Algorithm:
        // 1. Find the first index that A[index] >= target
        // 2. set two pointers left = index - 1 and right = index
        // 3. compare A[left] and A[right] to decide move which pointer

        vector<int> result;
        int index = firstIndex(A, target);
        int left = index - 1, right = index;
        for (int i = 0; i < k; i++)
        {
            // compare A[left] and A[right] to decide move which pointer

            if (left < 0)
            {
                result.push_back(A[right++]);
            }
            else if (right >= A.size())
            {
                result.push_back(A[left--]);
            }
            else
            {
                if (target - A[left] <= A[right] - target)
                {
                    result.push_back(A[left--]);
                }
                else
                {
                    result.push_back(A[right++]);
                }
            }
        }

        return result;
    }

  private:
    int firstIndex(vector<int> &A, int target)
    {
        // use binary search algorithm to find the first index that
        // A[index] >= target

        int start = 0, end = A.size() - 1;
        while (start + 1 < end)
        {
            int mid = start + (end - start) / 2;
            if (A[mid] < target)
            {
                start = mid;
            }
            else
            {
                end = mid;
            }
        }

        if (A[start] >= target)
        {
            return start;
        }

        if (A[end] >= target)
        {
            return end;
        }

        return A.size();
    }
};