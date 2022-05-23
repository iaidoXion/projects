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
  var g = svg.append("g").attr("id", "map"),
  places = svg.append("g").attr("id", "places");

var graticule = d3.geo.graticule()
    .step([5, 5]);

svg.append("path")
    .datum(graticule)
    .attr("class", "graticule")
    .attr("d", path);

/*seno,name,lati,longi
kh99982,세종시정부청사,36.503328,127.261827
kh99983,세종특별자치시청,36.480048,127.289070
kh99984,제주특별자치도청,33.488985,126.498377
kh99985,경상남도청,35.238289,128.692389
kh99986,경상북도청,35.892508,128.600602
kh99987,전라남도청,34.816217,126.462890
kh99988,전라북도청,35.820344,127.108727
kh99989,충청남도청,36.659439,126.673258
kh99990,충청북도청,36.635706,127.491350
kh99991,강원도청,37.885403,127.729784
kh99992,경기도청,37.275001,127.008479
kh99993,울산광역시청,35.539624,129.311522
kh99994,대전광역시청,36.350459,127.384847
kh99995,광주광역시청,35.160068,126.851451
kh99996,인천광역시청,37.455920,126.705501
kh99997,대구광역시청,35.871420,128.601720
kh99998,부산광역시청,35.179756,129.074998
kh99999,서울특별시청,37.566682,126.978418*/

var data = [{x:36.503328,y:127.261827},{x:36.480048,y:127.289070},{x:33.488985,y:126.498377},{x:35.238289,y:128.692389},{x:35.892508,y:128.600602}];

svg.selectAll("circle")
    .data(data)
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
	      data.forEach(function(datum)
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
  d3.json("/web/static/data/mapTopo/world.json", function(error, topology) {
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

function koreaMapChart() {
    var placeid = "";
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
    var mapSvg = d3.select("#koreaMap").append("svg")
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

    var data = [{x:36.503328,y:127.261827},{x:36.480048,y:127.289070},{x:33.488985,y:126.498377},{x:35.238289,y:128.692389},{x:35.892508,y:128.600602}];

    mapSvg.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("class","dot")
        .attr("transform",translateCircle)
        .attr("r",8);


    function translateCircle(datum, index)
              {
                return "translate(" +  koreaProjection([datum.y, datum.x]) + ")";
              };

    setInterval(function(){
              data.forEach(function(datum)
              {
                  mapSvg
                    .append("circle")
                      .attr("class", "ring")
                      .attr("transform", translateCircle(datum))
                      .attr("r", 6)
                      .style("stroke-width", 3)
                      .style("stroke", "red")
                    .transition()
                      .ease("linear")
                      .duration(6000)
                      .style("stroke-opacity", 1e-6)
                      .style("stroke-width", 1)
                      .style("stroke", "brown")
                      .attr("r", 160)
                      .remove();
              })
          }, 750);






/*    zoom = d3.behavior.zoom()
        .center(null) *//* zoom에서 center를 지정하지 않으면 즉, 값을 null로 하면 마우스가 있는 곳에서 확대, 축소 함 *//*
        .size([koreaMapWidth, koreaMapHeight])
        .scaleExtent([1, 10]) *//* [0.5, 5] 확대 및 축소 범위 지정 *//*
        .on("zoom", function()
         { koreaMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
           elecrailMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
           roadMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
           placeMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
         });
    koreaMap.call(zoom).call(zoom.event);
    elecrailMap.call(zoom).call(zoom.event);
    roadMap.call(zoom).call(zoom.event);
    placeMap.call(zoom).call(zoom.event);*/
    // zoom and pan //
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
    { placeMap.selectAll("circle")
              .data(data).enter().append("circle")
              .attr("cx", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("cy", function(d) { return placeProjection([d.longi, d.lati])[1]; })
              .attr("r", 3)
              .attr("class", "placeCircle")
              .attr("id", function(d) { return d.seno; });
      placeMap.selectAll("text")
              .data(data).enter().append("text")
              .attr("x", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("y", function(d) { return placeProjection([d.longi, d.lati])[1] - 5; })
              .attr("class", "placeName")
              .attr("id", function(d) { return d.seno+"name"; })
              .text(function(d) { return d.name; });
    });


/*    $( document )
     .on( "mouseenter", ".placeCircle", function()
      { placeid = $(this).attr('id')+"name";
        $(this).css({"fill" : "#fdca93"});
        $("#"+placeid).css({"display" : "block"});
      })
     .on( "mouseleave", ".placeCircle", function()
      { placeid = $(this).attr('id')+"name";
        $(this).css({"fill" : "#fff"});
        $("#"+placeid).css({"display" : "none"});
      })
     .on( "mouseenter", "#koreaMap #road path", function()
      { $(this).css({"stroke-width" : "6px"});
      })
     .on( "mouseleave", "#koreaMap #road path", function()
      { $(this).css({"stroke-width" : "3px"});
      });*/

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
};

function koreaPopMap(){
var placeid = "";
    var koreaMapWidth = 0;
    var koreaMapHeight = 0;
    var initialScale = 6200,
        initialX = 0,
        initialY = 0,
        centered,
        labels;
    koreaMapWidth  = initialScale / 6;
    koreaMapHeight = initialScale / 6;
    initialX = initialScale * -2.065 - 80;
    initialY = initialScale * 0.75 - 80;
    var mapSvg = d3.select("#koreaPopMap").append("svg")
        .attr("width", koreaMapWidth)
        .attr("height", koreaMapHeight)
        .attr('id', 'koreaPopMap');
    //    .call(zoom);
    var koreaProjection, koreaPath, koreaMap,
        placeProjection, placePath, placeMap,
        roadProjection, roadPath, roadMap,
        elecrailProjection, elecrailPath, elecrailMap;
    var zoom;

    function displayKoreaMap(){
    koreaProjection    = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    placeProjection    = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    roadProjection     = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    elecrailProjection = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    koreaPath    = d3.geo.path().projection(koreaProjection);
    placePath    = d3.geo.path().projection(placeProjection);
    roadPath     = d3.geo.path().projection(roadProjection);
    elecrailPath = d3.geo.path().projection(elecrailProjection);
    koreaMap    = mapSvg.append("g").attr("id", "maps");
    roadMap     = mapSvg.append("g").attr("id", "road");
    elecrailMap = mapSvg.append("g").attr("id", "elecrail");
    placeMap    = mapSvg.append("g").attr("id", "places");
    // zoom and pan //
    zoom = d3.behavior.zoom()
        .center(null) /* zoom에서 center를 지정하지 않으면 즉, 값을 null로 하면 마우스가 있는 곳에서 확대, 축소 함 */
        .size([koreaMapWidth, koreaMapHeight])
        .scaleExtent([1, 10]) /* [0.5, 5] 확대 및 축소 범위 지정 */
        .on("zoom", function()
         { koreaMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
           elecrailMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
           roadMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
           placeMap.attr("transform","translate("+ d3.event.translate + ")scale("+d3.event.scale+")");
         });
    koreaMap.call(zoom).call(zoom.event);
    elecrailMap.call(zoom).call(zoom.event);
    roadMap.call(zoom).call(zoom.event);
    placeMap.call(zoom).call(zoom.event);
    // zoom and pan //
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
    d3.json("/web/static/data/koreaelecrail.geojson", function(json)
    { elecrailMap.selectAll("path")
              .data(json.features).enter().append("path")
              .attr("d", elecrailPath);
    });
    d3.json("/web/static/data/koreaexpresswaylines.geojson", function(json)
    { roadMap.selectAll("path")
              .data(json.features).enter().append("path")
              .attr("d", roadPath);
    });
    d3.csv("/web/static/data/placekorea.csv", function(data)
    { placeMap.selectAll("circle")
              .data(data).enter().append("circle")
              .attr("cx", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("cy", function(d) { return placeProjection([d.longi, d.lati])[1]; })
              .attr("r", 3)
              .attr("class", "placeCircle")
              .attr("id", function(d) { return d.seno; });
      placeMap.selectAll("text")
              .data(data).enter().append("text")
              .attr("x", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("y", function(d) { return placeProjection([d.longi, d.lati])[1] - 5; })
              .attr("class", "placeName")
              .attr("id", function(d) { return d.seno+"name"; })
              .text(function(d) { return d.name; });
    });
    }
    /* ================================================ */


    displayKoreaMap();

    $( document )
     .on( "mouseenter", ".placeCircle", function()
      { placeid = $(this).attr('id')+"name";
        $(this).css({"fill" : "#fdca93"});
        $("#"+placeid).css({"display" : "block"});
      })
     .on( "mouseleave", ".placeCircle", function()
      { placeid = $(this).attr('id')+"name";
        $(this).css({"fill" : "#fff"});
        $("#"+placeid).css({"display" : "none"});
      })
     .on( "mouseenter", "#koreaMap #road path", function()
      { $(this).css({"stroke-width" : "6px"});
      })
     .on( "mouseleave", "#koreaMap #road path", function()
      { $(this).css({"stroke-width" : "3px"});
      });

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
};
koreaPopMap();
worldPopMap();


/*

function worldMapChart(data) {
    var width = 1000, height = 600;
    // projection-settings for mercator
    var projection = d3.geo.mercator()
        .center([0, 52]) // where to center the map in degrees
        .scale(137)// zoomlevel
        .rotate([0,0]);// map-rotation

    // defines "svg" as data type and "make canvas" command
    var svg = d3.select("#worldMap").append("svg").attr("width", width).attr("height", height);

    // defines "path" as return of geographic features
    var path = d3.geo.path().projection(projection);

    // group the svg layers
    var g = svg.append("g").attr("id", "map"), places = svg.append("g").attr("id", "places");
    var graticule = d3.geo.graticule().step([5, 5]);
    svg.append("path").datum(graticule).attr("class", "graticule").attr("d", path);
    svg.selectAll("circle").data(data).enter().append("circle").attr("class","dot").attr("transform",translateCircle).attr("r",4).style("fill", "#e08a0b");
    function translateCircle(datum, index){
        return "translate(" +  projection([datum.y, datum.x]) + ")";
    };
    setInterval(function(){
        data.forEach(function(datum){
            svg.append("circle").attr("class", "ring")
                .attr("transform", translateCircle(datum)).attr("r", 1).style("fill", "#e06f0b").style("opacity", "0.3").style("fill-opacity", "0.3")
			    .transition().ease("linear").duration(2000).style("stroke-opacity", 1e-6).style("stroke-width", 1).style("stroke", "e06f0b")
			    .attr("r", 30).remove();
        })
    }, 800);

    // load data and display the map on the canvas with country geometries
    d3.json("/web/static/data/mapTopo/world.json", function(error, topology) {
        g.selectAll("path").data(topojson0.object(topology, topology.objects.countries).geometries).enter()
            .append("path").attr("d", path).style("fill", "#d5d6dd");
    });
}


function koreaMapChart(data) {

    var placeid = "";
    var koreaMapWidth = 0;
    var koreaMapHeight = 0;
    var initialScale = 4900, initialX = 0, initialY = 0, centered, labels;
    koreaMapWidth  = initialScale / 6;
    koreaMapHeight = initialScale / 6;
    initialX = initialScale * -2.12 - 80;
    initialY = initialScale * 0.75 - 80;
    var mapSvg = d3.select("#koreaMap").append("svg")
        .attr("width", koreaMapWidth)
        .attr("height", koreaMapHeight)
        .attr('id', 'koreaMap');
    //    .call(zoom);
    var koreaProjection, koreaPath, koreaMap, placeProjection, placePath, placeMap;

    koreaProjection = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    placeProjection = d3.geo.mercator().scale(initialScale).translate([initialX, initialY]);
    koreaPath = d3.geo.path().projection(koreaProjection);
    placePath = d3.geo.path().projection(placeProjection);
    koreaMap = mapSvg.append("g").attr("id", "maps");
    placeMap = mapSvg.append("g").attr("id", "places");
    // zoom and pan //
    var koreaProjection = d3.geo.mercator().center([113, -3]).scale(1275).translate([koreaMapWidth / 2, koreaMapHeight / 2]).clipExtent([[0, 0], [koreaMapWidth, koreaMapHeight]]).precision(.1);
    var path = d3.geo.path().projection(koreaProjection);
    var graticule = d3.geo.graticule().step([5, 5]);
    mapSvg.append("path").datum(graticule).attr("class", "graticule").attr("d", path);
    mapSvg.selectAll("circle").data(data).enter().append("circle").attr("class","dot").attr("transform",translateCircle).attr("r",8);

    function translateCircle(datum, index){
        return "translate(" +  koreaProjection([datum.y, datum.x]) + ")";
    };

    setInterval(function(){
        data.forEach(function(datum){
            mapSvg.append("circle").attr("class", "ring").attr("transform", translateCircle(datum))
            .attr("r", 6).style("stroke-width", 3).style("stroke", "red").transition().ease("linear")
            .duration(6000).style("stroke-opacity", 1e-6).style("stroke-width", 1).style("stroke", "brown")
            .attr("r", 160).remove();
        })
    }, 750);


    d3.json("/web/static/data/mapTopo/korea.json", function(json){
        koreaMap.selectAll("path")
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
    d3.csv("/web/static/data/placekorea.csv", function(data){
        placeMap.selectAll("circle")
        .data(data).enter().append("circle")
              .attr("cx", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("cy", function(d) { return placeProjection([d.longi, d.lati])[1]; })
              .attr("r", 3)
              .attr("class", "placeCircle")
              .attr("id", function(d) { return d.seno; });
      placeMap.selectAll("text")
              .data(data).enter().append("text")
              .attr("x", function(d) { return placeProjection([d.longi, d.lati])[0]; })
              .attr("y", function(d) { return placeProjection([d.longi, d.lati])[1] - 5; })
              .attr("class", "placeName")
              .attr("id", function(d) { return d.seno+"name"; })
              .text(function(d) { return d.name; });
    });

    function labelsTransform(d) {
    // 경기도가 서울특별시와 겹쳐서 위치 조정 및 세종특별자치시와 대전광역시 위치 조정
     if (d.properties.code == 31) */
/* 경기도 *//*

     { var arr = koreaPath.centroid(d);
       arr[1] += (d3.event && d3.event.scale) ? (d3.event.scale / koreaMapHeight - 40) : (initialScale / koreaMapHeight - 40);
       return "translate(" + arr + ")";
     }
     else if (d.properties.code == 25) */
/* 대전광역시 *//*

     { var arr = koreaPath.centroid(d);
       arr[1] += (d3.event && d3.event.scale) ? (d3.event.scale / koreaMapHeight + 5) : (initialScale / koreaMapHeight + 5);
       return "translate(" + arr + ")";
     }
     else if (d.properties.code == 29) */
/* 세종특별자치시 *//*

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
};


function seoulMap(){
    var width = 800, height = 600;
    var svg = d3.select("#siMap").append("svg").attr("width", width).attr("height", height);
    var map = svg.append("g").attr("id", "map"),places = svg.append("g").attr("id", "places");
    var projection = d3.geo.mercator().center([126.9895, 37.5651]).scale(100000).translate([width/2, height/2]);
    var path = d3.geo.path().projection(projection);

    d3.json("/web/static/data/mapTopo/seoul.json", function(error, data) {
        var features = topojson.feature(data, data.objects.seoul_municipalities_geo).features;

        map.selectAll('path').data(features).enter().append('path')
        .attr('class', function(d) { console.log(); return 'municipality c' + d.properties.code })
        .attr('d', path);

        map.selectAll('text').data(features).enter().append("text")
        .attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
        .attr("dy", ".35em")
        .attr("class", "municipality-label")
        .text(function(d) { return d.properties.name; })
    });

    d3.csv("/web/static/data/placeSi.csv", function(data) {
        places.selectAll("circle").data(data).enter().append("circle")
        .attr("cx", function(d) { return projection([d.lon, d.lat])[0]; })
        .attr("cy", function(d) { return projection([d.lon, d.lat])[1]; })
        .attr("r", 10);

        places.selectAll("text").data(data).enter().append("text")
        .attr("x", function(d) { return projection([d.lon, d.lat])[0]; })
        .attr("y", function(d) { return projection([d.lon, d.lat])[1] + 8; })
        .text(function(d) { return d.name });
    });
}*/
