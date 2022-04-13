function lineChart() {
    const width = 400;
    const height = 200;
    const margin = {top: 40, right: 40, bottom: 40, left: 40};
    const data = [
      {date: new Date('2018-01-01'), value: 10},
      {date: new Date('2018-01-02'), value: 20},
      {date: new Date('2018-01-03'), value: 30},
      {date: new Date('2018-01-04'), value: 25},
      {date: new Date('2018-01-05'), value: 35},
      {date: new Date('2018-01-06'), value: 45},
      {date: new Date('2018-01-07'), value: 60},
      {date: new Date('2018-01-08'), value: 50}
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
          .attr("font-weight", "bold")
          .attr("font-size", '20px')
          .text('Y축')
        });

    const line = d3.line()
      .defined(d => !isNaN(d.value))
      .x(d => x(d.date))
      .y(d => y(d.value));

    const svg = d3.select('#lineChart').append('svg').style('width', width).style('height', height);
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1)
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("d", line);
    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);
    svg.node();
}
lineChart();