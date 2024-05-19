/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    let unique=new Set()
    for (let email of emails){
        let [local,domain]=email.split("@")
        local=local.split("+")[0].replace(/\./g, "")
        unique.add(`${local}@{${domain}}`)

    }
    
    return unique.size
    
};