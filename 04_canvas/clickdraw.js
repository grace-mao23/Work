var c = document.getElementById("slate");
if (c.getContext) {
  var ctx = c.getContext("2d");
}

function draw(event) {
  //var px = document.getElementById("x");
  //var py = document.getElementById("y");

  ctx.fillRect(MouseEvent.offsetX, MouseEvent.offsetY, 10, 10);
}
