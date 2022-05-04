function center(){
    $("#barChart").css({"width" : "100% "});
};

function barChart() {

var jsonData = [
            {name: 'Server', value: 100},
            {name: 'Desktop', value: 290},
            {name: 'Notebook', value: 320},
            {name: 'Monitor', value: 250},
            {name: 'Printer', value: 230},
            {name: 'Mobile', value: 150}
        ];

        var svgWidth = 400;
        var svgHeight = 130;

        var heightPad = 20;
        var widthPad = 22;

        var svg = d3.select("#barChart")
            .append("svg")
            .attr("width", svgWidth + (widthPad * 2))
            .attr("height", svgHeight + (heightPad * 2))
            .append("g")
            .attr("transform", "translate(" + widthPad + "," + heightPad + ")");

        //Set up scales
        var xScale = d3.scale.ordinal()
            .domain(jsonData.map(function(d) { return d.name; }))
            .rangeRoundBands([0, svgWidth], .4);

        var yScale = d3.scale.linear()
            .domain([0, 400])
            .range([svgHeight,-10]);

       // Create bars
        svg.selectAll("rect")
            .data(jsonData)
            .enter().append("rect")
            .attr("x", function (d) { return xScale(d.name) + widthPad; })
            .attr("y", function (d) { return yScale(d.value); })
            .attr("height", function (d) { return svgHeight - yScale(d.value); })
            .attr("width", xScale.rangeBand())
            .attr("fill", "#e08a0b");

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



   /* const width = 465;
    const height = 170;
    const margin = {top: 20, left: 40, bottom: 20, right: 5};

    const data = [
        {name: 'Server', value: 100},
        {name: 'Desktop', value: 290},
        {name: 'Notebook', value: 320},
        {name: 'Monitor', value: 250},
        {name: 'Printer', value: 230},
        {name: 'Mobile', value: 150}
      ];

    const x = d3.scaleBand()
      // .scaleBand() 그래프의 막대의 반복되는 범위를 정해줍니다.
      .domain(data.map(d => d.name))
      // .domain() 각각의 막대에 순서대로 막대에 매핑합니다.
      .range([margin.left, width - margin.right])
      // 시작위치와 끝 위치로 눈금의 범위를 지정합니다.
      .padding(0.5);
      // 막대의 여백을 설정합니다.

    // line chart와 동일
    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.value)]).nice()
        .range([height - margin.bottom, margin.top]);

    // line chart와 동일
    const xAxis = g => g
      .attr('transform', `translate(0, ${height - margin.bottom})`)
      .call(d3.axisBottom(x)
        .tickSizeOuter(0));

    // line chart와 동일
    const yAxis = g => g
      .attr('transform', `translate(${margin.left}, 0)`)
      .call(d3.axisLeft(y))
      .call(g => g.select('.domain').remove());

    // line chart와 동일
    const svg = d3.select('#barChart').append('svg').style('width', width).style('height', height);

    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);
    svg.append('g')
      .attr('fill', '#e08a0b')
      .selectAll('rect').data(data).enter().append('rect')
      // .selectAll() | .select() 메서드는 해당 엘리먼트를 찾지만, 가상의 요소로 선택되기도 합니다.
      // .data() 앞에 선택된 select에 (data)배열에 Join하여 새 선택항목을 반환합니다.
      // DOM에 없는 선택된 엘리먼트에 각 데이터에 대한 자리의 노드를 반환합니다.
      // 여기까지의 코드를 간략하게 풀어보면
      // svg에 g 엘리먼트를 추가하고 그 안의 rect 엘리먼트를 찾습니다.
      // 새로 추가된 g 엘리먼트이기 때문에 그 안의 rect 엘리먼트는 없기 때문에 가상의 엘리먼트로 선택되었습니다.
      // .data(data)로 가상의 엘리먼트에 data 배열 데이터와 Join 되고
      // .enter() Join 된 데이터에 각 자리에 대한 노드를 반환하고
      // .append() 반환된 노드 데이터를 담고 react 엘리먼트를 추가합니다.
      // ex. data = [1, 2, 3, 4] 값을 가지고 있었다면 1, 2, 3, 4 데이터와 매핑된 rect 엘리먼트가 4개 추가됩니다.
      .attr('x', d => x(d.name))
      .attr('y', d => y(d.value))
      .attr('height', d => y(0) - y(d.value))
      .attr('width', x.bandwidth());
      // .bandwidth() 이름 그대로 막대기의 너비값을 응답합니다.
      // 인자값으로 명칭된 d가 svg 엘리먼트 속성 d를 의미하는 줄 알았는데, 그냥 data 값을 의미하는 듯 합니다.

    svg.node();
}

function barChart2() {
    // 차트에 여백 만들기
    const margin = { top: 20, right: 70, bottom: 100, left: 70 };
    const graphWidth = 380 - margin.left - margin.right;
    const graphHeight = 340 - margin.top - margin.bottom;

    const barSvg = d3
      .select("#barChart")
      .append("svg")
      .attr("width", 380)
      .attr("height", 292);


    const graph = barSvg
      .append("g")
      .attr("transform", `translate(${margin.left}, ${margin.top})`);


    const xAxisGroup = graph
      .append("g")
      .attr("transform", `translate(0, ${graphHeight})`); // x축 아래로 translate
    const yAxisGroup = graph.append("g");

    // Data 적용해서 차트 만들기
    d3.json("/web/static/data/barchart.json").then(data => {
      const rects = graph.selectAll("rect").data(data);

      const y = d3
        .scaleLinear() // 한계치 설정
        .domain([0, d3.max(data, d => d.orders)])
        .range([graphHeight, 0]);

      const min = d3.min(data, d => d.orders); // 가장 작은 수 반환
      const max = d3.max(data, d => d.orders); // 가장 큰 수 반환
      const extent = d3.extent(data, d => d.orders); // [min, max] 반환

      const x = d3
        .scaleBand()
        .domain(data.map(item => item.name)) // data 각각의 이름 설정
        .range([0, 300])
        .paddingInner(0.2) // 0.2 padding
        .paddingOuter(0.2);

      rects
        .attr("width", x.bandwidth)
        .attr("height", d => graphHeight - y(d.orders)) // data의 orders 값 적용
        .attr("fill", "orange")
        .attr("x", d => x(d.name)) // data index 값 * 70
        .attr("y", d => y(d.orders));

      // 반환되지 못한 나머지 data 가상 DOM으로 생성
      rects
        .enter()
        .append("rect")
        .attr("width", x.bandwidth)
        .attr("height", d => graphHeight - y(d.orders))
        .attr("fill", "orange")
        .attr("x", d => x(d.name))
        .attr("y", d => y(d.orders)); // 위에 있는 그래프 뒤집기

      // x축 y축 (axis) 생성
      const xAxis = d3.axisBottom(x);
      const yAxis = d3
        .axisLeft(y)
        .ticks(3) //ticks 는 y축 눈금 갯수
        .tickFormat(d => d + " orders"); // 눈금 값 설정

      // 축 적용
      xAxisGroup.call(xAxis);
      yAxisGroup.call(yAxis);

      xAxisGroup
        .selectAll("text") // x축 눈금 값. text 선택
        .attr("transform", "rotate(-40)")
        .attr("text-anchor", "end")
        .attr("fill", "orange");
    });*/
};



barChart();
center();