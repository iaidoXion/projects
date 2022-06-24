function center(){
    $("#barChart").css({"width" : "100% "});
};

function barChart(barChartData) {


        var hoverColor = '#eec42d';
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
                 .style("cursor", "pointer");
                 /*tooltip
                    .html(
                      `<div>${d.value}</div>`
                    )
                    .style("margin-top", (d3.select(this).attr("y")-heightPad + "px"))
                    .style("margin-left", (d3.select(this).attr("x")-marginTip + "px"))
                    .style('visibility', 'visible');*/
            });
            /*
            .on("mouseout", function(d) {
                tooltip.style('visibility', 'hidden');
            });*/

          rect.append("title")
              .text(function(d) {
                return d.value;
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
            .text("")

};

