from collections import defaultdict

class Solution:
    """
    @param paths: a list of string
    @return: all the groups of duplicate files in the file system in terms of their paths
    """
    def findDuplicate(self, paths):
        # Write your code here
        if not paths or len(paths) == 0:
            return []

        res = []
        # map from content to directory
        mapping = defaultdict(list)

        for path in paths:
            # path = "root/a 1.txt(abcd) 2.txt(efgh)"
            splitted_path = path.split(' ')
            prefix_path = splitted_path[0]
            for idx in range(1, len(splitted_path)):
                file_name, content = splitted_path[idx].split('(')
                content = content[:len(content) - 1] # remove ')'

                mapping[content].append(prefix_path + "/" + file_name)

        for _, filelist in mapping.items():
            if len(filelist) > 1:
                res.append(filelist)

        return res
