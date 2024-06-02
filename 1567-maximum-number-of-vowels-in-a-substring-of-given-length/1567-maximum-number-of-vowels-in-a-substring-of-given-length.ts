function maxVowels(s: string, k: number): number {
    const mySet: Set<String>=new Set(['a','e','i','o','u'])

    let max_count=0
    let current_count=0
    for (let i=0; i<k;i++){
        if(mySet.has(s[i]))current_count++
    }
    if(current_count==k)return k
    max_count=current_count
    for(let right=k;right<s.length;right++){
        if(mySet.has(s[right])){
            current_count++
        }
        if(mySet.has(s[right-k])){
            current_count--
        }
        if(current_count==k)return k
        max_count=Math.max(max_count,current_count)
    }
    return max_count


};