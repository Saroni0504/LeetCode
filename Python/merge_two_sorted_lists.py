'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        if list1 and not list2:
            return list1
        if not list1 or (not list1 and not list2):
            return list2
        
        merged_list = ListNode()
        last_node = None
        while True:

            if last_node:
                last_node.next = ListNode()
                last_node = last_node.next
            else:
                last_node = merged_list
                
            if list1.val < list2.val:
                last_node.val = list1.val 
                list1 =  list1.next

            elif list1.val > list2.val:
                last_node.val = list2.val 
                list2 = list2.next

            else:  # equality
                last_node.val = list1.val
                last_node.next = ListNode(val=list2.val)
                last_node = last_node.next
                list1 = list1.next
                list2 = list2.next

            if not list1:
                last_node.next = list2
                return merged_list
            if not list2:
                last_node.next = list1
                return merged_list


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        merged_list = ListNode()
        head = merged_list
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 or list2
        return merged_list.next
