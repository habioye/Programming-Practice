// Prototypal inheritance
function MyCtor(element, data) {
    this.data = data;
    this.element = element;
    element.value = data;
    element.addEventListener("change", this, false);
}

// Implementation of the `eventListener` interface. Just give a handleEvent method.
MyCtor.prototype.handleEvent = function(event) {
    switch (event.type) {
        case "change": this.change(this.element.value);
    }
};


MyCtor.prototype.change = function(value) {
    this.data = value;
    this.element.value = value;
    this.element.innerText = value;
};

var obj = new MyCtor(document.getElementById("foo"), "20");

// simulate some JS based changes.
var i = 0;
setInterval(function() {
    obj.change(parseInt(obj.element.value) + ++i);
    console.log(obj.element.value);
}, 3000);


console.log("check")
