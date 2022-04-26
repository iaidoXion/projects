function confirmLogout() {
    if( confirm("정말 로그아웃 하시겠습니까?") ) {
        location.href = "/web/logout";
    }
}


//클릭시 유저정보 팝업
$(function() {
    $('.userInfo').click(function() {
        $('.userInfoOpen').show();
    });
    $('.userInfoClose').click(function() {
        $('.userInfoOpen').hide();
    });
})






/*// 유저 정보 클릭시 토글
$(".userInfo").on("click", function() {
  $(".userInfoOpen").toggle();
});*/



/*// 클릭시 유저정보 팝업
$(document).ready(function() {
    $('.userInfo').click(function() {
        $('.userInfoOpen').show();
    });
})*/


/*
$('.userInfo').click(function(event){
    event.stopPropagation();
    $('.userInfoOpen').toggle();
});

$(document).click(function(e){
    if(!$(e.target).hasClass(".userInfoOpen")) {
        $('.userInfoOpen').hide();
    }
});
*/






/*//영역 외 클릭시 팝업 close
$(document).mousedown(function(e){
$('.userInfoOpen').each(function(){
        if( $(this).css('display') == 'block' )
        {
            var l_position = $(this).offset();
            l_position.right = parseInt(l_position.left) + ($(this).width());
            l_position.bottom = parseInt(l_position.top) + parseInt($(this).height());


            if( ( l_position.left <= e.pageX && e.pageX <= l_position.right )
                && ( l_position.top <= e.pageY && e.pageY <= l_position.bottom ) )
            {
                //alert( 'popup in click' );
            }
            else
            {
                //alert( 'popup out click' );
                $(this).hide();
            }
        }
    });
});*/







