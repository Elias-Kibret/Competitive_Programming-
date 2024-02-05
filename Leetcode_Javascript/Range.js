/**
 *  Write a JavaScript program to get the integers in range (x, y).  Go to the editor
Example : range(2, 9)
Expected Output : [3, 4, 5, 6, 7, 8]
 * 
 */

function range(x, y) {
	const values = [];
	if ((x = y)) {
		return values;
	} else {
		range(x - 1, y);
	}
}
