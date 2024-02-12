// https://leetcode.com/problems/escape-the-ghosts/description/

var escapeGhosts = function (ghosts, target) {

    for (let item of ghosts) {
        if ((Math.abs(item[0] - target[0]) + Math.abs(item[1] - target[1])) <= Math.abs(target[0]) + Math.abs(target[1])) {
            return false
        }
    }
    return true


};