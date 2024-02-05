/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
	return s
		.trim()
		.split(" ")
		.reverse()
		.filter((item) => {
			return item !== "";
		})
		.join(" ");
};
// Elias Kibret
