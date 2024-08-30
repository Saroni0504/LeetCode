'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution:
    def merge(self, intervals):
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            t1 = set()
            start1 = intervals[i][0]
            end1 = intervals[i][1]
            t2 = set()
            start2 = intervals[i+1][0]
            end2 = intervals[i+1][1]
            for t in range(start1,end1 + 1):
                t1.add(t)
            for t in range(start2,end2 + 1):
                t2.add(t)
            if t1.intersection(t2):
                intervals[i] = [min(start1,start2),max(end1,end2)]
                del intervals[i+1]
            else:    
                i += 1
        return intervals
