class Solution(object):
    def reverseList(self, head):
        # # Initialize prev pointer as NULL...
        # prev = None
        # # Initialize the curr pointer as the head...
        # curr = head
        # # Run a loop till curr points to NULL...
        # while curr:
        #     # Initialize next pointer as the next pointer of curr...
        #     next = curr.next
        #     # Now assign the prev pointer to curr’s next pointer.
        #     curr.next = prev
        #     # Assign curr to prev, next to curr...
        #     prev = curr
        #     curr = next
        # return prev       # Return the prev pointer to get the reverse linked list...

        prev=None

        cur=head

        while cur:
            newNode=cur.next
            cur.next=prev
            prev=cur
            cur=newNode
        return prev




      