// Grace Mao and Derek Leung
// SoftDev1 pd9
// K29 -- Sequential Progression III
// 2019-12-12

/*Upon button push, add an element to the list.
When the mouse goes over an item in the list, change the heading at the top to contain the text of the item.
When the mouse is no longer over an item in the list, change the heading back to "Hello World!"
When an item on the list is clicked, remove it from the DOM.*/

var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e;
};

var removeItem = function(e) {
  e.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('mouseover', function(lis[i]) { changeHeading(lis[i]) });
  lis[i].addEventListener('mouseout', changeHeading("Hello World!"));
  lis[i].addEventListener('click', function(lis[i]) { removeItem(lis[i]) });
};
/*
var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  lis[i].addEventListener('mouseover', changeHeading(lis[i].innerHTML));
  lis[i].addEventListener('mouseout', changeHeading("Hello World!"));
  lis[i].addEventListener('click', removeItem(lis[i]));
  list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);*/

var b = document.getElementById("error");
b.addEventListener('click', function(e) { console.log(e) });
