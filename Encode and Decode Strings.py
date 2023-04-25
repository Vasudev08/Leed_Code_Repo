class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res, i = [], 0

        while i < len(str):
            j = i
            while (str[j] != "#"): 
            # this is to find the index at which our delmiter '#' is present
                j += 1
            length = int(str[i:j]) # as we have increased the length by 1 we get 
            #length of the upcomming word by using index i 

            res.append(str[j + 1: j + 1 + length]) # we start with j + 1 index to 
            # get the actual string 
            i = j + 1 + length


