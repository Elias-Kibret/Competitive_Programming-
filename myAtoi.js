/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
	const INT_MAX = 2147483647;
	const INT_MIN = -2147483648;
	const num = parseInt(s);
	if (num < INT_MIN) return INT_MIN;
	if (num > INT_MAX) return INT_MAX;
	return isNaN(num) ? 0 : num;
};

// Elias Kibret
