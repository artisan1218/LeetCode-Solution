# %%
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNodeHash(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        while headA is not None:
            seen.add(headA)
            headA = headA.next
        
        while headB is not None:
            if headB in seen:
                return headB
            else:
                headB = headB.next
        return None

    def getIntersectionNodeCount(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # calculate length of headA
        lenA = 0
        counterA = headA
        while counterA is not None:
            counterA = counterA.next
            lenA += 1
        
        # calculate length of headB
        lenB = 0
        counterB = headB
        while counterB is not None:
            counterB = counterB.next
            lenB += 1

        # swap A and B if B is longer than A, make sure A is always the longer one
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        # move the longer pointer to the same position as the shorter one
        lenDiff = lenA - lenB
        while lenDiff > 0:
            headA = headA.next
            lenDiff -= 1
        
        # start comparing, if they share an intersection, the pointers must be equal
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA # headB is also ok because they are same

    def getIntersectionNodeCount2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptrA, ptrB = headA, headB
        while ptrA != ptrB:
            # traverse A til the end, then points A to headB, do the same for B
            # this will make sure that ptrA and ptrB, after reaching the end of A and B,
            # are aligned, which means they will reach the intersection node at the same time
            if ptrA is None:
                ptrA = headB
            else:
                ptrA = ptrA.next

            if ptrB is None:
                ptrB = headA
            else:
                ptrB = ptrB.next
        return ptrA



if __name__ == '__main__':
    solver = Solution()

    intersection = ListNode(8)
    intersection.next = ListNode(4)
    intersection.next.next = ListNode(5)

    ll1 = ListNode(4)
    ll1.next = ListNode(1)  
    ll1.next.next = intersection

    ll2 = ListNode(5)
    ll2.next = ListNode(6)
    ll2.next.next = ListNode(1)
    ll2.next.next.next = intersection   

    result = solver.getIntersectionNodeCount2(ll1, ll2)
    print(result.val)   


