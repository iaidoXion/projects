function lineChart(lineChartData) {
const dataMap = lineChartData.map(d => d.asset);
let lineDataName = [...new Set(dataMap)];

var sumstat = d3v4.nest()
.key(function(d) { return d.asset;})
.entries(lineChartData);

var lineGroup = JSON.stringify(sumstat);

const margin = 30;
const marginTop = 13;
const width = 450 - margin;
const height = 140;
var duration = 100;
var lineOpacity = "1";
var lineOpacityHover = "1";
var otherLinesOpacityHover = "0.1";
var lineStroke = "3px";
var lineStrokeHover = "4px";
var circleOpacity = '0.85';
var circleOpacityOnLineHover = "0.25"
var circleRadius = 3;
var circleRadiusHover = 6;
/* Format Data */
var parseDate = d3.time.format("%Y-%m-%d");
lineChartData.forEach(function(d) {
    d.date = parseDate.parse(d.date);
    d.price = +d.price;
    d.name = +d.name;
});

// var yMax = Math.max(...lineChartData.flatMap(({values}) => values).map(({price}) => price));
var yMax = Math.max(...lineChartData.map(function(d){return d.price;}));
var yMin = Math.min(...lineChartData.map(function(d){return d.price;}));
/* Scale */
var xScale = d3.time.scale()
  .domain(d3.extent(lineChartData, d => d.date))
  .range([0, width - margin]);
var yScale = d3.scale.linear()
  .domain([yMin, yMax])
  .range([height - marginTop, 0]);

var color = ["#e08a0b","#f5a631","#f8c477","#f2cd96"];
/* Add SVG */
const svg = d3.select("#lineChart")
  .style("margin-left", '3%')
  .append('svg')
  .attr("width", (width + margin) + "px")
  .attr("height", (height + marginTop) + "px")
  .append('g')
  .attr("transform", `translate(${margin}, ${marginTop})`);
/* Add line into SVG */
var line = d3.svg.line()
  .x(d => xScale(d.date))
  .y(d => yScale(d.price));

let lines = svg.append('g')
  .attr('class', 'lines');
lines.selectAll('.line-group')
  .data(sumstat).enter()
  .append('g')
  .attr('class', 'line-group')
  .on("mouseover", function(d, i) {
    svg.append("text")
      .attr("class", "title-text")
      .style("fill", "#858796")
      .style("font-weight", "bold")
      .text(d.key)
      .attr("text-anchor", "middle")
      .attr("x", (width - 225))
      .attr("y", (height-(height+5)));
  })
  .on("mouseout", function(d) {
    svg.select(".title-text").remove();
  })
  .append('path')
  .attr('class', 'line')
  .attr('d', d => line(d.values))
  .style('stroke', function(d,i) { return color[i]; })
  .style('opacity', lineOpacity)
  .on("mouseover", function(d) {
    d3.selectAll('.line')
      .style('opacity', otherLinesOpacityHover);
    d3.selectAll('.circle')
      .style('opacity', circleOpacityOnLineHover);
    d3.select(this)
      .style('opacity', lineOpacityHover)
      .style("stroke-width", lineStrokeHover)
      .style("cursor", "pointer");
  })
  .on("mouseout", function(d) {
    d3.selectAll(".line")
      .style('opacity', lineOpacity);
    d3.selectAll('.circle')
      .style('opacity', circleOpacity);
    d3.select(this)
      .style("stroke-width", lineStroke)
      .style("cursor", "none");
  });
/*legend*/
 /* var legendItemSize = 9;
  var legendSpacing = 3;
  var xOffset = 0;
  var yOffset = 0;
  var legend = d3
   .select('#lineLegend')
   .append('svg')
   .selectAll('.legendItem')
   .data(lineDataName)

  //Create legend items
  legend
   .enter()
   .append('rect')
   .attr('class', 'legendItem')
   .attr('width', legendItemSize)
   .attr('height', legendItemSize)
   .style('fill', function(d,i) { return color[i]; })
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
   .text(function(d) { return d });*/

/* Add circles in the line */
lines.selectAll("circle-group")
  .data(sumstat).enter()
  .append("g")
  .style("fill", function(d,i) { return color[i]; })
  .selectAll("circle")
  .data(d => d.values).enter()
  .append("g")
  .attr("class", "circle")
  .on("mouseover", function(d) {
    d3.select(this)
      .style("cursor", "pointer")
      .append("text")
      .attr("class", "text")
      .text(`${d.price}`)
      .style("fill", "#858796")
      .style("font-weight", "bold")
      .attr("x", d => xScale(d.date) + 5)
      .attr("y", d => yScale(d.price) - 5);
  })
  .on("mouseout", function(d) {
    d3.select(this)
      .style("cursor", "none")
      .transition()
      .duration(duration)
      .selectAll(".text").remove();
  })
  .append("circle")
  .attr("cx", d => xScale(d.date))
  .attr("cy", d => yScale(d.price))
  .attr("r", circleRadius)
  .style('opacity', circleOpacity)
  .on("mouseover", function(d) {
    d3.select(this)
      .transition()
      .duration(duration)
      .attr("r", circleRadiusHover);
  })
  .on("mouseout", function(d) {
    d3.select(this)
      .transition()
      .duration(duration)
      .attr("r", circleRadius);
  });
var xAxis = d3.svg.axis().scale(xScale)
  .orient("bottom").tickFormat(d3.time.format("%Y-%m-%d")).tickSize(1);
var yAxis = d3.svg.axis().scale(yScale)
  .orient("left").tickSize(1);
svg.append("g")
  .attr("class", "x axis")
  .attr("transform", `translate(0, ${height-marginTop})`)
  .call(xAxis.ticks(d3.time.day));
svg.append("g")
  .attr("class", "y axis")
  .call(yAxis)
  .append('text')
  .attr("y", 15)
  .attr("transform", "rotate(-90)")
  .attr("fill", "#000")
  .attr('text-anchor', 'middle');
}

