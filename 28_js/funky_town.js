// Grace Mao and Leia Park
// SoftDev1 pd9
// K27 -- Sequential Progression
// 2019-12-10

var fact = function(n) {
  if (n === 1) {
    return 1;
  }
  return n * fact(n-1);
}

var fibonacci = function(n) {
  if (n === 0) {
    return 0;
  }
  if (n <= 2) {
    return 1;
  }
  return fib(n-1) + fib(n-2);
}

var x = document.getElementById("fact");
var func = function() { console.log(fact(5)) };
x.addEventListener('click', func);

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

var students = ["Joe", "Jane", "Bob", "Mr. Mykolyk", "Grace", "Leia", "Jude", "Connor", "Sophie"];

var randomStudent = function() {
  var x = Math.random() * students.length;
  x = Math.floor(x);
  return students[x];
}
