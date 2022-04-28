function worldMapChart() {

    const width = 1000;
    const height = 618;
    const svg = d3.select('#worldMap')
        .append('svg')
        .attr('width', width)
        .attr('height', height);

    const projection = d3.geoMercator()
        .scale(145)
        .translate([width / 2.5, height /2.5])
        .center([-50,55]);

    const path = d3.geoPath(projection);
    const g = svg.append('g');

    d3.json('/web/static/data/mapchart.json').then(data => {
        const countries = topojson.feature(data, data.objects.countries);
        g.selectAll('path')
            .data(countries.features)
            .enter()
            .append('path')
            .attr('class', 'country')
            .attr('d', path)
            .style("fill", "#858796");
    });
}

worldMapChart();

