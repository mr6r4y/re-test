function Person(first, last) {
  this.first = first;
  this.last = last;
}

Person.prototype.fullname = function(joiner, options) {
  options = options || { order: "western" };
  var first = options.order === "western" ? this.first : this.last;
  var last =  options.order === "western" ? this.last  : this.first;
  return first + (joiner || " ") + last;
};

// Create an unbound version of "fullname", usable on any object with 'first'
// and 'last' properties passed as the first argument. This wrapper will
// not need to change if fullname changes in number or order of arguments.
Person.fullname = function() {
  // Result: Person.prototype.fullname.call(this, joiner, ..., argN);
  return Function.call.apply(Person.prototype.fullname, arguments);
};

var grace = new Person("Grace", "Hopper");

// 'Grace Hopper'
console.log(grace.fullname());


// 'Turing, Alan'
console.log(Person.fullname({ first: "Alan", last: "Turing" }, ", ", { order: "eastern" }));
