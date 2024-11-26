function replaceElements(arr: number[]): number[] {
    let array_length=arr.length;

    let maxNumber:number=arr[array_length-1]
    arr[array_length-1]=-1
    for(let index=arr.length-2;index>=0;index--){
        let temp:number=arr[index]
        arr[index]=maxNumber
        maxNumber=Math.max(temp,maxNumber)
    }
    return arr

    
};