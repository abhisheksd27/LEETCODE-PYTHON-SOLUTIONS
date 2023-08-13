/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count=init
    return {
        increment: function(){
            return count=count+1
        },
        reset: function(){
            return count=init
        },
        decrement: function(){
            return count=count-1
        }
    }
};


  const counter = createCounter(5)
  counter.increment(); // 6
  counter.reset(); // 5
  counter.decrement(); // 4
