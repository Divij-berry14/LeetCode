class Node:
    def __init__(self, data= 0):
        self.data = data
        self.next = None
    def printl(self):
        print("divij")

class Solution():
    def reOrderListLL(self, head):
        if head is None:
            return None
        curr = head
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None
        temp1 = temp
        prev = None
        while temp1 is not None:
            next = temp1.next
            temp1.next = prev
            prev = temp1
            temp1 = next
        temp = prev
        head = Node(0)
        curr1 = head
        while (curr is not None) or (temp is not None):
            if curr:
                curr1.next = curr
                curr1 = curr1.next
                curr = curr.next
            if temp:
                curr1.next = temp
                curr1 = curr1.next
                temp = temp.next
        head = head.next
        return head

    def printLL(self, head):
        if head is None:
            return None
        count = 0
        while head is not None:
            print(head.data, "->", end=" ")
            head = head.next
        count += 1
        print(None)

    def InputLL(self):
        li = [int(x) for x in input().split()]
        head = None
        tail = None
        for currdata in li:
            if currdata == -1:
                break
            newNode = Node(currdata)
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = tail.next
        return head
head = Solution()
newHead = head.InputLL()
head.printLL(newHead)
newHead1 = head.reOrderListLL(newHead)
head.printLL(newHead1)