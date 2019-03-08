const EventEmitter = require('events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

myEmitter.on('event', function(a, b) {
  setImmediate(() => {
    console.log('this happens asynchronously');
  });
  function cb(){
    console.log('processed in next iteration',a,b);
  }
  process.nextTick(cb)
  console.log('processed in first iteration',a,b);
});

myEmitter.emit('event', 'Technoetics', 'Club');