function Person(name) {
    this.name = name;
}

Person.prototype.logName = function() {
    console.log(this.name);
};

var sean = new Person();
sean.logName();
var b = new Person("Ivan");
b.logName();
