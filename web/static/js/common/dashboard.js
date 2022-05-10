// 세계 맵차트 팝업
$(document).ready(function() {
    $('#popBtWorld').click(function() {
        $('#popWorld').show();
        $(".shadow").show();
        $('#popKorea').hide();
    });

    $('#closeWorld').click(function() {
        $('#popWorld').hide();
        $('.shadow').hide();
    });
});

// 국내 맵차트 팝업
$(document).ready(function() {
    $('#popBtKorea').click(function() {
        $('#popKorea').show();
        $(".shadow").show();
        $('#popWorld').hide();
    });

    $('#closeKorea').click(function() {
        $('#popKorea').hide();
        $('.shadow').hide();
    });
});

//국내지도 탭
$(function() {
    $('.btnKorea').click(function() {
        $('.mapChartMenuKorea, .korea-map').show();
        $('.mapChartMenuWorld, .world-map').hide();
    });
    $('.btnWorld').click(function() {
        $('.mapChartMenuKorea, .korea-map').hide();
        $('.mapChartMenuWorld, .world-map').show();
    });
});


$("#demo2").als({
	visible_items: 8,
	scrolling_items: 1,
	orientation: "horizontal",
	circular: "yes",
	autoscroll: "no"
});
/*
//슬라이드 배너
$(function(){
    $(".conBotPrev").click(function(){
        $(".conBotWrap").animate({
        left : "+=11.45%"
        }, 500);
    });
    $(".conBotNext").click(function(){
        $(".conBotWrap").animate({
        left : "-=11.45%"
        }, 500);
    });
});

*/


