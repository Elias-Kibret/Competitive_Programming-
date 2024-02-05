/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 *   Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
 *
 */
/**
 *
 *
 *
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */

var removeElements = function (head, val) {
	while (head !== null) {
		if (head.val === val) {
			head = head.next;
		} else {
			break;
		}
	}
	let temp = head;
	while (temp && temp.next) {
		if (temp.next.val == val) {
			temp.next = temp.next.next;
		} else {
			temp = temp.next;
		}
	}
	return head;
};

// Elias Kibret

const maxArea = (height) => {
	let result = 0,
		left = 0,
		right = height.length - 1;

	while (left < right) {
		let smallestSide = Math.min(height[left], height[right]);
		let area = (right - left) * smallestSide;

		if (area > result) result = area;

		if (height[left] < height[right]) left++;
		else right--;
	}

	return result;
};
//By DrewBie leetcode
