function koreaMapChart() {
    var width = 960,
        height = 600;

    var svg = d3.select("#koreaMap").append("svg")
        .attr("width", width)
        .attr("height", height);

    var projection = d3.geo.mercator()
        .center([127, 37.55])
        .scale(90000)
        .translate([width/2, height/2]);

    var path = d3.geo.path()
        .projection(projection);

    var quantize = d3.scale.quantize()
        .domain([0, 1000])
        .range(d3.range(9).map(function(i) { return "p" + i; }));

    var popByName = d3.map();

    queue()
        .defer(d3.json, "/web/static/data/municipalities-topo-simple.json")
        .defer(d3.csv, "/web/static/data/koreaMapData.csv", function(d) {
            popByName.set(d.name, +d.population);
        })
        .await(ready);

    function ready(error, data) {
      var features = topojson.feature(data, data.objects["municipalities-geo"]).features;

      features.forEach(function(d) {
        d.properties.population = popByName.get(d.properties.name);
        d.properties.density = d.properties.population / path.area(d);
        d.properties.quantized = quantize(d.properties.density);
      });

      svg.selectAll("path")
          .data(features)
        .enter().append("path")
          .attr("class", function(d) { return "municipality " + d.properties.quantized; })
          .attr("d", path)
          .attr("id", function(d) { return d.properties.name; })
          .append("title")
          .text(function(d) { return d.properties.name + ": " + d.properties.population/10000 + "만 명" });


      svg.selectAll("text")
          .data(features.filter(function(d) { return d.properties.name.endsWith("시"); }))
        .enter().append("text")
          .attr("transform", function(d) { return "translate(" + path.centroid(d) + ")"; })
          .attr("dy", ".35em")
          .attr("class", "region-label")
          .text(function(d) { return d.properties.name; });
    }
}

koreaMapChart();