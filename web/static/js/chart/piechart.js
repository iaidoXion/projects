function piechart(pieChartData) {
    const width = 200;
    const height = 170;
    const color = ["#e08a0b","#f5a631","#f8c477","#f2cd96"];
    //'#efa86b', '#c1484f', '#d35d50', '#f4c17c', '#fae8a4', '#df7454', '#e88d5d', '#f8d690'
    const arc = d3.svg.arc() // .arc() 새로운 기본값의 아치(호) 생성
        .innerRadius(30) // .innerRadius() 안쪽 반지름 값, 0이면 완전한 원이되고 값이 있으면 도넛 형태가 됩니다.
        .outerRadius(Math.min(width, height) / 2.3); // .outerRadius() 바깥쪽 반지름값
    // 라벨이 위치할 반지름 값을 설정합니다.
    const arcLabel = (() => {
      const radius = Math.min(width, height) / 3.3;
      return d3.svg.arc().innerRadius(radius).outerRadius(radius);
    })();

    const pie = d3.layout.pie()  // 새로운 기본값의 파이 모양의 생성
        .sort((a, b) => b.value - a.value) // data의 value 큰값 > 작은값 순으로 정렬 ex. 반대 순서는 a.value - b.value
        .value(d => d.value);

    const arcs = pie(pieChartData);
    const svg = d3.select('#pieChart')
        .append('svg')
        .style('width', width)
        .style('height', height)
        .style("margin-left", '29%')
        .attr('text-anchor', 'middle') // text-anchor 텍스트의 정렬을 설정 ( start | middle | end | inherit )
        .style('font-size', '13px');

    const g = svg.append('g')
      .attr('transform', `translate(${width/2}, ${height/2})`);
      // 우선 차트를 그릴 그룹 엘리먼트를 추가합니다.
      // 위치값을 각각 2로 나누는건 반지름 값을 기준으로 한바퀴 돌며 path를 그리기 때문인거 같습니다.

    g.selectAll('path')
      .data(arcs)
      .enter().append('path')
      // 이전과 동일하게 가상 path 요소를 만들고 그래프 데이터와 매핑하여 엘리먼트를 추가합니다.
      .attr('fill', function(d,i) { return color[i]; })
      // 다른 그래프와 다르게 .data 라는 객체가 추가되어 있는데, 위에 arcs 변수를 선언할때
      // .pie(data)가 {data, value, index, startAngle, endAngle, padAngle} 의 값을 가지고 있습니다.
      .attr('stroke', 'white')
      .attr('d', arc)
      .append('title')
      .text(d => `${d.data.value}`);
      // 각각 페스의 자식으로 title의 엘리먼트에 텍스트로 출력합니다.
      // 실제로 뷰에 출력되지는 않지만 시멘틱하게 각각의 요소의 설명 문자열을 제공합니다.



    const text = g.selectAll('text')
      .data(arcs)
      .enter().append('text')
      .attr('transform', d => `translate(${arcLabel.centroid(d)})`)
      .attr('dy', '0.35em');
      // 라벨을 취가하기 위한 text 엘리먼트를 만들고 위치를 지정합니다.

    text.append('tspan')
      .attr('x', '-0.1em')
      .attr('y', '-0.2em')
      .text(d => d.data.name);


/*    text.filter(d => (d.endAngle - d.startAngle > 0.25)).append('tspan')
      .attr('x', 0)
      .attr('y', '0.7em')
      .attr('fill-opacity', 0.7)
      .text(d => d.data.value);*/
      // 해당 데이터의 수치값을 투명도를 주어 출력합니다. ex. 1000

    svg.selectAll("path")
      .on("mouseover", function(d, i){
        d3.select(this)
            .style("cursor", "pointer")
            .attr('d',function(d){return d3.svg.arc().innerRadius(35)
            .outerRadius((Math.min(width, height) / 2))(d)});

      })
      .on("mouseout", function(d) {
        d3.select(this)
            .attr('d',function(d){return d3.svg.arc().innerRadius(30).outerRadius((Math.min(width, height) / 2.3))(d)});
      });


    svg.node();
}

