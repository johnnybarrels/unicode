$(window).ready( function () {
    let sideNavWidth = $('.sidenav').css('width');
    $('.content-container').css('margin-left', sideNavWidth);

    $(window).on('resize', function() {
        let sideNavWidth = $('.sidenav').css('width');
        $('.content-container').css('margin-left', sideNavWidth);
    });
}
);


$("document").ready(function(){
    $(".fa-caret-square-down").click(function(){
            document.getElementById("option-menu").style.visibility="visible";
    });
  });

$("document").ready(function(){
    $(".fa-times").click(function(){ 
        document.getElementById("option-menu").style.visibility="hidden";
    });
});



$("document").ready(function(){
    $(".fa-plus-circle").click(function(){ 
        $("#new-course-modal").modal("show");
    });
});

$("document").ready(function(){
    $("#new-test-btn").click(function(){ 
        $("#new-test-modal").modal("show");
    });
});

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});