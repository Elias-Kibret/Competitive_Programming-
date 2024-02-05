
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    
    let [prev,temp]=[null,head]

 while(temp){
     let nextNode=temp.next
     temp.next=prev
     prev=temp 
     temp=nextNode
 }
 
 return prev
};

                    // Elias Kibret



                    var reverseList = function(head) {
                        let [prev, current] = [null, head]
                        while(current) {
                            [current.next, prev, current] = [prev, current, current.next]
                        }
                        return prev
                    }
                     

                    // by Saltant @leetcode