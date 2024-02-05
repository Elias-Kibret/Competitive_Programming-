
function solution(cards) {
    let map = new Map()
    
    cards = cards.flat()
    
     cards.forEach((item)=>{
       if(map.has(item)){
         map.set(item, map.get(item)+1)
       }
       else {
       map.set(item,1)
       }
     })
     
  let uniqueCards;
  for (item of [...map.keys()]){
     if(map.get(item)===1)
     {
       if (uniqueCards == undefined) {
        uniqueCards=item
       }
        uniqueCards<item?uniqueCards=item:uniqueCards
     }
    }
    return uniqueCards!=undefined?uniqueCards:-1
 }
 
 console.log(solution([[5,7,3,9,4,9,8,3,1],[1,2,2,4,4,1],[1,2,3]]))
 // 8
 console.log(solution([[5,5],[2,2]]))
 // -1

 