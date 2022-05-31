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

var data = [{x:37.5569016,y:126.9329799},{x:37.5344248,y:126.9750082},{x:37.5189582,y:126.9307458},{x:37.5720260,y:126.9743351},{x:37.5617693,y:126.9921966}];

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




var data = [{x:37.5569016,y:126.9329799},{x:37.5344248,y:126.9750082},{x:37.5189582,y:126.9307458},{x:37.5720260,y:126.9743351},{x:37.5617693,y:126.9921966}];

mapSvg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("class","dot")
    .attr("transform",translateCircle)
    .attr("r",4)
    .style("fill", "#e08a0b");

function translateCircle(datum, index)
          {
            return "translate(" +  placeProjection([datum.y, datum.x]) + ")";
          };

setInterval(function(){
	      data.forEach(function(datum)
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

};


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


*/
function seoulMap(){
    var width = 1000, height = 600;
    var svg = d3.select("#siMap").append("svg").attr("width", width).attr("height", height).style("margin-left", '1%');
    var map = svg.append("g").attr("id", "map"),places = svg.append("g").attr("id", "places");
    var projection = d3.geo.mercator().center([126.9895, 37.5451]).scale(90000).translate([width/2, height/2]);
    var path = d3.geo.path().projection(projection);

var data = [{x:37.5569016,y:126.9329799},{x:37.5344248,y:126.9750082},{x:37.5189582,y:126.9307458},{x:37.5720260,y:126.9743351},{x:37.5617693,y:126.9921966}];

svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("class","dot")
    .attr("transform",translateCircle)
    .attr("r",8)
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

/*    d3.csv("/web/static/data/placeSi.csv", function(data) {
        places.selectAll("circle").data(data).enter().append("circle")
        .attr("cx", function(d) { return projection([d.lon, d.lat])[0]; })
        .attr("cy", function(d) { return projection([d.lon, d.lat])[1]; })
        .attr("r", 10);

        places.selectAll("text").data(data).enter().append("text")
        .attr("x", function(d) { return projection([d.lon, d.lat])[0]; })
        .attr("y", function(d) { return projection([d.lon, d.lat])[1] + 8; })
        .text(function(d) { return d.name });
    });*/


        /*var buildCircle = {
					init: function(){
                        var w = 1500;
                        var h = 800;
                        // make a dummy data set
                        var dataset = [],
                        i = 0;
                        for(i=0; i<7; i++){
                            var locale = {
                                "xcoord": getRandomInt (w/8, w/2),
                                "ycoord": getRandomInt (h/8, h/2),
                                "value": 30,//getRandomInt (10, 100),
                                "alarmLevel": getRandomInt (0, 200)
                            }
                            dataset.push(locale);
                        }
                        //__ make dummy data

                        function getRandomInt (min, max) {
                            return Math.floor(Math.random() * (max - min + 1)) + min;
                        }

                        //__viz append
                        svg.append("svg")
                            .attr("width", w)
                            .attr("height", h)
                                .append("g")
                                .attr("transform", "translate(140, 160)")

                        //_place holder for markers
                        var circleGroup = svg.append("g")
                            .attr("class", "circles");
                            circleGroup.selectAll("circle")
                            .data(dataset)
                            .enter().append("circle")
                            .style("stroke", "#e08a0b")
                            .style("fill", "#e08a0b")
                            .attr("r", function(d){
                                return d.value*.1;//scale the circles
                            })
                            .attr("cx", function(d){
                                return d.xcoord;
                            })
                            .attr("cy", function(d){
                                return d.ycoord;
                            });
                         //_place holder for rings
                         var speedLineGroup = svg.append("g")
                             .attr("class", "speedlines");
                        function getDurationPerDot(circleData){
                            var totalTime = 3000;//3 seconds max
                            var time = totalTime-(circleData.alarmLevel*10)
                            return time;
                        }

                        function getOuterRadiusPerDot(circleData){
                            var radius = circleData.alarmLevel*.5;
                            return radius;
                        }


                        $.each(dataset, function( index, value ) {
                            $('.throbdata').append("<li>dot:"+index+" , alarm val :"+value.alarmLevel+" , orb size :"+value.value+", Duration: "+getDurationPerDot(value)+"</li>");
                        });

                        //invoke rings
                        makeRings()
                        //window.setInterval(makeRings, 1000);
                        function makeRings() {
                            var datapoints = circleGroup.selectAll("circle");
                            var radius = 1;
                                function myTransition(circleData){
                                    var transition = d3.select(this).transition();
                                        var duration = getDurationPerDot(circleData);
                                        var outerRadius = getOuterRadiusPerDot(circleData);
                                        speedLineGroup.append("circle")
                                            .attr({
                                                "class": "ring",
                                                "fill":"#df7454",
                                                "stroke":"#f4c17c",
                                                "stroke-width": 1.5,
                                                "cx": circleData.xcoord,
                                                "cy": circleData.ycoord,
                                                "r":radius,
                                                "opacity": 0.7,
                                                "fill-opacity":0.7
                                            })
                                            .transition()
                                            .duration(6000)
                                            .attr("r", radius + outerRadius )
                                            .attr("opacity", 0)
                                            .remove();
                                    var t= setInterval(function(){
                                        clearInterval(t);
                                        myTransition(circleData)
                                    },700);
                                    //transition.each('end', myTransition);
                                }
                          datapoints.each(myTransition);
                        }
				}
			}
			$(document).ready(function() {
			buildCircle.init();
            });
*/
}

function bundangMap(){


/*
var mapContainer = document.getElementById('guMap'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.39806012268096, 127.1094211519), // 지도의 중심좌표
        level: 4 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 마커를 표시할 위치와 title 객체 배열입니다
var ncrd = [
    {
        title: '엔씨소프트 R&D센터',
        latlng: new kakao.maps.LatLng(37.39948593886602, 127.10864108531601)
    }
];

var ncalpha = [
    {
        title: '알파돔시티 판교알파리움1단지아파트',
        latlng: new kakao.maps.LatLng(37.39557358509345, 127.1082797008697)
    }
];

var users = [
    {
        title: '판교테크노파크공원',
        latlng: new kakao.maps.LatLng(37.39863925472823, 127.10834057983851)
    },
    {
        title: '봇들저류지 공원',
        latlng: new kakao.maps.LatLng(37.3994744444141, 127.11131206038527)
    },
    {
        title: '코트야드 바이 메리어트 서울 판교',
        latlng: new kakao.maps.LatLng(37.397501793831225, 127.11068799834034)
    }
];



// 마커 이미지의 이미지 주소입니다
var ncrdImage = "/web/static/img/dashboard/ncrd.png";
var ncalphaImage = "/web/static/img/dashboard/ncalpha.png";
var usersImage = "/web/static/img/dashboard/userorange.png";

for (var i = 0; i < ncrd.length; i ++) {

    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(40, 40)
        imageOption = {offset: new kakao.maps.Point(20, 50)};

    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(ncrdImage, imageSize, imageOption);

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: ncrd[i].latlng, // 마커를 표시할 위치
        title : ncrd[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지
    });}

for (var i = 0; i < ncalpha.length; i ++) {

    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(40, 40)
        imageOption = {offset: new kakao.maps.Point(20, 50)};

    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(ncalphaImage, imageSize, imageOption);

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: ncalpha[i].latlng, // 마커를 표시할 위치
        title : ncalpha[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지
    });}

for (var i = 0; i < users.length; i ++) {

    // 마커 이미지의 이미지 크기 입니다
    var imageSize = new kakao.maps.Size(20, 20)
        imageOption = {offset: new kakao.maps.Point(0, 20)};

    // 마커 이미지를 생성합니다
    var markerImage = new kakao.maps.MarkerImage(usersImage, imageSize, imageOption);

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: users[i].latlng, // 마커를 표시할 위치
        title : users[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
        image : markerImage // 마커 이미지
    });}




*/


}


function pangyoMap(){









/*// get the data
d3.csv("/web/static/data/force.csv", function(error, links) {

var nodes = {};

// Compute the distinct nodes from the links.
links.forEach(function(link) {
    link.source = nodes[link.source] ||
        (nodes[link.source] = {name: link.source});
    link.target = nodes[link.target] ||
        (nodes[link.target] = {name: link.target});
    link.value = +link.value;
});

var width = 800,
    height = 600;

var force = d3.layout.force()
    .nodes(d3.values(nodes))
    .links(links)
    .size([width, height])
    .linkDistance(60)
    .charge(-900)
    .on("tick", tick)
    .start();

var svg = d3.select("#dongMap").append("svg")
    .attr("width", width)
    .attr("height", height);*/

/*// build the arrow.
svg.append("svg:defs").selectAll("marker")
    .data(["end"])
  .enter().append("svg:marker")
    .attr("id", String)
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
  .append("svg:path")
    .attr("d", "M0,-5L10,0L0,5");*/



// define the nodes
/*var node = svg.selectAll(".node")
    .data(force.nodes())
  .enter().append("g")
    .attr("class", "node")
    .call(force.drag);

// add the nodes
node.append("image")
    .attr("xlink:href", "/web/static/img/dashboard/userorange.png")
    .attr("width", 60)
    .attr("height", 55);

// add the links and the arrows
var path = svg.append("svg:g").selectAll("path")
    .data(force.links())
  .enter().append("svg:path")
    .attr("class", "link")
    .attr("marker-end", "url(#end)");

// add the text
node.append("text")
    .attr("x", 12)
    .attr("dy", ".35em")
    .text(function(d) { return d.name; });

// add the curvy lines
function tick() {
    path.attr("d", function(d) {
        var dx = d.target.x - d.source.x,
            dy = d.target.y - d.source.y,
            dr = Math.sqrt(dx * dx + dy * dy);
        return "M" +
            d.source.x + "," +
            d.source.y + "A" +
            dr + "," + dr + " 0 0,1 " +
            d.target.x + "," +
            d.target.y;
    });

    node
        .attr("transform", function(d) {
            return "translate(" + d.x + "," + d.y + ")"; });
}

});*/
}