/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
	let prefix = "";
	let flag = 0;
	let shortestStr = strs.reduce((a, b) => {
		return a.length <= b.length ? a : b;
	});
	for (let i = 0; i < shortestStr.length; i++) {
		let checkPrefix = strs[0][i];
		strs.forEach((item, index) => {
			if (item[i] == checkPrefix) {
				flag++;
			}
		});

		if (flag == strs.length) {
			prefix = prefix + checkPrefix;
		} else {
			break;
		}
		flag = 0;
	}

	return prefix;
};
// Elias Kibret
