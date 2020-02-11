var c = document.getElementById("playground");
if (c.getContext) {
  var ctx = c.getContext("2d");
}

path = [];

var draw = function(e) {
	ctx.fillStyle = "#45c2f7";
	//ctx.borderStyle = "#45c2f7";
	var x = e.offsetX;
	var y = e.offsetY;
	ctx.beginPath();
	ctx.ellipse(x, y, 5, 5, 0, 0, 2 * Math.PI);
	ctx.fill();

	if (path.length == 0) {
		path.push([x,y]);
	}
	ctx.moveTo(path[0][0], path[0][1]);
	ctx.lineTo(x, y);
	ctx.stroke();
	path = [];
	path.push([x, y]);
}

var clear = function(e) {
  ctx.clearRect(0,0,c.width,c.height);
	path = [];
}

// clear button
document.getElementById("clear").addEventListener('click', clear);
// anytime canvas is clicked, draw something!
c.addEventListener('click', draw);
