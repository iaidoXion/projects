//datatable
$(document).ready(function(){
    $("#assetTable").DataTable({
        "dom": 'tflip',
        "searching": false,
        "ordering": true,
        "info": true,
        "paging": true,
        "lengthChange": false,
        "pageLength": 10

   });
});