/*d3.csv("/web/static/data/ttt.csv", lineChart);
function lineChart(data) {
console.log(data)
data.
// 여백을 넣어 스케일을 만든다.
    xScale = d3.scaleLinear().domain([1,10.5]).range([20,480]);
    yScale = d3.scaleLinear().domain([0,35]).range([480,20]);

// 날짜를 표현하도록 X-축의 눈금을 설정한다.
    xAxis = d3.axisBottom()
                .scale(xScale)
                .tickSize(480)
                .tickValues([1,2,3,4,5,6,7,8,9,10]);

    d3.select("svg").append("g").attr("id", "xAxisG").call(xAxis);

    yAxis = d3.axisBottom()
                .scale(yScale)
                .ticks(10)
                .tickSize(480);

    d3.select("svg").append("g").attr("id", "yAxisG").call(yAxis);

// 다음에 나오는 세 줄의 코드는 같은 데이터셋을 사용하지만, y위치가 각기 트윗, 리트윗, 관심글 담기 횟수를 나타낸다.
    d3.select("svg").selectAll("circle.tweets")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "tweets")
        .attr("r", 5)
        .attr("cx", function(d) {return xScale(d.day)})
        .attr("cy", function(d) {return yScale(d.tweets)})
        .style("fill", "black");

    d3.select("svg").selectAll("circle.retweets")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "retweets")
        .attr("r", 5)
        .attr("cx", function(d) {return xScale(d.day)})
        .attr("cy", function(d) {return yScale(d.retweets)})
        .style("fill", "lightgray");

    d3.select("svg").selectAll("circle.favorites")
        .data(data)
        .enter()
        .append("circle")
        .attr("class", "favorites")
        .attr("r", 5)
        .attr("cx", function(d) {return xScale(d.day)})
        .attr("cy", function(d) {return yScale(d.favorites)})
        .style("fill", "gray");

// 선 생성기 하나만 정의하고, 각각의 선을 그릴 때 y() 접근자 메서드만 변경하면 더 효율적으로 구현할 수 있지만,
// 이와 같이 따로 정의하면 각 선을 그리는 코드를 알아보기 쉽다.
    var tweetLine = d3.line()
        .x(function(d){
            return xScale(d.day)
        })
        .y(function(d){
            return yScale(d.tweets)
        });

// 세 개의 행에서 y() 접근자만 다른 것을 알 수 있다.
    var retweetLine = d3.line()
        .x(function(d){
            return xScale(d.day)
        })
        .y(function(d){
            return yScale(d.retweets)
        });

    var favLine = d3.line()
        .x(function(d){
            return xScale(d.day);
        })
        .y(function(d){
            return yScale(d.favorites);
        });

// 새로운 <path> 요소는 각기 자신에 대응되는 생성기를 호출한다.
    d3.select("svg")
        .append("path")
        .attr("d", tweetLine(data))
        .attr("fill", "none")
        .attr("stroke", "darkred")
        .attr("stroke-width", 2);

    d3.select("svg")
        .append("path")
        .attr("d", retweetLine(data))
        .attr("fill", "none")
        .attr("stroke", "gray")
        .attr("stroke-width", 3);

    d3.select("svg")
        .append("path")
        .attr("d", favLine(data))
        .attr("fill", "none")
        .attr("stroke", "black")
        .attr("stroke-width", 2);



}
lineChart();*/


function lineChart() {
    const width = 465;
    const height = 170;
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
      .attr("stroke", "#e08a0b")
      .attr("stroke-width", 2)
      .attr("stroke-linejoin", "round")
      .attr("stroke-linecap", "round")
      .attr("d", line);
    svg.append('g').call(xAxis);
    svg.append('g').call(yAxis);
    svg.node();
}
lineChart();