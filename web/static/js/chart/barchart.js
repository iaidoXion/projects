function barChart(barChartData) {


var margin = {top: 10, right: 160, bottom: 25, left: 30};

var width = 620 - margin.left - margin.right,
    height = 175 - margin.top - margin.bottom;

var svg = d3.select("#barChart")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


/* Data in strings like it would be if imported from a csv */

var data = [
  { year: "2019", Windows: "10", Linux: "15", Mac: "9" },
  { year: "2020", Windows: "12", Linux: "18", Mac: "11" },
  { year: "2021", Windows: "20", Linux: "12", Mac: "3" }
];

var parse = d3.time.format("%Y").parse;
// console.log(Object.keys(data[0]))

// Transpose the data into layers
var dataset = d3.layout.stack()(["Windows", "Linux", "Mac"].map(function(useOsCount) {
  return data.map(function(d) {
    return {x: parse(d.year), y: +d[useOsCount]};
  });
}));

// Set x, y and colors
var x = d3.scale.ordinal()
  .domain(dataset[0].map(function(d) { return d.x; }))
  .rangeRoundBands([0, width-10], 0.25);

var y = d3.scale.linear()
  .domain([0, d3.max(dataset, function(d) {  return d3.max(d, function(d) { return d.y0 + d.y; });  })])
  .range([height, 0]);

var colors = ["#e18a0a", "#f6a631", "#f8c477"];


// Define and draw axes
var yAxis = d3.svg.axis()
  .scale(y)
  .orient("left")
  .ticks(5)
  .tickSize(0, 0)
  .tickFormat( function(d) { return d } );

var xAxis = d3.svg.axis()
  .scale(x)
  .orient("bottom")
  .tickFormat(d3.time.format("%Y"));

svg.append("g")
  .attr("class", "y axis")
  .call(yAxis);

svg.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + height + ")")
  .call(xAxis);

// Create groups for each series, rects for each segment
var groups = svg.selectAll("g.cost")
  .data(dataset)
  .enter().append("g")
  .attr("class", "cost")
  .style("fill", function(d, i) { return colors[i]; });

var rect = groups.selectAll("rect")
  .data(function(d) { return d; })
  .enter()
  .append("rect")
  .attr("x", function(d) { return x(d.x); })
  .attr("y", function(d) { return y(d.y0 + d.y); })
  .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); })
  .attr("width", x.rangeBand())
  .on("mouseover", function(d, i) {
               d3.select(this)
                 .style("cursor", "pointer")
                 tooltip
                    .html(
                      `<div>${d.y}</div>`
                    )
                    .style("margin-top", (d3.select(this).attr("y")-120 + "px"))
                    .style("margin-left", (d3.select(this).attr("x")-10 + "px"))
                    .style('visibility', 'visible');
            })
            .on("mouseout", function(d) {
                tooltip.style('visibility', 'hidden');
            });

/*legend*/
  var legendItemSize = 9;
  var legendSpacing = 3;
  var xOffset = 0;
  var yOffset = 0;
  var legend = d3
   .select('#barLegend')
   .append('svg')
   .selectAll('.legendItem')
   .data(dataset)

  //Create legend items
  legend
   .enter()
   .append('rect')
   .attr('class', 'legendItem')
   .attr('width', legendItemSize)
   .attr('height', legendItemSize)
   .style("fill", function(d, i) {return colors.slice()[i];})
   .attr('transform',
                (d, i) => {
                    var x = xOffset;
                    var y = yOffset + (legendItemSize + legendSpacing) * i;
                    return `translate(${x}, ${y})`;
                });


  //Create legend labels
  legend
   .enter()
   .append('text')
   .attr('x', xOffset + legendItemSize + 5)
   .attr('y', (d, i) => yOffset + (legendItemSize + legendSpacing) * i + 10)
   .text(function(d, i) {
    switch (i) {
      case 0: return "Windows";
      case 1: return "Linux";
      case 2: return "Mac";
    }
  });




var tooltip = d3
    .select('#barChart')
    .append('div')
    .attr('class', 'd3-tooltip')
    .style('position', 'absolute')
    .style('z-index', '999')
    .style('visibility', 'hidden')
    .style('padding', '10px')
    .style('background', 'rgba(0,0,0,0.6)')
    .style('border-radius', '4px')
    .style('color', '#fff')
    .text('a simple tooltip');

tooltip.append("rect")
  .attr("width", 30)
  .attr("height", 20)
  .attr("fill", "white")
  .style("opacity", 0.5);
tooltip.append("text")
  .attr("x", 15)
  .attr("dy", "1.2em")
  .style("text-anchor", "middle")
  .attr("font-size", "12px")
  .attr("font-weight", "bold");

















// Prep the tooltip bits, initial display is hidden
/*

tooltip.append("rect")
  .attr("width", 30)
  .attr("height", 20)
  .attr("fill", "white")
  .style("opacity", 0.5);

tooltip.append("text")
  .attr("x", 15)
  .attr("dy", "1.2em")
  .style("text-anchor", "middle")
  .attr("font-size", "12px")
  .attr("font-weight", "bold");
*/


        /*var tooltip = d3
                    .select('#barChart')
                    .append('div')
                    .attr('class', 'd3-tooltip')
                    .style('position', 'absolute')
                    .style('z-index', '999')
                    .style('visibility', 'hidden')
                    .style('padding', '10px')
                    .style('background', 'rgba(0,0,0,0.6)')
                    .style('border-radius', '4px')
                    .style('color', '#fff')
                    .text('a simple tooltip');



        var svgWidth = 400;
        var svgHeight = 130;

        var heightPad = 20;
        var widthPad = 22;
        var marginTip = -21;

        var svg = d3.select("#barChart")
            .append("svg")
            .attr("width", svgWidth + (widthPad * 2))
            .attr("height", svgHeight + (heightPad * 2))
            .append("g")
            .attr("transform", "translate(" + widthPad + "," + heightPad + ")");

        //Set up scales
        var xScale = d3.scale.ordinal()
            .domain(barChartData.map(function(d) { return d.name; }))
            .rangeRoundBands([0, svgWidth], .4);

        var yScale = d3.scale.linear()
            .domain([0, d3.max(barChartData, function (d) { return d.value; })])
            .range([svgHeight,-10]);

       // Create bars
        var rect = svg
            .selectAll('g')
            .data(barChartData)
            .enter().append("rect")
            .attr("x", function (d) { return xScale(d.name) + widthPad; })
            .attr("y", function (d) { return yScale(d.value); })
            .attr("height", function (d) { return svgHeight - yScale(d.value); })
            .attr("width", xScale.rangeBand())
            .attr("fill", "#e08a0b")
            .on("mouseover", function(d, i) {
               d3.select(this)
                 .style("cursor", "pointer")
                 tooltip
                    .html(
                      `<div>${d.value}</div>`
                    )
                    .style("margin-top", (d3.select(this).attr("y")-heightPad + "px"))
                    .style("margin-left", (d3.select(this).attr("x")-marginTip + "px"))
                    .style('visibility', 'visible');
            })
            .on("mouseout", function(d) {
                tooltip.style('visibility', 'hidden');
            });

        // Y axis
        var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient("left");

        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + widthPad + ",0)")
            .call(yAxis)

        // X axis
        var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient("bottom");

        svg.append("g")
            .attr("class", "axis")
            .attr("transform", "translate(" + widthPad + "," + svgHeight + ")")
            .call(xAxis)
            .append("text")
            .attr("x", svgWidth / 2 - widthPad)
            .attr("y", 50)
            .text("")*/

};


