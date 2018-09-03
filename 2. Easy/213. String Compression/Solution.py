class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        if not originalString or len(originalString) == 1:
            return originalString

        mapping = {}
        mapping[originalString[0]] = 0
        result = ""

        for os in originalString:
            if os not in mapping:
                newSubString = mapping.keys()[0] + str(mapping.get(mapping.keys()[0]))
                result += newSubString
                mapping.clear()

            mapping[os] = mapping.get(os, 0) + 1

        newSubString = mapping.keys()[0] + str(mapping.get(mapping.keys()[0]))
        result += newSubString
        return result if len(result) < len(originalString) else originalString
