var svg = document.getElementById("vimage");
var btn = document.getElementById("clear");

var draw = function(e) {
  if (e.target == svg) {
    console.log(e.target)
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    var x = e.offsetX;
    var y = e.offsetY;
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", "10");
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    c.addEventListener('click', circle);
    svg.appendChild(c);
  }
}

var circle = function(e){
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "violet");
  }
  else if (e.target.getAttribute("fill") == "violet") {
    var x = Math.floor(Math.random() * 500);
    var y = Math.floor(Math.random() * 500);
    e.target.setAttribute("cx", x);
    e.target.setAttribute("cy", y);
    e.target.setAttribute("fill", "blue");
  }
}

var clear = function(e){
  while (svg.lastChild){
    svg.removeChild(svg.lastChild);
  }
}

btn.addEventListener('click', clear);
svg.addEventListener('click', draw);
