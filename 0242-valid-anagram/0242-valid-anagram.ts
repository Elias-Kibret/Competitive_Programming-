function isAnagram(s: string, t: string): boolean {
    let count=Array(26).fill(0)

    for(let c of s){
        count[c.charCodeAt(0)-'a'.charCodeAt(0)]++;
    }
    for(let c of t){
        count[c.charCodeAt(0)-'a'.charCodeAt(0)]--;
    }
    for(let i=0;i<26;i++){
        if(count[i]!=0){
            return false;
        }
    }
    return true;
    
};