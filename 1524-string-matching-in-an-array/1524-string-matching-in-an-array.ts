function stringMatching(words: string[]): string[] {

    let result:string[]=[]

    for(let word of words){
       for(let checkword of words){
              if(checkword.includes(word) && !result.includes(word) && word!==checkword){
                result.push(word)
              }
       }
    }
    return result
    
};