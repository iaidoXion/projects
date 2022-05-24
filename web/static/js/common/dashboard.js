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

//맵차트 탭
$(function() {
    $('.btnKorea').click(function() {
        $('.world-map, .si-map, .gu-map, .dong-map').hide();
        $('.korea-map').show();
    });
    $('.btnWorld').click(function() {
        $('.korea-map, .si-map, .gu-map, .dong-map').hide();
        $('.world-map').show();
    });
    $('.btnSi').click(function() {
        $('.korea-map, .world-map, .gu-map, .dong-map').hide();
        $('.si-map').show();
    });
    $('.btnGu').click(function() {
        $('.korea-map, .world-map, .si-map, .dong-map').hide();
        $('.gu-map').show();
        bundangMap();
    });
    $('.btnDong').click(function() {
        $('.korea-map, .world-map, .si-map, .gu-map').hide();
        $('.dong-map').show();
    });

});

//슬라이드배너
$("#demo2").als({
	visible_items: 8,
	scrolling_items: 1,
	orientation: "horizontal",
	circular: "yes",
	autoscroll: "no"
});




