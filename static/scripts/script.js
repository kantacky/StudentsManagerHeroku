$(function() {
    $('#nav-toggle').on('click', function() {
        $('body').toggleClass('open');
    });
});

$(function() {
    $('[type="submit"]').click(function() {
        $(this).prop('disabled', true);
        $(this).closest('form').submit();
    });
});