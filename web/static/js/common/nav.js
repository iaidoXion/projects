function confirmLogout() {
    if( confirm("정말 로그아웃 하시겠습니까?") ) {
        location.href = "/logout";
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







