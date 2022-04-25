// 맵차트 팝업
$(document).ready(function() {
    $('#popBt').click(function() {
        $('#pop').show();
        $(".shadow").show();
    });

    $('#close').click(function() {
        $('#pop').hide();
        $('.shadow').hide();
    });
});

