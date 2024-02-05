/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {

    //if length is not equal return 
    
   if(s.length!==t.length)return false
   
   //if they have differenct char
   
   if([...s].sort().join('')!==[...t].sort().join(''))return false
   
   return true
   };
   
                            // Elias Kibret