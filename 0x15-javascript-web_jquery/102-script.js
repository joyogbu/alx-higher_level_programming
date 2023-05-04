$(document).ready(function() {
    let value = $('INPUT#language_code').val();
    $('INPUT#btn_translate').click(function(data) {
        $.post('https://www.fourtonfish.com/hellosalut/hello/', {lang: value}, function() {
            alert($('DIV#hello').text(data));
        });
    });
});
