function worldMapChart() {

  var width = 1000,
      height = 600;

  // projection-settings for mercator
  var projection = d3.geo.mercator()
      // where to center the map in degrees
      .center([0, 52])
      // zoomlevel
      .scale(137)
      // map-rotation
      .rotate([0,0]);

  // defines "svg" as data type and "make canvas" command
  var svg = d3.select("#worldMap").append("svg")
      .attr("width", width)
      .attr("height", height);

  // defines "path" as return of geographic features
  var path = d3.geo.path()
      .projection(projection);

  // group the svg layers
  var g = svg.append("g");

  // load data and display the map on the canvas with country geometries
  d3.json("/web/static/data/worldMapChart.json", function(error, topology) {
      g.selectAll("path")
      .data(topojson0.object(topology, topology.objects.countries)
      .geometries)
      .enter()
      .append("path")
      .attr("d", path)
      .style("fill", "#858796");
  });

  // zoom and pan functionality
  /*var zoom = d3.behavior.zoom()
      .on("zoom",function() {
          g.attr("transform","translate("+
              d3.event.translate.join(",")+")scale("+d3.event.scale+")");
          g.selectAll("path")
              .attr("d", path.projection(projection));
    });

  svg.call(zoom)*/

}

function worldPopMap(){

  var width = 1110,
      height = 850;

  // projection-settings for mercator
  var projection = d3.geo.mercator()
      // where to center the map in degrees
      .center([0, 70 ])
      // zoomlevel
      .scale(150)
      // map-rotation
      .rotate([0,0]);

  // defines "svg" as data type and "make canvas" command
  var svg = d3.select("#worldPopMap").append("svg")
      .attr("width", width)
      .attr("height", height)
      .style("margin-left", '4%');

  // defines "path" as return of geographic features
  var path = d3.geo.path()
      .projection(projection);

  // group the svg layers
  var g = svg.append("g");

  // load data and display the map on the canvas with country geometries
  d3.json("/web/static/data/worldMapChart.json", function(error, topology) {
      g.selectAll("path")
      .data(topojson0.object(topology, topology.objects.countries)
      .geometries)
      .enter()
      .append("path")
      .attr("d", path)
      .style("fill", "#858796");
  });

  // zoom and pan functionality
  /*var zoom = d3.behavior.zoom()
      .on("zoom",function() {
          g.attr("transform","translate("+
              d3.event.translate.join(",")+")scale("+d3.event.scale+")");
          g.selectAll("path")
              .attr("d", path.projection(projection));
    });

  svg.call(zoom)*/

}

worldMapChart();
worldPopMap();