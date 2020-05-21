
function createTest(url) {

    $(document).ready( function() {
         
        $('#create-output-question').click( function() {

            form_data = $('#question-form').serializeArray();
            form_data.q_type = 'output';
            
            $.post(url, $('#question-form').serializeArray(),
                function(data, status, xhr) {
                    if(status == 200) {
                        console.log('success');
                    } else {
                        console.log('failure');              
                    }
                },
                'json');
            }
        });

    });
