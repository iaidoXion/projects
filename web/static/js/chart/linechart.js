function lineChart() {

//************************************************************
// Data notice the structure
//************************************************************
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


//************************************************************
// Create Margins and Axis and hook our zoom function
//************************************************************
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





//************************************************************
// SVG 객체 생성
//************************************************************
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





//************************************************************
// Create D3 line object and draw data on our SVG object
//************************************************************
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




//************************************************************
// 주어진 데이터를 기반으로 SVG 객체에 점 그리기
//************************************************************
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






//************************************************************
// Zoom specific updates
//************************************************************
function zoomed() {
	svg.select(".x.axis").call(xAxis);
	svg.select(".y.axis").call(yAxis);
	svg.selectAll('path.line').attr('d', line);

	points.selectAll('circle').attr("transform", function(d) {
		return "translate(" + x(d.point.x) + "," + y(d.point.y) + ")"; }
	);
}







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