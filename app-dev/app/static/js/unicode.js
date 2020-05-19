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
    $("#option-btn").click(function(){
        // document.getElementById("lala").style.backgroundColor="pink";
        document.getElementById("options").style.display="visible";
        document.getElementById("option-menu").style.display="visible";
        $("li").toggle("slow");
    });
  });
