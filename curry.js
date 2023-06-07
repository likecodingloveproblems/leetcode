/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function (fn) {
    var inputs = []
    return function curried(...args) {
        inputs.push(...args)
        if (inputs.length === fn.length) {
            return fn(...inputs)
        } else {
            return curried
        }
    };
};


function sum(a, b) { return a + b; }
const csum = curry(sum);
console.log(csum()()(1, 3))
