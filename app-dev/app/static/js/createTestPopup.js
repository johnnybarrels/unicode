/*
console.log("hello");
$("document").ready(function() {
    console.log("hello");
    $(".content-container").click(function() {
        console.log("hello");
        $('.content-container').toggle( function() {
            $(".content-container").css({ 'background-color': 'var(--unicode-pale)' });
            $(".content-container").css({ 'opacity' : 1.0 });
        }, function () {
            $(".content-container").css({ 'background-color': black });
            $(".content-container").css({ 'opacity' : 0.7 });
        });      
    });
});
*/

$("document").ready(function() {
    console.log("hello");
    $(".content-container").click(function() {
        console.log("hello");
        //$('.content-container').toggle();
        $('body').toggleClass('active');
        $('.create-test').toggle();
        //$('.test').toggleClass('active');
        return false;
    });
});
