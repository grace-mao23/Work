var c = document.getElementById("slate");
if (c.getContext) {
  var ctx = c.getContext("2d");
}

var mode = 0; // 0 os a rectangle, 1 is a dot

var draw = function(e) {
  if (mode == 0) { // rectangle stuff!
    ctx.fillStyle = "#45c2f7";
    ctx.fillRect(e.layerX, e.layerY, 20, 20);
  } else { // dot stuff!
    ctx.fillStyle = "#d400ff";
    ctx.beginPath();
    ctx.ellipse(e.layerX, e.layerY, 5, 5, 0, 0, 2 * Math.PI); // woah, PI
    ctx.fill();
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
