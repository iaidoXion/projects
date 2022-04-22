function wordMapChart() {

    const width = 1050;
    const height = 475;
    const svg = d3.select('#worldMap').append('svg').attr('width', width).attr('height', height);
    const projection = d3.geoMercator().scale(100).translate([width / 2.5, height /1.4]);
    const path = d3.geoPath(projection);
    const g = svg.append('g');

    d3.json('/web/static/data/mapchart.json').then(data => {
        const countries = topojson.feature(data, data.objects.countries);
        g.selectAll('path').data(countries.features).enter().append('path').attr('class', 'country').attr('d', path);
    });
}
wordMapChart();