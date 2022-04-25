function confirmLogout() {
    if( confirm("정말 로그아웃 하시겠습니까?") ) {
        location.href = "/web/logout";
    }
}

// 유저 정보 클릭시 토글
$(".userInfo").on("click", function() {
  $(".userInfoOpen").toggle();
});