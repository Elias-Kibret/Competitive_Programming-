//  Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

// Integers in each row are sorted in ascending from left to right.
// Integers in each column are sorted in ascending from top to bottom.

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
// var searchMatrix = function (matrix, target) {
// 	matrix = matrix.flat().sort((a, b) => a - b);
// 	let left = matrix[0];
// 	let right = matrix[matrix.length - 1];
// 	while (left <= right) {
// 		let half = Math.floor(matrix.length / 2);
// 		if (target === matrix[half]) return true;
// 		if (target === left) return true;
// 		if (target === right) return true;
// 		if (target > matrix[half]) {
// 			left = matrix[half + 1];
// 			matrix = matrix.splice(half);
// 		} else if (target < matrix[half]) {
// 			matrix = matrix.splice(0, half);
// 			right = matrix[half - 1];
// 		}
// 	}
// 	return false;
// };

// let matrix = [
// 	[1, 3, 5, 7, 9],
// 	[2, 4, 6, 8, 10],
// 	[11, 13, 15, 17, 19],
// 	[12, 14, 16, 18, 20],
// 	[21, 22, 23, 24, 25],
// ];
// let target = 8;
// console.log(searchMatrix(matrix, target));

var searchMatrix = function (matrix, target) {
	if (matrix.length === 0) {
		return false;
	}
	//start with top-right element
	var i = 0;
	var j = matrix[0].length - 1;

	//loop till row and column number are within bounds
	while (i <= matrix.length - 1 && j >= 0) {
		if (matrix[i][j] > target) {
			//current element is greater than target
			//means this row might have the target element
			//change column
			j--;
		} else if (matrix[i][j] === target) {
			//element found
			return true;
		} else if (matrix[i][j] < target) {
			//current element is lesser than target
			//means this column might have the target element
			//change rows
			i++;
		}
	}
	return false;
};
