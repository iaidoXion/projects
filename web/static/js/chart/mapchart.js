function wordMapChart() {

    const width = 1025;
    const height = 590;

    const svg = d3.select('#worldMap').append('svg').attr('width', width).attr('height', height);

    const projection = d3.geoMercator().scale(140).translate([width / 2, height / 1.4]);
    const path = d3.geoPath(projection);

    const g = svg.append('g');

    d3.json('/web/static/data/mapchart.json') .then(data => {
        const countries = topojson.feature(data, data.objects.countries);
        g.selectAll('path').data(countries.features).enter().append('path').attr('class', 'country').attr('d', path);
    });
}
wordMapChart();