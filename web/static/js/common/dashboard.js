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

//슬라이드 배너

/*$(function(){
    $('.conBotPrev').click(function(){
        $('#mySlide').css('left', '-100px')

    });
});*/

//슬라이드 배너
$(function(){
  $(".conBotPrev").click(function(){
          $("#mySlide").animate(
          {left:"-9.7%",}, 500
          );
  });
  $(".conBotNext").click(function(){
          $("#mySlide").animate(
          {left:"9.7%",}, 500
          );
  });
})