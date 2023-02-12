/**
 * @param {string[]} words
 * @return {string[]}
 * 1408. String Matching in an Array
 * Companies
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string
 */

var stringMatching = function (words) {
	let ss = [];
	words.forEach((string) => {
		words.forEach((subString) => {
			if (string.includes(subString) && string !== subString) {
				ss.push(subString);
			}
		});
	});
	return [...new Set(ss)];
}; // Elias Kibret
