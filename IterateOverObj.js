// Iterate through the object
for (const key in obj) {
	if (population.hasOwnProperty(key)) {
		console.log(`${key}: ${[key]}`);
	}
}

// Iterate through the object

Object.entries(obj).forEach(([key, value]) => {
	console.log(key, value);
});

// Or

for (let [key, value] of Object.entries(obj)) {
	console.log(key, value);
}

// Elias Kibret
