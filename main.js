/**
 * Created by Beni on 2/11/15.
 */

function addListItem() {
    // create a new List Item
    var li = document.createElement("li");
    // create some text
    var things = ['Money', 'Cars', 'Clothes', 'Nature', 'Food', 'Friends', 'Fitness'];
var thing = things[Math.floor(Math.random()*things.length)];
var t = document.createTextNode(thing);
    // assign the text value to the new list item
    li.appendChild(t);
    // get all the elements of class list (which is exactly 1 in this example)
    var ol = document.getElementsByClassName("list");
    // target the one and only element and append the new list item to the existing list
    ol[0].appendChild(li);
}

/* Possible upgrades so it isn't Money everytime but instead a random word from a list

Replace - var t = document.createTextNode("Money");

With:

var things = ['Money', 'Cars', 'Clothes', 'Nature', 'Food', 'Friends', 'Fitness'];
var thing = things[Math.floor(Math.random()*things.length)];
var t = document.createTextNode(thing);

*/