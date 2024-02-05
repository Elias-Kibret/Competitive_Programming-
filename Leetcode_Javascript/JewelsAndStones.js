/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function (jewels, stones) {
	let map = new Map();
	stones.split("").forEach((item) => {
		if (map.has(item)) {
			map.set(item, map.get(item) + 1);
		} else map.set(item, 1);
	});
	let amount = 0;
	jewels.split("").forEach((item) => {
		if (map.has(item)) {
			amount = amount + map.get(item);
		}
	});
	return amount;
};
