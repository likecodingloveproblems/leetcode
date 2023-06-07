/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function (fn, t) {
    let id
    return function (...args) {
        clearTimeout(id)
        id = setTimeout(fn, t, ...args)
    }
};

const log = debounce(console.log, 100);
log('Hello');
log('Hello');
log('Hello');
