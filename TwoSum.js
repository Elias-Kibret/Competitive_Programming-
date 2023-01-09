/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	var number = [];

	for (let i = 0; i <= nums.length; i++) {
		var temp = nums[i];
		for (let j = i + 1; j <= nums.length - 1; j++) {
			if (temp + nums[j] == target) {
				number.push(i);
				number.push(j);
				return number;
				break;
			}
		}
	}
};
// Elias Kibret
