function totalReplacements(ranks: number[]): number {
     if(ranks.length==0){
        return 0
     }
     let minRank:number=ranks[0]
     let countReplacement=0

     for(let i=1;i<ranks.length;i++){
        if(minRank>ranks[i]){
            minRank=ranks[i]
            countReplacement++
        }
     }
     return countReplacement
    
};