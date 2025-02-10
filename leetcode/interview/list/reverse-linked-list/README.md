# 206. Reverse Linked List

<https://leetcode.com/problems/reverse-linked-list/description/>

Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solution

Input: head = [1,2]

- prev=nil, [1->2, 2->nil]
- curr=1, temp=2, [1->2, 2->nil]
- curr=2, temp=2, prev=1 [1->prev=nil, 2->nil]
- curr=2, temp=nil, prev=1 [1->nil, 2->1]
- curr=nil, temp=nil, prev=2 [1->nil, 2->1]
- return prev=2

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var temp, prev *ListNode
    curr := head
    
    for curr != nil {
        temp = curr.Next
        curr.Next = prev

        prev = curr
        curr = temp
    }
    
    return prev
}
```

<https://leetcode.com/problems/reverse-linked-list/submissions/1537848055/>

## Complexity

time = O(N)
mem = O(1)
