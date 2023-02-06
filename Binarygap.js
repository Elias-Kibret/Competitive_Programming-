// Codility Interview Question

function solution(N) {
	// Implement your solution here
	let num = 0;
	let index = 0;
	N = Math.abs(N).toString(2).split("");
	for (let i = 0; i < N.length; i++) {
		if (N[i] == 1) {
			if (num <= i - index) {
				num = i - index;
				index = i;
			}
		}
	}
	return num == 0 ? num : num - 1;
}

// Elias Kibret
