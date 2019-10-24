def mergeTwoLists(l1, l2):
    head = None

    while l1 or l2:
        if (l1 and not l2) or (l1 and l2 and l1.val <= l2.val):
            if not head:
                head = l1
                curNode = head
            else:
                curNode.next = l1
                curNode = curNode.next
            l1 = l1.next
        elif (l2 and not l1) or (l1 and l2 and l1.val > l2.val):
            if not head:
                head = l2
                curNode = head
            else:
                curNode.next = l2
                curNode = curNode.next
            l2 = l2.next

    return head