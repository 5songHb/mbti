$(document).ready(function(){
    var answers = [];
    $("input[name='answer']").change(function(){
        var answer = $(this).val();
        answers.push(answer);
        var form = $(this).parent().parent().parent();
        var next_form = form.next();
        setTimeout(function(){
            form.remove();
            next_form.css('display', 'block');
        }, 550);
    });
});
