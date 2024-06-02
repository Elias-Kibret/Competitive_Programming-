function totalFruit(fruits: number[]): number {
    let max_length=0
    let l=0
    const fruitsCount: Map<number,number>=new Map()

    for(let r=0,l=0;r<fruits.length;++r){
        fruitsCount.set(fruits[r],(fruitsCount.get(fruits[r]) || 0)+1)
        while (fruitsCount.size>2){
            fruitsCount.set(fruits[l],(fruitsCount.get(fruits[l]) || 0)-1)
            if(fruitsCount.get(fruits[l])===0){
                fruitsCount.delete(fruits[l])
            }
            l++;
        } 
        max_length=Math.max(max_length,r-l+1)
    }
    return max_length
    
};