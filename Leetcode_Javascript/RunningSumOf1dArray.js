/* Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]


*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function (nums) {
	let outPut = [0];
	let currentIndex = 0;
	let prevIndex = 0;
	for (let i = 0; i < nums.length; i++) {
		if (i === 0) {
			outPut[currentIndex] = outPut[prevIndex] + nums[i];
		} else {
			currentIndex = i;
			outPut[currentIndex] = outPut[prevIndex] + nums[i];
			prevIndex++;
		}
	}
	return outPut;
};
// Elias Kibret

const runningSum = (nums) => {
	nums.reduce((a, c, i, arr) => (arr[i] += a));
	return nums;
};
// Leetcode trevH

const runningSum = (nums) => {
	for (let i = 1; i < nums.length; i++) {
		nums[i] += nums[i - 1];
	}
	return nums;
};
// By AndanRashied

var runningSum = function (nums) {
	return nums.map((num, i) => (i > 0 ? (nums[i] += nums[i - 1]) : nums[i]));
};

// by Risclover
