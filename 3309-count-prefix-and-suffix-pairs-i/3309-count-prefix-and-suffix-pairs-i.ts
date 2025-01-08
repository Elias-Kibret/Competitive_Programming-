function countPrefixSuffixPairs(words: string[]): number {
    let count = 0;

    for (let i = 0; i < words.length - 1; i++) {
        for (let j = i + 1; j < words.length; j++) {
            if (isPrefix(words[i], words[j]) && isSuffix(words[i], words[j])) {
                count += 1;
            }
        }
    }
    return count;
}

function isPrefix(str1: string, str2: string): boolean {
    // Allow a word to be its own prefix
    return str2.startsWith(str1);
}

function isSuffix(str1: string, str2: string): boolean {
    // Allow a word to be its own suffix
    return str2.endsWith(str1);
}

// Example usage:

