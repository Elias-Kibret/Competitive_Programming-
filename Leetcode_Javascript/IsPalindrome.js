// Valid Palindrome

/**
 * 
 * Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
	s = s.replace(/[^A-Za-z0-9]/g, "").toLowerCase();
	return s === s.split("").reverse().join("");
};
