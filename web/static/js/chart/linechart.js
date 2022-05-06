function lineChart() {

var data = [{
    name: "A",
    values: [{
        date: "2021-10-01",
        price: "0"
      },
      {
        date: "2021-10-02",
        price: "400"
      },
      {
        date: "2021-10-03",
        price: "1000"
      },
      {
        date: "2021-10-04",
        price: "700"
      },
      {
        date: "2021-10-05",
        price: "550"
      }
    ]
  },
  {
    name: "B",
    values: [{
        date: "2021-10-01",
        price: "400"
      },
      {
        date: "2021-10-02",
        price: "1000"
      },
      {
        date: "2021-10-03",
        price: "300"
      },
      {
        date: "2021-10-04",
        price: "1000"
      },
      {
        date: "2021-10-05",
        price: "900"
      }
    ]
  },
  {
    name: "C",
    values: [{
        date: "2021-10-01",
        price: "300"
      },
      {
        date: "2021-10-02",
        price: "200"
      },
      {
        date: "2021-10-03",
        price: "100"
      },
      {
        date: "2021-10-04",
        price: "200"
      },
      {
        date: "2021-10-05",
        price: "1000"
      }
    ]
  },
  {
    name: "D",
    values: [{
        date: "2021-10-01",
        price: "800"
      },
      {
        date: "2021-10-02",
        price: "500"
      },
      {
        date: "2021-10-03",
        price: "400"
      },
      {
        date: "2021-10-04",
        price: "700"
      },
      {
        date: "2021-10-05",
        price: "600"
      }
    ]
  }

];
const margin = 30;
const width = 450 - margin;
const height = 147;
var duration = 100;
var lineOpacity = "0.4";
var lineOpacityHover = "0.9";
var otherLinesOpacityHover = "0.1";
var lineStroke = "2px";
var lineStrokeHover = "2.5px";
var circleOpacity = '0.85';
var circleOpacityOnLineHover = "0.25"
var circleRadius = 3;
var circleRadiusHover = 6;
/* Format Data */
var parseDate = d3.time.format("%Y-%m-%d");
data.forEach(function(d) {
  d.values.forEach(function(d) {
    d.date = parseDate.parse(d.date);
    d.price = +d.price;
  });
});
/* Scale */
var xScale = d3.time.scale()
  .domain(d3.extent(data[0].values, d => d.date))
  .range([0, width - margin]);
var yScale = d3.scale.linear()
  .domain([0, d3.max(data[0].values, d => d.price)])
  .range([height - margin, 0]);
// var color = d3.scale.ordinal(d3.schemeCategory10);
var color = d3.scale.category10();
/* Add SVG */
const svg = d3.select("#lineChart")
  .style("margin-left", '3%')
  .append('svg')
  .attr("width", (width + margin) + "px")
  .attr("height", (height + margin) + "px")
  .append('g')
  .attr("transform", `translate(${margin}, ${margin})`);
/* Add line into SVG */
var line = d3.svg.line()
  .x(d => xScale(d.date))
  .y(d => yScale(d.price));
let lines = svg.append('g')
  .attr('class', 'lines');
lines.selectAll('.line-group')
  .data(data).enter()
  .append('g')
  .attr('class', 'line-group')
  .on("mouseover", function(d, i) {
    svg.append("text")
      .attr("class", "title-text")
      .style("fill", color(i))
      .text(d.name)
      .attr("text-anchor", "middle")
      .attr("x", (width - margin) / 2)
      .attr("y", 5);
  })
  .on("mouseout", function(d) {
    svg.select(".title-text").remove();
  })
  .append('path')
  .attr('class', 'line')
  .attr('d', d => line(d.values))
  .style('stroke', (d, i) => color(i))
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
/* Add circles in the line */
lines.selectAll("circle-group")
  .data(data).enter()
  .append("g")
  .style("fill", (d, i) => color(i))
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
      .attr("x", d => xScale(d.date) + 5)
      .attr("y", d => yScale(d.price) - 10);
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
  .attr("transform", `translate(0, ${height-margin})`)
  .call(xAxis.ticks(d3.time.day));
svg.append("g")
  .attr("class", "y axis")
  .call(yAxis)
  .append('text')
  .attr("y", 15)
  .attr("transform", "rotate(-90)")
  .attr("fill", "#000")
  .attr('text-anchor', 'middle')
















/*

/*/
/************************************************************
// Data notice the structure
/*/
/************************************************************
var data = 	[
	[{'x':1,'y':0},{'x':2,'y':500},{'x':3,'y':100},{'x':4,'y':0},{'x':5,'y':600}],
	[{'x':1,'y':100},{'x':2,'y':600},{'x':3,'y':200},{'x':4,'y':100},{'x':5,'y':700}],
	[{'x':1,'y':200},{'x':2,'y':700},{'x':3,'y':890},{'x':4,'y':200},{'x':5,'y':800}],
	[{'x':1,'y':300},{'x':2,'y':800},{'x':3,'y':800},{'x':4,'y':300},{'x':5,'y':900}],
	[{'x':1,'y':400},{'x':2,'y':900},{'x':3,'y':990},{'x':4,'y':400},{'x':5,'y':1000}]
]

var colors = [
	'#e08a0b',
	'#df7454',
	'#f4c17c',
	'#ED8953'
]


/*/
/************************************************************
// Create Margins and Axis and hook our zoom function
/*/
/************************************************************
var margin = {top: 20, right: 50, bottom: 30, left: 50},
    width = 390,
    height = 120;
var x = d3.scale.linear()
    .domain([1, 5])
    .range([0, width]);


var y = d3.scale.linear()
    .domain([0, 1000])
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
	.tickSize(-height)
	.tickPadding(10)
	.tickSubdivide(true)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
	.tickPadding(10)
	.tickSize(-width)
	.tickSubdivide(true)
    .orient("left");

var zoom = d3.behavior.zoom()
    .x(x)
    .y(y)
    .scaleExtent([1, 10])
    .on("zoom", zoomed);





/*/
/************************************************************
// SVG 객체 생성
/*/
/************************************************************
var svg = d3.select("#lineChart").append("svg")
	.call(zoom)
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
	.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

svg.append("g")
    .attr("class", "y axis")
    .call(yAxis);

svg.append("g")
	.attr("class", "y axis")
	.append("text")
	.attr("class", "axis-label")
	.attr("transform", "rotate(-90)")
	.attr("y", (-margin.left) + 10)
	.attr("x", -height/2)
	.text('');

svg.append("clipPath")
	.attr("id", "clip")
	.append("rect")
	.attr("width", width)
	.attr("height", height);





/*/
/************************************************************
// Create D3 line object and draw data on our SVG object
/*/
/************************************************************
var line = d3.svg.line()
    .interpolate("linear")
    .x(function(d) { return x(d.x); })
    .y(function(d) { return y(d.y); });

svg.selectAll('.line')
	.data(data)
	.enter()
	.append("path")
    .attr("class", "line")
	.attr("clip-path", "url(#clip)")
	.attr('stroke', function(d,i){
		return colors[i%colors.length];
	})
    .attr("d", line);




/*/
/************************************************************
// 주어진 데이터를 기반으로 SVG 객체에 점 그리기
/*/
/************************************************************
var points = svg.selectAll('.dots')
	.data(data)
	.enter()
	.append("g")
    .attr("class", "dots")
	.attr("clip-path", "url(#clip)");

points.selectAll('.dot')
	.data(function(d, index){
		var a = [];
		d.forEach(function(point,i){
			a.push({'index': index, 'point': point});
		});
		return a;
	})
	.enter()
	.append('circle')
	.attr('class','dot')
	.attr("r", 2.5)
	.attr('fill', function(d,i){
		return colors[d.index%colors.length];
	})
	.attr("transform", function(d) {
		return "translate(" + x(d.point.x) + "," + y(d.point.y) + ")"; }
	);






/*/
/************************************************************
// Zoom specific updates
/*/
/************************************************************
function zoomed() {
	svg.select(".x.axis").call(xAxis);
	svg.select(".y.axis").call(yAxis);
	svg.selectAll('path.line').attr('d', line);

	points.selectAll('circle').attr("transform", function(d) {
		return "translate(" + x(d.point.x) + "," + y(d.point.y) + ")"; }
	);
}

*/






    /*const width = 465;
    const height = 170;
    const margin = {top: 10, right: 10, bottom: 20, left: 40};
    const data = [
      //{date: new Date('2021-05'), value: 100},
      //{date: new Date('2021-06'), value: 200},
      //{date: new Date('2021-07'), value: 300},
      //{date: new Date('2021-08'), value: 250},
      //{date: new Date('2021-09'), value: 350},
      //{date: new Date('2021-10'), value: 450},
      {date: new Date('2021-11-30'), value: 600},
      {date: new Date('2021-12-31'), value: 350},
      {date: new Date('2022-01-'), value: 480},
      {date: new Date('2022-02'), value: 960},
      {date: new Date('2022-03'), value: 100},
      {date: new Date('2022-04'), value: 500},
    ];

    const x = d3.scaleTime()
      .domain(d3.extent(data, d => d.date))
      .range([margin.left, width - margin.right]);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.value)]).nice()
      .range([height - margin.bottom, margin.top]);

    const xAxis = g => g
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(x).ticks(width / 90).tickSizeOuter(0));

    const yAxis = g => g
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(y))
      .call(g => g.select(".domain").remove())
      .call(g => {
        return g.select(".tick:last-of-type text").clone()
          .attr("x", 3)
          .attr("text-anchor", "start")
         // .attr("font-weight", "bold")
          .attr("font-size", '10px')
          //.text('Count')
        });

    const line = d3.line()
      .defined(d => !isNaN(d.value))
      .x(d => x(d.date))
      .y(d => y(d.value));

    const svg = d3.select('#lineChart').append('svg').style('width', width).style('height', height);
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "#e08a0b")
      .attr("stroke-width", 2)
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("d", line);
    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);
    svg.node();*/
}
lineChart();