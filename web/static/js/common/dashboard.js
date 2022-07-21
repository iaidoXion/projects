// world 이상징후 팝업

$(function() {
    $('.worldBt1').click(function() {
        $('.popWorldBt1').show();
        $(".shadow").show();
    });

    $('.closeWorldBt1').click(function() {
        $('.popWorldBt1').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.worldBt2').click(function() {
        $('.popWorldBt2').show();
        $(".shadow").show();
    });

    $('.closeWorldBt2').click(function() {
        $('.popWorldBt2').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.worldBt3').click(function() {
        $('.popWorldBt3').show();
        $(".shadow").show();
    });

    $('.closeWorldBt3').click(function() {
        $('.popWorldBt3').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.worldBt4').click(function() {
        $('.popWorldBt4').show();
        $(".shadow").show();
    });

    $('.closeWorldBt4').click(function() {
        $('.popWorldBt4').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.worldBt5').click(function() {
        $('.popWorldBt5').show();
        $(".shadow").show();
    });

    $('.closeWorldBt5').click(function() {
        $('.popWorldBt5').hide();
        $('.shadow').hide();
    });
});

//Korea 이상징후 팝업
$(function() {
    $('.koreaBt1').click(function() {
        $('.popWorldBt1').show();
        $(".shadow").show();
    });

    $('.closeKoreaBt1').click(function() {
        $('.popWorldBt1').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.koreaBt2').click(function() {
        $('.popWorldBt2').show();
        $(".shadow").show();
    });

    $('.closeKoreaBt2').click(function() {
        $('.popWorldBt2').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.koreaBt3').click(function() {
        $('.popWorldBt3').show();
        $(".shadow").show();
    });

    $('.closeKoreaBt3').click(function() {
        $('.popWorldBt3').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.koreaBt4').click(function() {
        $('.popWorldBt4').show();
        $(".shadow").show();
    });

    $('.closeKoreaBt4').click(function() {
        $('.popWorldBt4').hide();
        $('.shadow').hide();
    });
});

$(function() {
    $('.koreaBt5').click(function() {
        $('.popWorldBt5').show();
        $(".shadow").show();
    });

    $('.closeKoreaBt5').click(function() {
        $('.popWorldBt5').hide();
        $('.shadow').hide();
    });
});

//Area 이상징후 팝업
$(function() {
    $('#areaBt1').click(function() {
        $('#popAreaBt1').show();
        $(".shadow").show();
    });

    $('#closeAreaBt1').click(function() {
        $('#popAreaBt1').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#areaBt2').click(function() {
        $('#popAreaBt2').show();
        $(".shadow").show();
    });

    $('#closeAreaBt2').click(function() {
        $('#popAreaBt2').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#areaBt3').click(function() {
        $('#popAreaBt3').show();
        $(".shadow").show();
    });

    $('#closeAreaBt3').click(function() {
        $('#popAreaBt3').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#areaBt4').click(function() {
        $('#popAreaBt4').show();
        $(".shadow").show();
    });

    $('#closeAreaBt4').click(function() {
        $('#popAreaBt4').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#areaBt5').click(function() {
        $('#popAreaBt5').show();
        $(".shadow").show();
    });

    $('#closeAreaBt5').click(function() {
        $('#popAreaBt5').hide();
        $('.shadow').hide();
    });
});

//Zone 이상징후 팝업
$(function() {
    $('#zoneBt1').click(function() {
        $('#popZoneBt1').show();
        $(".shadow").show();
    });

    $('#closeZoneBt1').click(function() {
        $('#popZoneBt1').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#zoneBt2').click(function() {
        $('#popZoneBt2').show();
        $(".shadow").show();
    });

    $('#closeZoneBt2').click(function() {
        $('#popZoneBt2').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#zoneBt3').click(function() {
        $('#popZoneBt3').show();
        $(".shadow").show();
    });

    $('#closeZoneBt3').click(function() {
        $('#popZoneBt3').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#zoneBt4').click(function() {
        $('#popZoneBt4').show();
        $(".shadow").show();
    });

    $('#closeZoneBt4').click(function() {
        $('#popZoneBt4').hide();
        $('.shadow').hide();
    });
});
$(function() {
    $('#zoneBt5').click(function() {
        $('#popZoneBt5').show();
        $(".shadow").show();
    });

    $('#closeZoneBt5').click(function() {
        $('#popZoneBt5').hide();
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

//datatable
$(document).ready(function(){
    $(".popTable").DataTable({
        "dom": 'ltfip',
        "pageLength": 10,
        "searching": false,
        "ordering": false,
        "info": true,
        "paging": true,
        "lengthChange": true,
   });
});
