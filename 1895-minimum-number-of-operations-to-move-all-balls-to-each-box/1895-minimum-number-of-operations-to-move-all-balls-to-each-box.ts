function minOperations(boxes: string): number[] {
    

    let result=[]

    for (let i=0 ; i<boxes.length;i++){
        let count=0
        for(let j=0;j<boxes.length;j++){
            if (boxes[j]=='1'){
                 count+=Math.abs(i-j)
            }
              
        } 
        result[i]=count
    }
    return result
};