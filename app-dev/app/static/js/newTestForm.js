$(document).ready( function() {
    console.log('hello');
    $('#create-test-btn').click( function(event) {
        event.preventDefault();
        let url = "{{ url_for('create_test', course_id=course.id) }}";
        console.log(url);
        alert(url);
        $.get(url, function(data) {
            $.post(url, data=$('#createTestForm').serialize(), function(data) {
                if (data.status == 'ok') {
                    $('#new-test-modal').modal('hide');
                    location.reload();  
                } else {
                    console.log('failed');
                }
            });
        });
    });
});             
