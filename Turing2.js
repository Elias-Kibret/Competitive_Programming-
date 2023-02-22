var twoSumLessThanK = function (A, K) {
	let map = new Map();
	for (item of A) {
		if (map.has(item)) {
			map.set(item, map.get(item) + 1);
		} else {
			map.set(item, 1);
		}
	}
	let min;
	for (item of A) {
	}
	console.log(map);
};

console.log(twoSumLessThanK([1, 2, 2, 3, 3, 3, 4, 5, 6], 3));
