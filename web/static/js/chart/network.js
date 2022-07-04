function networkChart(networkData){

var width = 960, height = 600;

var svg = d3v4.select("#guMap").append("svg").attr("width", width).attr("height", height);

var imgs = svg.append("svg:image").attr("xlink:href", "/web/static/img/dashboard/zone-background.png").attr("x", 0).attr("y", 0).attr("width", "960").attr("height", "600");

var simulation = d3v4.forceSimulation()
    .force("link", d3v4.forceLink().distance(150).id(function(d) { return d.id; }))
    .force("charge", d3v4.forceManyBody().strength(-73))
    .force("center", d3v4.forceCenter(width / 2, height / 2));

networkData.forEach(function(graph) {

  var link = svg.append("g").attr("class", "links").selectAll("line").data(graph.links).enter().append("line").attr("stroke-width", "1.7").style("stroke", "#e18a0a");

  var node = svg.append("g").attr("class", "nodes").selectAll("g").data(graph.nodes).enter().append("g")
            .on("mouseover", function(d) { d3.select(this).style("cursor", "pointer")})

  var ipGroup = function(g){
    if(g == "192.168.0"){
        return "group0";
    }else if(g == "192.168.1"){
        return "group1";}
  };


  var fillCircle = function(g){
        if(g == "false"){
            return "/web/static/img/dashboard/hexagon-border.png";
        }else if(g == "true"){
            return "/web/static/img/dashboard/hexagon.png";}
  };

  var fillCenter = function(g){
        if(g == "groupCenter1"){
            return "/web/static/img/dashboard/ncrd.png";
        }else if(g == "groupCenter2"){
            return "/web/static/img/dashboard/ncalpha.png";}
  };

  var CircleSize = function(g){
        if(g.startsWith('groupCenter') == true){
            return "80";
        }else{
            return "60";
        }
    };

  var textColor = function(g){
        if(g == "true"){
            return "#ffffff";
        }else{
            return "#e18a0a";
        }
    };

  var circles = node.append("image")
    .attr('width',function(d) { return CircleSize(d.id); })
    .attr('height',function(d) { return CircleSize(d.id); })
    .attr('x', -31)
    .attr('y', -55)
    .attr("xlink:href", function(d) { return fillCenter(d.id); })
    .style("filter", "url(#drop-shadow)");

  var centerCircles = node.append("image")
    .attr('width',function(d) { return CircleSize(d.id); })
    .attr('height',function(d) { return CircleSize(d.id); })
    .attr('x', -31)
    .attr('y', -55)
    .attr("xlink:href", function(d) { return fillCircle(d.point); })
    .style("filter", "url(#drop-shadow)");

// Create a drag handler and append it to the node object instead
/*  var drag_handler = d3v4.drag()
      .on("start", dragstarted)
      .on("drag", dragged)
      .on("end", dragended);

  drag_handler(node);*/

  var labels = node.append("text")
        .text(function(d) { return d.name;})
        .style("fill", function(d) { return textColor(d.point); })
        .attr("text-anchor", "middle").attr('x', 0).attr('y', -18);

  node.append("title")
        .text(function(d) {
            returnData = "Case : " + d.alarmCase + "\nCount :" + d.alarmCount
            return returnData;
         });

  simulation.nodes(graph.nodes).on("tick", ticked);

  simulation.force("link").links(graph.links);

  function ticked() {
    link.attr("x1", function(d) { return d.source.x; }).attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; }).attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) {return "translate(" + d.x + "," + d.y + ")";})
  }
});

/*
function dragstarted(d) {
  if (!d3v4.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3v4.event.x;
  d.fy = d3v4.event.y;
}

function dragended(d) {
  if (!d3v4.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
*/

var dropShadowFilter = svg.append('svg:filter')
  .attr('id', 'drop-shadow')
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

}
