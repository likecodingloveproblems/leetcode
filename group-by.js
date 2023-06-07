/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
    result = {}
    for (const item of this) {
        if (fn(item) in result) {
            result[fn(item)].push(item)
        } else {
            result[fn(item)] = [item]
        }
    }
    return result
};

console.log([1, 2, 3].groupBy(String)) // {"1":[1],"2":[2],"3":[3]}
