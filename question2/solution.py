class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = l1
        current_node2 = l2
        values = []

        while True:
            values.append(current_node1.val+current_node2.val)
            if current_node1.next == None or current_node2.next == None: break
            current_node1 = current_node1.next
            current_node2 = current_node2.next

        list_length = len(values)

        values_modified = [values[i]*(10**(list_length-i-1)) for i in range(0, list_length)]
        values_modified_sum = sum(values_modified)
        values_modified_sum_string = str(values_modified_sum)

        result = ListNode(values_modified_sum_string[0])
        values_modified_sum_string = values_modified_sum_string[1:]
        for x in values_modified_sum_string:
            new_node = ListNode(x)
            new_node.next = result
            result = new_node

        return result