function lineChart() {
    const width = 400;
    const height = 200;
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
      .attr("stroke", "#efa86b")
      .attr("stroke-width", 2)
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("d", line);
    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);
    svg.node();
}
lineChart();