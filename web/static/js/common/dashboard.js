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
    $('.btnWorld').click(function() {
        $('.korea-map, .si-map, .gu-map, .dong-map').hide();
        $('#expandIconBt2, #expandIconBt3, #expandIconBt4').hide();
        $('.world-map').show();
        $('#expandIconBt1').show();
    });
    $('.btnKorea').click(function() {
        $('.world-map, .si-map, .gu-map, .dong-map').hide();
        $('#expandIconBt1, #expandIconBt3, #expandIconBt4').hide();
        $('.korea-map').show();
        $('#expandIconBt2').show();
    });
    $('.btnSi').click(function() {
        $('.korea-map, .world-map, .gu-map, .dong-map').hide();
        $('#expandIconBt1, #expandIconBt2, #expandIconBt4').hide();
        $('.si-map').show();
        $('#expandIconBt3').show();
    });
    $('.btnGu').click(function() {
        $('.korea-map, .world-map, .si-map, .dong-map').hide();
        $('#expandIconBt1, #expandIconBt2, #expandIconBt3').hide();
        $('.gu-map').show();
        $('#expandIconBt4').show();
    });
    $('.btnDong').click(function() {
        $('.korea-map, .world-map, .si-map, .gu-map').hide();
        $('.dong-map').show();
    });

});

// 맵 화면 확장 아이콘
$(document).ready(function(){
    $('#expandIconBt1').show();
});

// 맵 화면 팝업
$(function(){
    $('#expandIconBt1').click(function(){
        $('#popExpandBt1').show();
    });

    $('#closeExpandBt1').click(function(){
        $('#popExpandBt1').hide();
    });
});
$(function(){
    $('#expandIconBt2').click(function(){
        $('#popExpandBt2').show();
    });

    $('#closeExpandBt2').click(function(){
        $('#popExpandBt2').hide();
    });
});
$(function(){
    $('#expandIconBt3').click(function(){
        $('#popExpandBt3').show();
    });

    $('#closeExpandBt3').click(function(){
        $('#popExpandBt3').hide();
    });
});
$(function(){
    $('#expandIconBt4').click(function(){
        $('#popExpandBt4').show();
    });

    $('#closeExpandBt4').click(function(){
        $('#popExpandBt4').hide();
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
    var tNum1 = $('.tableNum1').DataTable({
        dom: 'litfp',
        pageLength: 10,
        searching: false,
        ordering: true,
        info: true,
        paging: true,
        lengthChange: false,
        columnDefs: [
            {
                searchable: false,
                orderable: false,
                targets: 0,
            },
        ],
        order: [[1, 'asc']],
        language: {
            emptyTable: "데이터가 없어요.",
            lengthMenu: "페이지당 _MENU_ 개씩 보기",
            info: "현재 _START_ - _END_ / _TOTAL_건",
            infoEmpty: "데이터 없음",
            infoFiltered: "( _MAX_건의 데이터에서 필터링됨 )",
            search: "에서 검색: ",
            zeroRecords: "일치하는 데이터가 없어요.",
            loadingRecords: "로딩중...",
            processing:     "잠시만 기다려 주세요...",
            paginate: {
                next: "다음",
                previous: "이전"
            }
        }
    });
    tNum1.on('order.dt search.dt', function () {
        let i = 1;

        tNum1.cells(null, 0, { search: 'applied', order: 'applied' }).every(function (cell) {
            this.data(i++);
        });
    }).draw();

    var tNum2 = $('.tableNum2').DataTable({
            dom: 'litfp',
            pageLength: 10,
            searching: false,
            ordering: true,
            info: true,
            paging: true,
            lengthChange: false,
            columnDefs: [
                {
                    searchable: false,
                    orderable: false,
                    targets: 0,
                },
            ],
            order: [[1, 'asc']],
            language: {
                emptyTable: "데이터가 없어요.",
                lengthMenu: "페이지당 _MENU_ 개씩 보기",
                info: "현재 _START_ - _END_ / _TOTAL_건",
                infoEmpty: "데이터 없음",
                infoFiltered: "( _MAX_건의 데이터에서 필터링됨 )",
                search: "에서 검색: ",
                zeroRecords: "일치하는 데이터가 없어요.",
                loadingRecords: "로딩중...",
                processing:     "잠시만 기다려 주세요...",
                paginate: {
                    next: "다음",
                    previous: "이전"
                }
            }
    });

    tNum2.on('order.dt search.dt', function () {
        let i = 1;

        tNum2.cells(null, 0, { search: 'applied', order: 'applied' }).every(function (cell) {
            this.data(i++);
        });
    }).draw();

    var tNum3 = $('.tableNum3').DataTable({
        dom: 'litfp',
        pageLength: 10,
        searching: false,
        ordering: true,
        info: true,
        paging: true,
        lengthChange: false,
        columnDefs: [
            {
                searchable: false,
                orderable: false,
                targets: 0,
            },
        ],
        order: [[1, 'asc']],
        language: {
            emptyTable: "데이터가 없어요.",
            lengthMenu: "페이지당 _MENU_ 개씩 보기",
            info: "현재 _START_ - _END_ / _TOTAL_건",
            infoEmpty: "데이터 없음",
            infoFiltered: "( _MAX_건의 데이터에서 필터링됨 )",
            search: "에서 검색: ",
            zeroRecords: "일치하는 데이터가 없어요.",
            loadingRecords: "로딩중...",
            processing:     "잠시만 기다려 주세요...",
            paginate: {
                next: "다음",
                previous: "이전"
            }
        }
    });

    tNum3.on('order.dt search.dt', function () {
        let i = 1;

        tNum3.cells(null, 0, { search: 'applied', order: 'applied' }).every(function (cell) {
            this.data(i++);
        });
    }).draw();

    var tNum4 = $('.tableNum4').DataTable({
        dom: 'litfp',
        pageLength: 10,
        searching: false,
        ordering: true,
        info: true,
        paging: true,
        lengthChange: false,
        columnDefs: [
            {
                searchable: false,
                orderable: false,
                targets: 0,
            },
        ],
        order: [[1, 'asc']],
        language: {
            emptyTable: "데이터가 없어요.",
            lengthMenu: "페이지당 _MENU_ 개씩 보기",
            info: "현재 _START_ - _END_ / _TOTAL_건",
            infoEmpty: "데이터 없음",
            infoFiltered: "( _MAX_건의 데이터에서 필터링됨 )",
            search: "에서 검색: ",
            zeroRecords: "일치하는 데이터가 없어요.",
            loadingRecords: "로딩중...",
            processing:     "잠시만 기다려 주세요...",
            paginate: {
                next: "다음",
                previous: "이전"
            }
        }
    });

    tNum4.on('order.dt search.dt', function () {
        let i = 1;

        tNum4.cells(null, 0, { search: 'applied', order: 'applied' }).every(function (cell) {
            this.data(i++);
        });
    }).draw();

    var tNum5 = $('.tableNum5').DataTable({
        dom: 'litfp',
        pageLength: 10,
        searching: false,
        ordering: true,
        info: true,
        paging: true,
        lengthChange: false,
        columnDefs: [
            {
                searchable: false,
                orderable: false,
                targets: 0,
            },
        ],
        order: [[1, 'asc']],
        language: {
            emptyTable: "데이터가 없어요.",
            lengthMenu: "페이지당 _MENU_ 개씩 보기",
            info: "현재 _START_ - _END_ / _TOTAL_건",
            infoEmpty: "데이터 없음",
            infoFiltered: "( _MAX_건의 데이터에서 필터링됨 )",
            search: "에서 검색: ",
            zeroRecords: "일치하는 데이터가 없어요.",
            loadingRecords: "로딩중...",
            processing:     "잠시만 기다려 주세요...",
            paginate: {
                next: "다음",
                previous: "이전"
            }
        }
    });

    tNum5.on('order.dt search.dt', function () {
        let i = 1;

        tNum5.cells(null, 0, { search: 'applied', order: 'applied' }).every(function (cell) {
            this.data(i++);
        });
    }).draw();
 });