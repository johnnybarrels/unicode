//-------------------------------------------------------------//
//-----Functions and callbacks in this file form the-----------//
//-----basis for most functionality in our website,------------//
//-----excluding that which controls our ace-editor------------//
//-------------------------------------------------------------//

/* All callbacks which are defined within this ready callback
require no parameters, and control various functionalities
within our website. */

$(window).ready(function () {


    // Initial resize of our main content container's left margin based on the size of our sidenav bar
    let sideNavWidth = $('.sidenav').css('width');
    $('.content-container').css('margin-left', sideNavWidth);

    /* Resize the main content container's left margin in tandem with our sidenav's left margin when the page is scaled.
    This callback and the initial definition above allow our pages to be resized horizontally without elements in our
    main container from collapsing in behind the sidenav */ 
    $(window).on('resize', function () {
        let sideNavWidth = $('.sidenav').css('width');
        $('.content-container').css('margin-left', sideNavWidth);
    });

    // Show or hide our option drop-down on test object boxes 
    $(".fa-caret-square-down").click(function () {
        $("#option-menu").toggle();
    });

    /* The following are modal button assignments littered 
    throughout website. We have used boostrap modal classes
    to support this functionality */

    // for the new course button within our main admin portal
    $("#new-course-btn").click(function () {
        $("#new-course-modal").modal("show");
    });

    // for the new course icon found on the sidenav of all admin views
    $("#new-course-icon").click(function () {
        $("#new-course-modal").modal("show");
    });

    // for the new test button in the top right of our admin course-view
    $("#new-test-btn").click(function () {
        $("#new-test-modal").modal("show");
    });

    // for the rename test button in the top right of our admin test-view
    $("#rename-test-btn").click(function () {
        $("#rename-test-modal").modal("show")
    })

    // for the manage students button in the rop right of our admin-course view
    // allows us to add/remove users from a particular course
    $("#manage-students-btn").click(function () {
        $("#manage-students-modal").modal("show");
    });

    $(".dropdown-toggle").dropdown();

    $('#submit-and-feedback-btn').click(function () {
        $('#feedback-modal').modal('show')
    })


});


/* Hides and shows certain form elements rendering
based on the type of question being entered in our
edit-test view. Additionally sets the question-type
HiddenField based on the type of question selected */

function newQuestionSelector(qType) {
    if (qType == 1) { // If code-output question
        $('#new-question-mcq').hide();
        $('#new-question-solution').show();
        $('#solution-textbox').show();
        $('#solution-mcq').hide()
        $('#question-type').attr('value', 1);
        $('#new-question-form #question-description').css('height', '190px');
    }
    else if (qType == 2) { // If MCQ question
        $('#new-question-mcq').show();
        $('#new-question-solution').show();
        $('#solution-textbox').hide();
        $('#solution-mcq').show()
        $('#question-type').attr('value', 2);
        $('#new-question-form #question-description').css('height', '50px');
    }
    else if (qType == 3) { // If code-submission question
        $('#new-question-mcq').hide();
        $('#new-question-solution').hide();
        $('#question-type').attr('value', 3);
        $('#new-question-form #question-description').css('height', '280px');
    }
};

function validatePassword() {
    var validator = $("#registration-form").validate({
        rules: {
            password_again: {
                equalTo: "#password"
            }
        },
        messages: {
            password_again: "Passwords do not match"
        }
    });
}

// function validatePassword() {
//     confirm("are you sure?");
//     var pswd = $('#password').attr('value');
//     var pswd_rpt = $('#password_again').attr('value');
//     if (pswd != pswd_rpt) {
//         alert("The passwords do not match!");
//         $('#password_again').focus();
//         $('#password_again').closest('form').preventDefault();
//         return;
//     }
// }

// Storing value of MCQ radio button submission
function insertValueToHidden(loop_index, i) {
    mcq_index_str = "#mcq-form-" + loop_index.toString() + " #mcq-answer";
    console.log(mcq_index_str);
    $(mcq_index_str).attr('value', ['a', 'b', 'c', 'd'][i - 1])
}


// $('nav-add-tab').click(function () {
//     if ($('#mcq-option-1').hasClass('active')) {
//         console.log('Hello')
//         $('#new-question-mcq').hide()
//         $('#new-question-solution').show()
//     };

//     if ($('#mcq-option-2').hasClass('active')) {
//         $('#new-question-mcq').show()
//         $('#new-question-solution').show()
//     };

//     if ($('#mcq-option-3').hasClass('active')) {
//         $('#new-question-mcq').hide()
//         $('#new-question-solution').hide()
//     };
// })



