# 426. Restore IP Addresses

**Description**

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

(Your task is to add three dots to this string to make it a valid IP address. Return all possible IP address.)

You can return all valid IP address in any order.


**Example**

Example 1:

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
Explanation: ["255.255.111.35", "255.255.11.135"] will be accepted as well.
```

Example 2:

```
Input: "1116512311"
Output: ["11.165.123.11","111.65.123.11"]
```

**DFS**

*What makes an IP address valid?*

It contains four octets, each within the range `0` through `255` inclusive


```python
class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        if not s or len(s) < 4:
            return []

        ips = []
        self._find_all_ips(s, 0, "", ips)
        return ips

    def _find_all_ips(self, s, partition, ip, ips):

        if partition == 4 and s == "":
            ips.append(ip[1:])
            return

        for i in range(1, 4):
            if i <= len(s):

                if int(s[:i]) <= 255:
                    self._find_all_ips(s[i:], partition + 1, ip + "." + s[:i], ips)
                
                if s[0] == '0':
                    break
```