// You are given a string number representing
// a positive integer and a character digit.

//  Return the resulting string after removing
//exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized.The test cases are generated such that digit occurs at least once in number.


/* Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12". 

*/



function removeDigit(s: string, digit: string): string {

    let str:string[]=[]
    for(let i:number=0;i<s.length;i++){
    
        if(s[i]===digit){
         str.push(s.substring(0, i) + '' + s.substring(i + 1))
        }
    }
    str.sort()
    return str[str.length-1]
    
    };