function expandWorldMapChart(worldMapData, mapNetwork) {
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
  var svg = d3.select("#popExpandWorld").append("svg")
      .attr("width", width)
      .attr("height", height);

  // defines "path" as return of geographic features
  var path = d3.geo.path()
      .projection(projection);

  // group the svg layers
  var g = svg.append("g").attr("id", "map"),
  places = svg.append("g").attr("id", "places");

var graticule = d3.geo.graticule()
    .step([5, 5]);

svg.append("path")
    .datum(graticule)
    .attr("class", "graticule")
    .attr("d", path);

svg.selectAll("circle")
    .data(worldMapData)
    .enter()
    .append("circle")
    .attr("class","dot")
    .attr("transform",translateCircle)
    .attr("r",4)
    .style("fill", "#e08a0b");

function translateCircle(datum, index)
          {
            return "translate(" +  projection([datum.y, datum.x]) + ")";
          };

setInterval(function(){
	      worldMapData.forEach(function(datum)
          {
			  svg
			  	.append("circle")
			      .attr("class", "ring")
			      .attr("transform", translateCircle(datum))
			      .attr("r", 1)
			      .style("fill", "#e06f0b")
			      .style("opacity", "0.3")
			      .style("fill-opacity", "0.3")
			    .transition()
			      .ease("linear")
			      .duration(2000)
			      .style("stroke-opacity", 1e-6)
			      .style("stroke-width", 1)
			      .style("stroke", "e06f0b")
			      .attr("r", 30)
			      .remove();
          })
      }, 800);

  // load data and display the map on the canvas with country geometries
  d3.json("/web/static/data/mapTopo/world.json", function(error, topology) {
      g.selectAll("path")
      .data(topojson0.object(topology, topology.objects.countries)
      .geometries)
      .enter()
      .append("path")
      .attr("d", path)
      .style("fill", "#d5d6dd");
  });

  var simulation = d3v4.forceSimulation()
    .force("link", d3v4.forceLink().distance(d => d.distance).id(function(d) { return d.id; }))
    .force("charge", d3v4.forceManyBody().strength(-170));
   /* .force("center", d3v4.forceCenter(width / 2, height / 2));*/

  mapNetwork.forEach(function(graph) {

      var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
          .attr("stroke-width", "1.7")
          .style("stroke", "#e18a0a");

      var fillCircle = function(g){
            if(g == "Ncrd"){
                return "/web/static/img/dashboard/ncrd.png";
            }else if(g=="Ncalpha"){
                return "/web/static/img/dashboard/ncalpha.png";
            }
        };

      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

      function ticked() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("transform", function(d) {
              return "translate(" + d.x + "," + d.y + ")";
            })
      };

      //make arrow
      svg.append("svg:defs").append("svg:marker")
        .attr("id", "arrow")
        .attr("viewBox", "0 -5 10 10")
        .attr('refX', 18)//so that it comes towards the center.
        .attr("markerWidth", 7)
        .attr("markerHeight", 7)
        .attr("orient", "auto-start-reverse")
      .append("svg:path")
        .attr("d", "M0,-5L10,0L0,5")
        .style( "fill", "#e18a0a" );

       links = svg.selectAll( "line.link" )
        .data( graph.links )
        .enter().append( "path" )//append path
        .attr( "class", "link" )
        .style( "stroke", "#e18a0a" )
        .attr('marker-start', (d) => "url(#arrow)")//attach the arrow from defs
        .style( "stroke-width", 1.5 );

       links
        .attr( "d", (d) => "M" + d.source.x + "," + d.source.y + ", " + d.target.x + "," + d.target.y);

        var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
          .on("mouseover", function(d) {
            d3.select(this)
                .style("cursor", "pointer")
          });
        var circles = node.append("image")
        .attr('width',80)
        .attr('height',80)
        .attr('x', -40)
        .attr('y', -40)
        .attr("xlink:href", function(d) { return fillCircle(d.id); })
        .style("filter", "url(#world-drop-shadow)");

        node.append("title")
        .text("- Assets unchanged in number of listen port\n- Assets without established ports\n- Assets without login history");
    /*      .text(function(d) { return d.name; });*/

        var dropShadowFilter = svg.append('svg:filter')
          .attr('id', 'world-drop-shadow')
          .attr('filterUnits', "userSpaceOnUse")
          .attr('width', '250%')
          .attr('height', '250%');
        dropShadowFilter.append('svg:feGaussianBlur')
          .attr("in", "SourceAlpha")
          .attr('stdDeviation', 2)
          .attr('result', 'blur-out');
        dropShadowFilter.append('svg:feColorMatrix')
          .attr("type", "matrix")
          .attr("values", ".33 .33 .33 0 0  .33 .33 .33 0 0  .33 .33 .33 0 0  0 0 0 .5 0");
        dropShadowFilter.append('svg:feOffset')
          .attr('in', 'color-out')
          .attr('dx', 4)
          .attr('dy', 4)
          .attr('result', 'the-shadow');
        dropShadowFilter.append('svg:feBlend')
          .attr('in', 'SourceGraphic')
          .attr('in2', 'the-shadow');

    });
};


function expandKoreaMapChart(worldMapData, mapNetwork) {
    var koreaMapWidth = 0;
    var koreaMapHeight = 0;

    var initialScale = 4900,
        initialX = 0,
        initialY = 0,
        centered,
        labels;
    koreaMapWidth  = initialScale / 6;
    koreaMapHeight = initialScale / 6;
    initialX = initialScale * -2.12 - 80;
    initialY = initialScale * 0.75 - 80;
    var mapSvg = d3.select("#popExpandKorea").append("svg")
        .attr("width", koreaMapWidth)
        .attr("height", koreaMapHeight)
        .attr('id', 'koreaMap');
    //    .call(zoom);
    var koreaProjection, koreaPath, koreaMap,
        placeProjection, placePath, placeMap,
    /*var zoom;*/

    koreaProjection    = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    placeProjection    = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    koreaPath    = d3.geo.path().projection(koreaProjection);
    placePath    = d3.geo.path().projection(placeProjection);
    koreaMap    = mapSvg.append("g").attr("id", "maps");
    placeMap    = mapSvg.append("g").attr("id", "places");
    // zoom and pan //

    var koreaProjection = d3.geo.mercator()
        .center([113, -3])
        .scale(1275)
        .translate([koreaMapWidth / 2, koreaMapHeight / 2])
        .clipExtent([[0, 0], [koreaMapWidth, koreaMapHeight]])
        .precision(.1);

    var path = d3.geo.path()
        .projection(koreaProjection);

    var graticule = d3.geo.graticule()
        .step([5, 5]);

    mapSvg.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);

mapSvg.selectAll("circle")
    .data(worldMapData)
    .enter()
    .append("circle")
    .attr("class","dot")
    .attr("transform",translateCircle)
    .attr("r",4)
    .style("fill", "#e08a0b")
    .style("stroke", "#e18a0a");


var imgX = [40, -120, 40, -120, 60];
var imgY = [40, -120, -120, 40, 60];

var centerIMG = ["/web/static/img/dashboard/group_orange-1.png",
                 "/web/static/img/dashboard/group_orange-2.png",
                 "/web/static/img/dashboard/group_orange-3.png",
                 "/web/static/img/dashboard/group_orange-4.png"]


var node = mapSvg.append("g")
            .attr("class", "nodes")
            .selectAll("g")
            .data(worldMapData)
            .enter().append("g")
            .attr("transform", translateCircle)
            .on("mouseover", function(d) {
            d3.select(this)
                .style("cursor", "pointer")
            });

var circles = node.append("image")
            .attr('width',80)
            .attr('height',80)
            .attr('x', function(d,i){return imgX[i];})
            .attr('y', function(d,i){return imgY[i];})
            .attr("xlink:href", function(d,i){return centerIMG[i];});



/*            .style("filter", "url(#seoul-drop-shadow)");

var dropShadowFilter = mapSvg.append('svg:filter')
          .attr('id', 'seoul-drop-shadow')
          .attr('filterUnits', "userSpaceOnUse")
          .attr('width', '250%')
          .attr('height', '250%');
        dropShadowFilter.append('svg:feGaussianBlur')
          .attr("in", "SourceAlpha")
          .attr('stdDeviation', 2)
          .attr('result', 'blur-out');
        dropShadowFilter.append('svg:feColorMatrix')
          .attr("type", "matrix")
          .attr("values", ".33 .33 .33 0 0  .33 .33 .33 0 0  .33 .33 .33 0 0  0 0 0 .5 0");
        dropShadowFilter.append('svg:feOffset')
          .attr('in', 'color-out')
          .attr('dx', 4)
          .attr('dy', 4)
          .attr('result', 'the-shadow');
        dropShadowFilter.append('svg:feBlend')
          .attr('in', 'SourceGraphic')
          .attr('in2', 'the-shadow');*/

function translateCircle(datum, index)
          {
            return "translate(" +  placeProjection([datum.y, datum.x]) + ")";
          };

setInterval(function(){
	      worldMapData.forEach(function(datum)
          {
			  mapSvg
			  	.append("circle")
			      .attr("class", "ring")
			      .attr("transform", translateCircle(datum))
			      .attr("r", 1)
			      .style("fill", "#e06f0b")
			      .style("opacity", "0.3")
			      .style("fill-opacity", "0.3")
			    .transition()
			      .ease("linear")
			      .duration(2000)
			      .style("stroke-opacity", 1e-6)
			      .style("stroke-width", 1)
			      .style("stroke", "e06f0b")
			      .attr("r", 30)
			      .remove();
          })
      }, 800);

    function labelsTransform(d) {
    // 경기도가 서울특별시와 겹쳐서 위치 조정 및 세종특별자치시와 대전광역시 위치 조정
     if (d.properties.code == 31) /* 경기도 */
     { var arr = koreaPath.centroid(d);
       arr[1] += (d3.event && d3.event.scale) ? (d3.event.scale / koreaMapHeight - 40) : (initialScale / koreaMapHeight - 40);
       return "translate(" + arr + ")";
     }
     else if (d.properties.code == 25) /* 대전광역시 */
     { var arr = koreaPath.centroid(d);
       arr[1] += (d3.event && d3.event.scale) ? (d3.event.scale / koreaMapHeight + 5) : (initialScale / koreaMapHeight + 5);
       return "translate(" + arr + ")";
     }
     else if (d.properties.code == 29) /* 세종특별자치시 */
     { var arr = koreaPath.centroid(d);
       arr[1] += (d3.event && d3.event.scale) ? (d3.event.scale / koreaMapHeight + 10) : (initialScale / koreaMapHeight + 10);
       return "translate(" + arr + ")";
     }
     else
     { var arr = koreaPath.centroid(d);
       arr[1] += (d3.event && d3.event.scale) ? (d3.event.scale / koreaMapHeight - 10) : (initialScale / koreaMapHeight - 10);
       return "translate(" + arr + ")";
     }
    }

d3.json("/web/static/data/mapTopo/korea.json", function(json)
    { koreaMap.selectAll("path")
              .data(json.features).enter().append("path")
              .attr("d", koreaPath)
              .attr("id", function(d) { return 'path-'+d.properties.code; });
      labels = koreaMap.selectAll("text")
              .data(json.features).enter().append("text")
              .attr("transform", labelsTransform)
              .attr("id", function(d) { return 'label-'+d.properties.code; })
              .attr('text-anchor', 'middle')
              .attr("dy", ".35em")
              .text(function(d) { return d.properties.name; });
    });
    d3.csv("/web/static/data/placekorea.csv", function(data)
    { /*placeMap.selectAll("circle")
              .data(data).enter().append("circle")
              .attr("cx", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("cy", function(d) { return placeProjection([d.longi, d.lati])[1]; })
              .attr("r", 3)
              .attr("class", "placeCircle")
              .attr("id", function(d) { return d.seno; });*/
      placeMap.selectAll("text")
              .data(data).enter().append("text")
              .attr("x", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("y", function(d) { return placeProjection([d.longi, d.lati])[1] - 5; })
              .attr("class", "placeName")
              .attr("id", function(d) { return d.seno+"name"; })
              .text(function(d) { return d.name; });
    });

/*  var simulation = d3v4.forceSimulation()
    .force("link", d3v4.forceLink().distance(d => d.distance).id(function(d) { return d.id; }));*/

/*koreaNetwork.forEach(function(graph) {
      var link = mapSvg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links);
        .enter().append("line")
        .attr("stroke-width", "1.7")
        .style("stroke", "#e18a0a");



      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

      function ticked() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("transform", function(d) {
              return "translate(" + d.x + "," + d.y + ")";
            })
      }

//make arrow
      mapSvg.append("svg:defs").append("svg:marker")
        .attr("id", "seoul-arrow")
        .attr("viewBox", "0 -5 10 10")
        .attr('refX', -5)
        .attr("markerWidth", 7)
        .attr("markerHeight", 7)
        .attr("orient", "auto-start-reverse")
      .append("svg:path")
        .attr("d", "M0,-5L10,0L0,5")
        .style( "fill", "#e18a0a" );

       links = mapSvg.selectAll( "line.link" )
        .data( graph.links )
        .enter().append( "path" )
        .attr( "class", "link" )
        .style( "stroke", "#e18a0a" )
        .attr('marker-start', (d) => "url(#seoul-arrow)")
        .style( "stroke-width", 1.5 );

       links
        .attr( "d", (d) => "M" + d.source.x + "," + d.source.y + ", " + d.target.x + "," + d.target.y)

        var node = mapSvg.append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
          .on("mouseover", function(d) {
            d3.select(this)
                .style("cursor", "pointer")
          })
        var circles = node.append("image")
        .attr('width',80)
        .attr('height',80)
        .attr('x', -40)
        .attr('y', -40)
        .attr("xlink:href", function(d,i) {return centerIMG[i];})
        .style("filter", "url(#seoul-drop-shadow)");

        node.append("title")
        .text("- Assets unchanged in number of listen port\n- Assets without established ports\n- Assets without login history");
    /*      .text(function(d) { return d.name; });*/

        /*var dropShadowFilter = mapSvg.append('svg:filter')
          .attr('id', 'seoul-drop-shadow')
          .attr('filterUnits', "userSpaceOnUse")
          .attr('width', '250%')
          .attr('height', '250%');
        dropShadowFilter.append('svg:feGaussianBlur')
          .attr("in", "SourceAlpha")
          .attr('stdDeviation', 2)
          .attr('result', 'blur-out');
        dropShadowFilter.append('svg:feColorMatrix')
          .attr("type", "matrix")
          .attr("values", ".33 .33 .33 0 0  .33 .33 .33 0 0  .33 .33 .33 0 0  0 0 0 .5 0");
        dropShadowFilter.append('svg:feOffset')
          .attr('in', 'color-out')
          .attr('dx', 4)
          .attr('dy', 4)
          .attr('result', 'the-shadow');
        dropShadowFilter.append('svg:feBlend')
          .attr('in', 'SourceGraphic')
          .attr('in2', 'the-shadow');

    });*/

};

function expandSeongnamMap(worldMapData, seongnamNetwork){
    var width = 1880, height = 880;
    var svg = d3.select("#popExpandArea").append("svg").attr("width", width).attr("height", height).style("margin-left", '1%');
    var map = svg.append("g").attr("id", "map"),places = svg.append("g").attr("id", "places");
    var projection = d3.geo.mercator().center([127.1094211519, 37.399]).scale(180000).translate([width/2, height/2]);
    var path = d3.geo.path().projection(projection);

svg.selectAll("circle")
    .data(worldMapData)
    .enter()
    .append("circle")
    .attr("class","dot")
    .attr("transform",translateCircle)
    .attr("r",4)
    .style("fill", "#e08a0b");

function translateCircle(datum, index)
          {
            return "translate(" +  projection([datum.y, datum.x]) + ")";
          };

setInterval(function(){
	      worldMapData.forEach(function(datum)
          {
			  svg
			  	.append("circle")
			      .attr("class", "ring")
			      .attr("transform", translateCircle(datum))
			      .attr("r", 1)
			      .style("fill", "#e06f0b")
			      .style("opacity", "0.3")
			      .style("fill-opacity", "0.3")
			    .transition()
			      .ease("linear")
			      .duration(2000)
			      .style("stroke-opacity", 1e-6)
			      .style("stroke-width", 1)
			      .style("stroke", "e06f0b")
			      .attr("r", 30)
			      .remove();
          })
      }, 800);

    d3.json("/web/static/data/mapTopo/seongnam.json", function(error, data) {
        var features = topojson.feature(data, data.objects.seongnam).features;

        map.selectAll('path').data(features).enter().append('path')
        .attr('class', function(d) { return 'municipality c' + d.properties.code })
        .attr('d', path);

        map.selectAll('text').data(features).enter().append("text")
        .attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
        .attr("dy", ".35em")
        .attr("class", "municipality-label")
        .text(function(d) { return d.properties.sggnm; })
        .style("fill", "#717384")
    });


  var simulation = d3v4.forceSimulation()
    .force("link", d3v4.forceLink().distance(d => d.distance).id(function(d) { return d.id; }))
    .force("charge", d3v4.forceManyBody().strength(-170));

      seongnamNetwork.forEach(function(graph) {
      var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
          .attr("stroke-width", "1.7")
          .style("stroke", "#e18a0a");

      var fillCircle = function(g){
            if(g == "Ncrd"){
                return "/web/static/img/dashboard/ncrd.png";
            }else if(g=="Ncalpha"){
                return "/web/static/img/dashboard/ncalpha.png";
            }
        };

      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

      function ticked() {
        link
            .attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        node
            .attr("transform", function(d) {
              return "translate(" + d.x + "," + d.y + ")";
            })
      }

    //make arrow
          svg.append("svg:defs").append("svg:marker")
            .attr("id", "seongnam-arrow")
            .attr("viewBox", "0 -5 10 10")
            .attr('refX', -28)//so that it comes towards the center.
            .attr("markerWidth", 7)
            .attr("markerHeight", 7)
            .attr("orient", "auto-start-reverse")
          .append("svg:path")
            .attr("d", "M0,-5L10,0L0,5")
            .style( "fill", "#e18a0a" );

           links = svg.selectAll( "line.link" )
            .data( graph.links )
            .enter().append( "path" )//append path
            .attr( "class", "link" )
            .style( "stroke", "#e18a0a" )
            .attr('marker-start', (d) => "url(#seongnam-arrow)")//attach the arrow from defs
            .style( "stroke-width", 1.5 );

           links
            .attr( "d", (d) => "M" + d.source.x + "," + d.source.y + ", " + d.target.x + "," + d.target.y)

        var node = svg.append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
          .on("mouseover", function(d) {
            d3.select(this)
                .style("cursor", "pointer")
          })
        var circles = node.append("image")
        .attr('width',80)
        .attr('height',80)
        .attr('x', 410)
        .attr('y', 100)
        .attr("xlink:href", function(d) { return fillCircle(d.id); })
        .style("filter", "url(#seongnam-drop-shadow)");

        node.append("title")
        .text("- Assets unchanged in number of listen port\n- Assets without established ports\n- Assets without login history");
    /*      .text(function(d) { return d.name; });*/

        var dropShadowFilter = svg.append('svg:filter')
          .attr('id', 'seongnam-drop-shadow')
          .attr('filterUnits', "userSpaceOnUse")
          .attr('width', '250%')
          .attr('height', '250%');
        dropShadowFilter.append('svg:feGaussianBlur')
          .attr("in", "SourceAlpha")
          .attr('stdDeviation', 2)
          .attr('result', 'blur-out');
        dropShadowFilter.append('svg:feColorMatrix')
          .attr("type", "matrix")
          .attr("values", ".33 .33 .33 0 0  .33 .33 .33 0 0  .33 .33 .33 0 0  0 0 0 .5 0");
        dropShadowFilter.append('svg:feOffset')
          .attr('in', 'color-out')
          .attr('dx', 4)
          .attr('dy', 4)
          .attr('result', 'the-shadow');
        dropShadowFilter.append('svg:feBlend')
          .attr('in', 'SourceGraphic')
          .attr('in2', 'the-shadow');

    });







}

