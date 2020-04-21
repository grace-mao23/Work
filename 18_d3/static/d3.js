// Team hallo - Tammy Chen & Grace Mao
// SoftDev pd9
// K18: Come Up For Air
// 2020-04-21

var renderbtn = document.getElementById('render');
var transitionbtn = document.getElementById('transition');

var svg;
var x,y;
var width = 1000;
var count = 0;

var render = function(e){
    const new_cases = [];

    var i;
    for (i = 0; i < data.length; i++) {
        new_cases.push(data[i][0]);
    };

    console.log(new_cases);

    x = d3.scaleLinear()
              .domain([0, d3.max(new_cases)])
              .range([0, width]);

    y = d3.scaleBand()
              .domain(d3.range(data.length))
              .range([0, 15 * data.length]);

    svg = d3.create("svg")
                  .attr("width", width + 200)
                  .attr("height", y.range()[1])
                  .attr("font-family", "sans-serif")
                  .attr("font-size", "10")
                  .attr("text-anchor", "end");

    const bar = svg.selectAll("g")
                    .data(data)
                    .join("g")
                    .attr("transform", (d, i) => `translate(0,${y(i)})`);

    bar.append("rect")
        .attr("fill", "steelblue")
        .attr("width", function(d) {
          return x(d[0]);
        })
        .attr("height", y.bandwidth() - 1);

    bar.append("text")
        .attr("class", "date")
        .attr("fill", "black")
        .attr("x", d => x(d[0] + 225))
        .attr("y", y.bandwidth() / 2 + 3)
        .attr("dy", "0.35")
        .text(function(d, i) {
            return heading[i];
        });

    bar.append("text")
        .attr("class", "label")
        .attr("fill", "white")
        .attr("x", d => x(d[0] - 25))
        .attr("y", y.bandwidth() / 2 + 3)
        .attr("dy", "0.35")
        .text(function(d) {
            return d[0];
        });

    document.getElementsByTagName("body")[0].append(svg.node());

};

var change = function(e){
    count += 1;
    console.log(count)

    const hosp = [];
    if (count % 3 == 1){
      var i;
      for (i = 0; i < data.length; i++) {
          hosp.push(data[i][1]);
      };

      x = d3.scaleLinear()
               .domain([0, d3.max(hosp)])
               .range([0, width]);

      console.log(x(data[0][1]));

      svg.selectAll("rect")
          .transition()
          .attr("width", function(d) {
                return x(d[1]);
          });

      svg.selectAll(".label")
          .transition()
          .attr("x", d => x(d[1] - 10))
          .text(function(d) {
            return d[1];
          });

      svg.selectAll(".date")
          .transition()
          .attr("x", d => x(d[1] + 80))
    };

    if (count % 3 == 2){
      var i;
      for (i = 0; i < data.length; i++) {
          hosp.push(data[i][2]);
      };

      x = d3.scaleLinear()
               .domain([0, d3.max(hosp)])
               .range([0, width]);

      //console.log(x(data[0][2]));

      svg.selectAll("rect")
          .transition()
          .attr("width", function(d) {
                return x(d[2]);
          });

      svg.selectAll(".label")
          .transition()
          .attr("x", d => x(d[2] - 10))
          .text(function(d) {
            return d[2];
          });

      svg.selectAll(".date")
          .transition()
          .attr("x", d => x(d[2] + 80))
    };

    if (count % 3 == 0){
      var i;
      for (i = 0; i < data.length; i++) {
          hosp.push(data[i][0]);
      };

      x = d3.scaleLinear()
               .domain([0, d3.max(hosp)])
               .range([0, width]);

      //console.log(x(data[0][1]));

      svg.selectAll("rect")
          .transition()
          .attr("width", function(d) {
                return x(d[0]);
          });

      svg.selectAll(".label")
          .transition()
          .attr("x", d => x(d[0] - 10))
          .text(function(d) {
            return d[0];
          });

      svg.selectAll(".date")
          .transition()
          .attr("x", d => x(d[0] + 80))
    };
};

renderbtn.addEventListener('click', render);
transitionbtn.addEventListener('click', change);