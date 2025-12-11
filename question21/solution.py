from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:              
        is_list1_empty = list1 == None
        is_list2_empty = list2 == None
        if is_list1_empty and is_list2_empty: return None
        if is_list1_empty: return list2
        if is_list2_empty: return list1

        def createListNode(l: list):
            node = ListNode(l[-1])
            for i in range(len(l)-2, -1, -1):
                new_node = ListNode(l[i])
                new_node.next = node
                node = new_node
            return node
        
        sorted_list = []
        
        current_list1_node = list1
        current_list2_node = list2
        
        if list1.val < list2.val: 
            sorted_list.append(list1.val)
            current_list1_node = list1.next
        else:
            sorted_list.append(list2.val)
            current_list2_node = list2.next
        
        while current_list1_node != None and current_list2_node != None:
            if current_list1_node.val < current_list2_node.val: 
                sorted_list.append(current_list1_node.val)
                current_list1_node = current_list1_node.next
                continue
            
            sorted_list.append(current_list2_node.val)
            current_list2_node = current_list2_node.next
            
        if current_list1_node == None:
            while current_list2_node != None:
                sorted_list.append(current_list2_node.val)
                current_list2_node = current_list2_node.next
                
        if current_list2_node == None:
            while current_list1_node != None:
                sorted_list.append(current_list1_node.val)
                current_list1_node = current_list1_node.next

        print(sorted_list)
        return createListNode(sorted_list)
