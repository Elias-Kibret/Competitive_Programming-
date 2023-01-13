/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
	let length = 0;
	if (!head) return head;
	let temp = head;
	while (temp) {
		temp = temp.next;
		length++;
	}
	temp = head;
	for (let i = 0; i < length; i++) {
		if (i == length - n - 1) {
			temp.next = temp.next.next;
			break;
		}
		if (length - n - 1 < 0) {
			return temp.next;
		}
		temp = temp.next;
	}
	return head;
};

// Your Boy Elias Kibret
