# An abstraction that updates both objects

I suppose there are other techniques, but ultimately I'd have an object that holds reference to a related DOM element, and provides an interface that coordinates updates to its own data and its related element.

The `.addEventListener()` provides a very nice interface for this. You can give it an object that implements the `eventListener` interface, and it'll invoke its handlers with that object as the `this` value.

This gives you automatic access to both the element and its related data.

Defining your object

Prototypal inheritance is a nice way to implement this, though not required of course. First you'd create a constructor that receives your element and some initial data.

```javascript

    function MyCtor(element, data) {
        this.data = data;
        this.element = element;
        element.value = data;
        element.addEventListener("change", this, false);
    }
    
```

So here the constructor stores the element and data on properties of the new object. It also binds a change event to the given element. The interesting thing is that it passes the new object instead of a function as the second argument. But this alone won't work.

# Implementing the `eventListener` interface

To make this work, your object needs to implement the eventListener interface. All that's needed to accomplish this is to give the object a handleEvent() method.

That's where the inheritance comes in.



``

    MyCtor.prototype.handleEvent = function(event) {
        switch (event.type) {
            case "change": this.change(this.element.value);
        }
    };
    
    MyCtor.prototype.change = function(value) {
        this.data = value;
        this.element.value = value;
    };


``


There are many different ways in which this could be structured, but for your example of coordinating updates, I decided to make the `change()` method only accept a value, and have the `handleEvent` pass that value instead of the event object. This way the `change()` can be invoked without an event as well.

So now, when the `change` event happens, it'll update both the element and the `.data` property. And the same will happen when you call `.change()` in your JavaScript program.

# Using the code

Now you'd just create the new object, and let it perform updates. Updates in JS code will appear on the input, and change events on the input will be visible to the JS code.

var obj = new MyCtor(document.getElementById("foo"), "20");

    // simulate some JS based changes.
    var i = 0;
    setInterval(function() {
        obj.change(parseInt(obj.element.value) + ++i);
    }, 3000);
    
DEMO: http://jsfiddle.net/RkTMD/
