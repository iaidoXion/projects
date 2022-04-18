function gaugeChart(){
    function gaugeChartDefaultSettings() {
        return {
            minValue: 0, // The gauge minimum value.
            maxValue: 100, // The gauge maximum value.
            circleThickness: 0.05, // The outer circle thickness as a percentage of it's radius.
            circleFillGap: 0.05, // The size of the gap between the outer circle and wave circle as a percentage of the outer circles radius.
            circleColor: "#178BCA", //178BCA The color of the outer circle.
            waveHeight: 0.05, // The wave height as a percentage of the radius of the wave circle.
            waveCount: 1, // The number of full waves per width of the wave circle.
            waveRiseTime: 1000, // The amount of time in milliseconds for the wave to rise from 0 to it's final height.
            waveAnimateTime: 18000, // The amount of time in milliseconds for a full wave to enter the wave circle.
            waveRise: true, // Control if the wave should rise from 0 to it's full height, or start at it's full height.
            waveHeightScaling: true, // Controls wave size scaling at low and high fill percentages. When true, wave height reaches it's maximum at 50% fill, and minimum at 0% and 100% fill. This helps to prevent the wave from making the wave circle from appear totally full or empty when near it's minimum or maximum fill.
            waveAnimate: true, // Controls if the wave scrolls or is static.
            waveColor: "#178BCA", // 178BCAThe color of the fill wave.
            waveOffset: 0, // The amount to initially offset the wave. 0 = no offset. 1 = offset of one full wave.
            textVertPosition: .5, // The height at which to display the percentage text withing the wave circle. 0 = bottom, 1 = top.
            textSize: 1, // The relative height of the text to display in the wave circle. 1 = 50%
            valueCountUp: true, // If true, the displayed value counts up from 0 to it's final value upon loading. If false, the final value is displayed.
            displayPercent: true, // If true, a % symbol is displayed after the value.
            textColor: "#045681", //045681 The color of the value text when the wave does not overlap it.
            waveTextColor: "#A4DBf8" //A4DBf8 The color of the value text when the wave overlaps it.
        };
    }

    function gaugeChartLoad(elementId, value, config) {
        if (config == null) config = gaugeChartDefaultSettings();
        const gauge = d3.select("#" + elementId);
        const radius = Math.min(parseInt(gauge.style("width")), parseInt(gauge.style("height"))) / 2;
        const locationX = parseInt(gauge.style("width")) / 2 - radius;
        const locationY = parseInt(gauge.style("height")) / 2 - radius;
        const fillPercent = Math.max(config.minValue, Math.min(config.maxValue, value)) / config.maxValue;
        let waveHeightScale = null;
        if (config.waveHeightScaling) {
            waveHeightScale = d3.scaleLinear()
                .range([0, config.waveHeight, 0])
                .domain([0, 50, 100]);
        } else {
            waveHeightScale = d3.scaleLinear()
                .range([config.waveHeight, config.waveHeight])
                .domain([0, 100]);
        }

        const textPixels = (config.textSize * radius / 2);
        const textFinalValue = parseFloat(value).toFixed(2);
        const textStartValue = config.valueCountUp ? config.minValue : textFinalValue;
        const percentText = config.displayPercent ? "%" : "";
        const circleThickness = config.circleThickness * radius;
        const circleFillGap = config.circleFillGap * radius;
        const fillCircleMargin = circleThickness + circleFillGap;
        const fillCircleRadius = radius - fillCircleMargin;
        const waveHeight = fillCircleRadius * waveHeightScale(fillPercent * 100);

        const waveLength = fillCircleRadius * 2 / config.waveCount;
        const waveClipCount = 1 + config.waveCount;
        const waveClipWidth = waveLength * waveClipCount;

        let textRounder = function (value) { return Math.round(value); };
        if (parseFloat(textFinalValue) != parseFloat(textRounder(textFinalValue))) {
            textRounder = function (value) { return parseFloat(value).toFixed(1); };
        }
        if (parseFloat(textFinalValue) != parseFloat(textRounder(textFinalValue))) {
            textRounder = function (value) { return parseFloat(value).toFixed(2); };
        }

        // Data for building the clip wave area.
        const data = [];
        for (let i = 0; i <= 40 * waveClipCount; i++) {
            data.push({ x: i / (40 * waveClipCount), y: (i / (40)) });
        }

        // Scales for drawing the outer circle.
        const gaugeCircleX = d3.scaleLinear().range([0, 2 * Math.PI]).domain([0, 1]);
        const gaugeCircleY = d3.scaleLinear().range([0, radius]).domain([0, radius]);

        // Scales for controlling the size of the clipping path.
        const waveScaleX = d3.scaleLinear().range([0, waveClipWidth]).domain([0, 1]);
        const waveScaleY = d3.scaleLinear().range([0, waveHeight]).domain([0, 1]);

        // Scales for controlling the position of the clipping path.
        const waveRiseScale = d3.scaleLinear()
           .range([(fillCircleMargin + fillCircleRadius * 2 + waveHeight), (fillCircleMargin - waveHeight)])
           .domain([0, 1]);
        const waveAnimateScale = d3.scaleLinear()
            .range([0, waveClipWidth - fillCircleRadius * 2]) // Push the clip area one full wave then snap back.
            .domain([0, 1]);

        // Scale for controlling the position of the text within the gauge.
        const textRiseScaleY = d3.scaleLinear()
           .range([fillCircleMargin + fillCircleRadius * 2, (fillCircleMargin + textPixels * 0.7)])
           .domain([0, 1]);

        // Center the gauge within the parent SVG.
        const gaugeGroup = gauge.append("g")
            .attr('transform', 'translate(' + locationX + ',' + locationY + ')');

        // Draw the outer circle.
        const gaugeCircleArc = d3.arc()
            .startAngle(gaugeCircleX(0))
            .endAngle(gaugeCircleX(1))
            .outerRadius(gaugeCircleY(radius))
            .innerRadius(gaugeCircleY(radius - circleThickness));
        gaugeGroup.append("path")
            .attr("d", gaugeCircleArc)
            .style("fill", config.circleColor)
            .attr('transform', 'translate(' + radius + ',' + radius + ')');

        // Text where the wave does not overlap.
        const text1 = gaugeGroup.append("text")
           .text(textRounder(textStartValue) + percentText)
           .attr("class", "liquidFillGaugeText")
           .attr("text-anchor", "middle")
           .attr("font-size", textPixels + "px")
           .style("fill", config.textColor)
           .attr('transform', 'translate(' + radius + ',' + textRiseScaleY(config.textVertPosition) + ')');
        let text1InterpolatorValue = textStartValue;

        // The clipping wave area.
        const clipArea = d3.area()
            .x(function (d) { return waveScaleX(d.x); })
            .y0(function (d) { return waveScaleY(Math.sin(Math.PI * 2 * config.waveOffset * -1 + Math.PI * 2 * (1 - config.waveCount) + d.y * 2 * Math.PI)); })
            .y1(function (d) { return (fillCircleRadius * 2 + waveHeight); });
        const waveGroup = gaugeGroup.append("defs")
            .append("clipPath")
            .attr("id", "clipWave" + elementId);
        const wave = waveGroup.append("path")
            .datum(data)
            .attr("d", clipArea)
            .attr("T", 0);

        // The inner circle with the clipping wave attached.
        const fillCircleGroup = gaugeGroup.append("g")
            .attr("clip-path", "url(#clipWave" + elementId + ")");
        fillCircleGroup.append("circle")
            .attr("cx", radius)
            .attr("cy", radius)
            .attr("r", fillCircleRadius)
            .style("fill", config.waveColor);

        // Text where the wave does overlap.
        const text2 = fillCircleGroup.append("text")
           .text(textRounder(textStartValue))
           .attr("class", "liquidFillGaugeText")
           .attr("text-anchor", "middle")
           .attr("font-size", textPixels + "px")
           .style("fill", config.waveTextColor)
           .attr('transform', 'translate(' + radius + ',' + textRiseScaleY(config.textVertPosition) + ')');
        let text2InterpolatorValue = textStartValue;

        // Make the value count up.
        if (config.valueCountUp) {
            text1.transition()
            .duration(config.waveRiseTime)
            .tween("text", function () {
                const i = d3.interpolateNumber(text1InterpolatorValue, textFinalValue);
                return function (t) {
                    text1InterpolatorValue = textRounder(i(t));
                    // Set the gauge's text with the new value and append the % sign
                    // to the end
                    text1.text(text1InterpolatorValue + percentText);
                }
            });
            text2.transition()
                .duration(config.waveRiseTime)
                .tween("text", function () {
                    const i = d3.interpolateNumber(text2InterpolatorValue, textFinalValue);
                    return function (t)  {
                        text2InterpolatorValue = textRounder(i(t));
                    // Set the gauge's text with the new value and append the % sign
                    // to the end
                    text2.text(text2InterpolatorValue + percentText);
                }
                });
        }

        // Make the wave rise. wave and waveGroup are separate so that horizontal and vertical movement can be controlled independently.
        var waveGroupXPosition = fillCircleMargin + fillCircleRadius * 2 - waveClipWidth;
        if (config.waveRise) {
            waveGroup.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(0) + ')')
                .transition()
                .duration(config.waveRiseTime)
                .attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(fillPercent) + ')')
            // .each("start", function () { wave.attr('transform', 'translate(1,0)'); }); // This transform is necessary to get the clip wave positioned correctly when waveRise=true and waveAnimate=false. The wave will not position correctly without this, but it's not clear why this is actually necessary.
            .on("start", function () { wave.attr('transform', 'translate(1,0)'); }); // This transform is necessary to get the clip wave positioned correctly when waveRise=true and waveAnimate=false. The wave will not position correctly without this, but it's not clear why this is actually necessary.
        } else {
            waveGroup.attr('transform', 'translate(' + waveGroupXPosition + ',' + waveRiseScale(fillPercent) + ')');
        }

        if (config.waveAnimate) animateWave();

        function animateWave() {
            wave.attr('transform', 'translate(' + waveAnimateScale(wave.attr('T')) + ',0)');
            wave.transition()
                .duration(config.waveAnimateTime * (1 - wave.attr('T')))
                .ease(d3.easeLinear)
                .attr('transform', 'translate(' + waveAnimateScale(1) + ',0)')
                .attr('T', 1)
                .on('end', function () {
                    wave.attr('T', 0);
                    animateWave(config.waveAnimateTime);
                });
        }

        function GaugeUpdater() {
            this.update = function (value) {
                var newFinalValue = parseFloat(value).toFixed(2);
                var textRounderUpdater = function (value) { return Math.round(value); };
                if (parseFloat(newFinalValue) != parseFloat(textRounderUpdater(newFinalValue))) {
                    textRounderUpdater = function (value) { return parseFloat(value).toFixed(1); };
                }
                if (parseFloat(newFinalValue) != parseFloat(textRounderUpdater(newFinalValue))) {
                    textRounderUpdater = function (value) { return parseFloat(value).toFixed(2); };
                }
                text1.transition()
            .duration(config.waveRiseTime)
            .tween("text", function () {
                const i = d3.interpolateNumber(text1InterpolatorValue, newFinalValue);
                return function (t) {
                    text1InterpolatorValue = textRounder(i(t));
                    // Set the gauge's text with the new value and append the % sign
                    // to the end
                    text1.text(text1InterpolatorValue + percentText);
                }
            });
                text2.transition()
                    .duration(config.waveRiseTime)
                    .tween("text", function () {
                        const i = d3.interpolateNumber(text2InterpolatorValue, newFinalValue);
                        return function (t) {
                            text2InterpolatorValue = textRounder(i(t));
                            text2.text(text2InterpolatorValue + percentText);
                        }
                    });

                var fillPercent = Math.max(config.minValue, Math.min(config.maxValue, value)) / config.maxValue;
                var waveHeight = fillCircleRadius * waveHeightScale(fillPercent * 100);
                var waveRiseScale = d3.scaleLinear()
                    .range([(fillCircleMargin + fillCircleRadius * 2 + waveHeight), (fillCircleMargin - waveHeight)])
                    .domain([0, 1]);
                var newHeight = waveRiseScale(fillPercent);
                var waveScaleX = d3.scaleLinear().range([0, waveClipWidth]).domain([0, 1]);
                var waveScaleY = d3.scaleLinear().range([0, waveHeight]).domain([0, 1]);
                var newClipArea;
                if (config.waveHeightScaling) {
                    newClipArea = d3.area()
                        .x(function (d) { return waveScaleX(d.x); })
                        .y0(function (d) { return waveScaleY(Math.sin(Math.PI * 2 * config.waveOffset * -1 + Math.PI * 2 * (1 - config.waveCount) + d.y * 2 * Math.PI)); })
                        .y1(function (d) { return (fillCircleRadius * 2 + waveHeight); });
                } else {
                    newClipArea = clipArea;
                }

                var newWavePosition = config.waveAnimate ? waveAnimateScale(1) : 0;
                wave.transition()
                    .duration(0)
                    .transition()
                    .duration(config.waveAnimate ? (config.waveAnimateTime * (1 - wave.attr('T'))) : (config.waveRiseTime))
                    .ease(d3.easeLinear)
                    .attr('d', newClipArea)
                    .attr('transform', 'translate(' + newWavePosition + ',0)')
                    .attr('T', '1')
                    .on("end", function () {
                        if (config.waveAnimate) {
                            wave.attr('transform', 'translate(' + waveAnimateScale(0) + ',0)');
                            animateWave(config.waveAnimateTime);
                        }
                    });
                waveGroup.transition()
                    .duration(config.waveRiseTime)
                    .attr('transform', 'translate(' + waveGroupXPosition + ',' + newHeight + ')')
            }
        }

        return new GaugeUpdater();
    }

    var gaugeChartConfig = gaugeChartDefaultSettings();
    gaugeChartConfig.textVertPosition = 0.5
    gaugeChartConfig.waveAnimateTime = 1000;
    gaugeChartConfig.valueCountUp = true;
    gaugeChartConfig.displayPercent = true;
    gaugeChartConfig.waveCount = 1;
    gaugeChartLoad("gaugeChart1", 54.91, gaugeChartConfig);
    gaugeChartLoad("gaugeChart2", 30.91, gaugeChartConfig);
    gaugeChartLoad("gaugeChart3", 45.91, gaugeChartConfig);
    gaugeChartLoad("gaugeChart4", 14.91, gaugeChartConfig);
    gaugeChartLoad("gaugeChart5", 24.91, gaugeChartConfig);
    gaugeChartLoad("gaugeChart6", 34.91, gaugeChartConfig);

}

gaugeChart();