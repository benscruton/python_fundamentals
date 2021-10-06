# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
    def get_list_as_string(self):
        runner = self
        display = ""
        while runner != None:
            display += str(runner.val)
            if runner.next != None:
                display += " > "
            runner = runner.next
        return display

    def print_list(self):
        print(self.get_list_as_string())


def create_linked_list(*values):
    value_it = iter(values)
    output = ListNode(val = next(value_it))
    runner = output
    for value in value_it:
        runner.next = ListNode(val = value)
        runner = runner.next
    return output




def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    output = ListNode(val = 0)
    runner = output
    while l1 != None and l2 != None:
        runner.val += (l1.val + l2.val)
        carry_over = runner.val // 10
        runner.val %= 10
        runner.next = ListNode(val = carry_over)
        runner = runner.next
        l1 = l1.next
        l2 = l2.next
    rest = None
    if l1 != None:
        rest = l1
    elif l2 != None:
        rest = l2
    while rest != None:
        runner.val += rest.val
        carry_over = runner.val // 10
        runner.val %= 10
        runner.next = ListNode(val = carry_over)
        runner = runner.next
        rest = rest.next
    if runner == output or runner.val != 0:
        return output
    back_runner = output
    while back_runner.next != runner:
        back_runner = back_runner.next
    back_runner.next = None
    return output
        
            
# [2,4,3]
# [5,6,4]
# [0]
# [0]
# [9,9,9,9,9,9,9]
# [9,9,9,9]
[7,0,8]
[0]
[8,9,9,9,0,0,0,1]

test_cases = [
    {
        "l1": create_linked_list(2,4,3),
        "l2": create_linked_list(5,6,4),
        "solution": create_linked_list(7,0,8)
    },
    {
        "l1": create_linked_list(0),
        "l2": create_linked_list(0),
        "solution": create_linked_list(0)
    },
    {
        "l1": create_linked_list(9,9,9,9,9,9,9),
        "l2": create_linked_list(9,9,9,9),
        "solution": create_linked_list(8,9,9,9,0,0,0,1)
    },
]

for case in test_cases:
    r = add_two_numbers(case["l1"], case["l2"])
    assert r.get_list_as_string() == case["solution"].get_list_as_string()

print("Reached end of file")