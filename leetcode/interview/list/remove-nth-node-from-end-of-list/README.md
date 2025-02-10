# 19. Remove Nth Node From End of List

Solved
Medium
Topics
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?

### Solution

Input: head = [1,2,3,4,5], n = 2

- add a dummy node pointing to the list head
- [dummy, 1,2,3,4,5]
- create a forward pointer to the dummy and move it n times to a next node
- - [dummy, 1,forward->2,3,4,5]
- create a backward pointer to the dummy node
- [backward->dummy, 1,forward->2,3,4,5]
- move the both pointers to a next node until forward points to the last element, whose Next is nil
- [dummy, 1,2,backward->3,4,forward->5]
- set the Next value of the node the backward is pointing, the node #3, to the next node #4 node.Next
- [dummy, 1,2,backward->3,forward->5]
- return the list starting from the head [1,2,3,5]

### Go

<https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1537434322>

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func removeNthFromEnd(head *ListNode, n int) *ListNode {
 dummy := ListNode{Next: head}
 forward := &dummy
 backward := &dummy

 for i := 0; i<n; i++ {
   forward = forward.Next
 }

 for forward.Next != nil {
   forward = forward.Next
   backward = backward.Next
 }

 backward.Next = backward.Next.Next
 return dummy.Next
}
```

### time

O(N)

0
ms
Beats
100.00%

### memory

O(1)
