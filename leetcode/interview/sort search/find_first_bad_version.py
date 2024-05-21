"""
278. First Bad Version - Easy
You are here!
Your runtime beats 99.66 % of python3 submissions.

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def find_version(start, end):
            if start == end:
                return start
            elif end - start == 1:
                res_start = isBadVersion(start)
                res_end = isBadVersion(end)
                if res_start:
                    return start
                else:
                    return end
            mid = start + (end - start ) // 2
            res = isBadVersion(mid)
            if res:
                return find_version(start, mid)
            else:
                return find_version(mid, end)
            
        return find_version(1, n)