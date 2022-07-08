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

//페이징
window.onload = function(){
    console.log("");
    console.log("[window onload] : [start]");
    console.log("");
    tableInsert();
};

const tableList = [];
const pageList = 5;
const pageMax = 3
var idx = 0;
var page = 1;


function tableInsert(){
    console.log("");
    console.log("[tableInsert] : [start]");
    console.log("");

    pageInsert(page);
};

function pageInsert(value){
    console.log("");
    console.log("[pageInsert] : [start]" + value);
    console.log("");

    $("#ul-page").empty();

    var startIndex = value;
    var endIndex = tableList.length;

    console.log("");
    console.log("[pageInsert] : [startIndex] : " + startIndex);
    console.log("[pageInsert] : [endIndex] : " + endIndex);
    console.log("");

    var pageCount = 0;
    var pagePlus = 0;
    if(endIndex > pageList){
        pageCount = Math.floor(endIndex / pageList);
        pagePlus = endIndex % pageList;
        if(pagePlus > 0){
            pageCount = pageCount + 1;
        }
        console.log("");
        console.log("[pageInsert] : [pageCount] : " + pageCount);
        console.log("[pageInsert] : [pagePlus] : " + pagePlus);
        console.log("");
    }
    if(startIndex > pageCount){
        startIndex = page;
    }
    else if(startIndex < 0){
        startIndex = page;
    }
    else {
        page = startIndex;
    }

    if(pageCount == 1){
        var insertUl = "<li class='page-item'>"; // 변수 선언
        insertUl += insertUl + "<a class='page-link' href='javascript:void(0)' onclick = 'newPage(1);'>";
        insertUl += insertUl + i;
        insertUl += insertUl + "</a></li>";
        $("#ul-page").append(insertUl); //jquery append 사용해 동적으로 추가 실시
    }
    else if(pageCount >= 2){ //생성해야할 페이지가 2페이지 이상인 경우
        // 이전 페이지 추가 실시
        var insertSTR = "<li class='page-item'>"; // 변수 선언
        insertSTR = insertSTR + "<a class='page-link' href='javascript:void(0)' onclick = 'newPage("+"-1"+");'>";
        insertSTR = insertSTR + "Previous";
        insertSTR = insertSTR + "</a></li>";
        $("#ul-page").append(insertSTR); //jquery append 사용해 동적으로 추가 실시

        // 특정 1, 2, 3 .. 페이지 추가 실시
        var count = 1;
        for(var i=startIndex; i<=pageCount; i++){
            if(count > pageMax){ //최대로 생성될 페이지 개수가 된 경우
                page = i - pageMax; //생성된 페이지 초기값 저장 (초기 i값 4 탈출 인경우 >> 1값 저장)
                break; //for 반복문 탈출
            }
            var insertUl = "<li class='page-item'>"; // 변수 선언
            insertUl = insertUl + "<a class='page-link' href='javascript:void(0)' onclick = 'newPage("+i+");'>";
            insertUl = insertUl + String(i);
            insertUl = insertUl + "</a></li>";
            $("#ul-page").append(insertUl); //jquery append 사용해 동적으로 추가 실시
            count ++;
        }

        // 다음 페이지 추가 실시
        var insertEND = "<li class='page-item'>"; // 변수 선언
        insertEND = insertEND + "<a class='page-link' href='javascript:void(0)' onclick = 'newPage("+"0"+");'>";
        insertEND = insertEND + "Next";
        insertEND = insertEND + "</a></li>";
        $("#ul-page").append(insertEND); //jquery append 사용해 동적으로 추가 실시
    }


    // [페이징 완료 후 >> tr 개수 전체 삭제 >> 페이징 개수에 맞게 다시 표시 실시]
    $("#tbody-init").empty(); //tbody tr 전체 삭제 실시


    // [새롭게 페이지 목록 리스트 처리 실시]
    newPage(startIndex);
};
