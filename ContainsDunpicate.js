// LeetCode day 2/365

/*
Given an integer array nums,
return true if any value appears at least
 twice in the array, and return false
 if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

*/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] === val) {
			nums.splice(i, 1);
			i--;
		}
	}
	return nums.length;
};

var removeElement = function (nums, val) {
	let arr = nums.filter((item) => item !== val);
	nums.length = 0;
	nums.push(...arr);
	return nums.length;
};
