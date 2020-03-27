var svg = document.getElementById("vimage");

path = [];

var draw = function(e) {
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  var x = e.offsetX;
  var y = e.offsetY;
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", "10");
  c.setAttribute("fill", "blue");
  c.setAttribute("stroke", "black");
  console.log("trig");
  console.log(c);
  svg.appendChild(c);

  if (path.length == 0) {
    path.push([x,y]);
  }

  var l = document.createElementNS("http://www.w3.org/2000/svg", "line")
  l.setAttribute("x1", path[0][0]);
  l.setAttribute("y1", path[0][1]);
  l.setAttribute("x2", x);
  l.setAttribute("y2", y);
  l.setAttribute("style", "stroke:rgb(255,0,0);stroke-width:2")
  svg.appendChild(l)

  path = [];
  path.push([x,y]);

}

var clear = function(e) {
  while (svg.lastChild) {
    svg.removeChild(svg.lastChild);
  }
  path = [];
}

document.getElementById("clear").addEventListener('click',clear);
svg.addEventListener('click', draw);
