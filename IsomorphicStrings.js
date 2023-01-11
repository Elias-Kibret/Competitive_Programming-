/** 205. Isomorphic Strings
 * Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isIsomorphic = function (s, t) {
	const map = {};
	let T = [...t];
	let S = [...s];
	let check = true;
	S.forEach((item, index) => {
		if (map[item] === undefined) {
			map[item] = T[index];
		}
		if (!(map[item] == T[index])) {
			check = false;
		}
	});
	if (
		[...new Set(Object.values(map))].length !==
		[...new Set(Object.keys(map))].length
	) {
		check = false;
	}

	return check;
};

// Elias Kibret
