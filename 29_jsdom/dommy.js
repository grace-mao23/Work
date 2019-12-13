// Grace Mao and Derek Leung
// SoftDev1 pd9
// K29 -- Sequential Progression III
// 2019-12-12

//var b = document.getElementById("error");
//b.addEventListener('click', function(e) { console.log(e) });

var changeHeading = function(e) { // e is an event
  var h = document.getElementById("h");
  if (e.type == 'mouseover') {
    h.innerHTML = e.target.innerHTML;
  } else {
    h.innerHTML = "Hello World!";
  }
};

var removeItem = function(e) {
  e.target.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('mouseover', changeHeading);
  lis[i].addEventListener('mouseout', changeHeading);
  lis[i].addEventListener('click', removeItem);
};

var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener('mouseover', changeHeading);
  item.addEventListener('mouseout', changeHeading);
  item.addEventListener('click', removeItem);
  list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
  if (n < 2) {
    return 1;
  } else {
    return fib(n-1) + fib(n-2);
  }
};

var fibs = {
  nums: [],
  add: function() {
    var ans;
    if (this.nums.length < 2) { // if the length is less than 2, the statement in else won't work
      ans = fib(this.nums.length);
    } else { // append the next fibonacci number into the list
      ans = this.nums[this.nums.length - 1] + this.nums[this.nums.length - 2];
    }
    this.nums.push(ans);
    return ans;
  }
}

var addFib = function(e) {
  console.log(e);
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  item.innerHTML = fibs.add();
  list.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener('click', addFib);
