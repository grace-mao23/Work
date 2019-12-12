// Grace Mao and Jason Zheng
// SoftDev1 pd9
// K28 -- Sequential Progression II
// 2019-12-11

var result = function(id, call, text) {
  var a = document.getElementById(id);
  var func = function() {
    console.log(call);
    var p = document.createElement("P");
    p.innerText = text + call;
    document.body.appendChild(p);
  }
  a.addEventListener('click', func);
}

var fact = function(n) {
  if (n === 1) {
    return 1;
  }
  return n * fact(n-1);
}

result("fact", fact(5), "5! is ");

var fibonacci = function(n) {
  if (n === 0) {
    return 0;
  }
  if (n <= 2) {
    return 1;
  }
  return fibonacci(n-1) + fibonacci(n-2);
}

result("fib", fibonacci(8), "The 8th Fibonacci number is ");

var gcd = function(a, b) {
  if (a <= 1) {
    return a;
  }
  if (b <= 1) {
    return b;
  }
  if (a === b) {
    return a;
  }
  if (a > b) {
    return gcd(a - b, b);
  }
  return gcd(a, b - a);
}

result("gcd", gcd(96, 108), "The GCD of 108 and 96 is ");

var students = ["Joe", "Jane", "Bob", "Mr. Mykolyk", "Grace", "Leia", "Jude", "Connor", "Sophie"];

var randomStudent = function() {
  var x = Math.random() * students.length;
  x = Math.floor(x);
  return students[x];
}

// NOTE: function result() not used in order to generate new random student with every click
var a = document.getElementById("randS");
var func = function() {
  var temp = randomStudent();
  console.log(temp);
  var p = document.createElement("P");
  p.innerText = "The random student chosen is " + temp;
  document.body.appendChild(p);
}
a.addEventListener('click', func);
