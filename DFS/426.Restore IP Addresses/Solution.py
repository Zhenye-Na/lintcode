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
