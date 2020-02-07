var c = document.getElementById("slate");
if (c.getContext) {
  var ctx = c.getContext("2d");
}

// while some actions may have a default reaction, e.preventDefault()
// would block that. For example, if we set draw to the default action
// when a user clicks on the page, we can use preventDefault() to
// block the drawing if they aren't over the canvas

var mode = 0; // 0 os a rectangle, 1 is a dot

var draw = function(e) {
  if (mode == 0) { // rectangle stuff!
    ctx.fillStyle = "#45c2f7";
    ctx.fillRect(e.offsetX, e.offsetY, 20, 20);
    // offsetX and offsetY returns the mouse cursor relative to the target
    // in this case, the target is the canvas
  } else { // dot stuff!
    ctx.fillStyle = "#d400ff";
    ctx.beginPath(); // begin path simply tells the program to start drawing
    // without it, sometimes the program will connect dots without knowing where to start
    ctx.ellipse(e.offsetX, e.offsetY, 5, 5, 0, 0, 2 * Math.PI); // woah, PI
    ctx.fill(); // every ellipse needs to be filled
  }
}

var clear = function(e) {
  ctx.clearRect(0,0,c.width,c.height);
}

var toggle = function(e) {
  if (mode == 0) {
    mode = 1;
  } else {
    mode = 0;
  }
  update(e);
}

var update = function(e) {
  var words = document.getElementById("mode");
  if (mode == 0) {
    words.innerHTML = "rectangle";
  } else {
    words.innerHTML = "dot";
  }
}

// clear button
document.getElementById("clear").addEventListener('click', clear);
// toggle button
document.getElementById("toggle").addEventListener('click', toggle);
// anytime canvas is clicked, draw something!
c.addEventListener('click', draw);
