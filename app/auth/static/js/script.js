$(document).ready(function(){

    var csrf_token = "{{ csrf_token() }}";

    jQuery('form').submit(function(ev){
        ev.preventDefault();
        var form = $(this)
        jQuery.ajax({
            type: form.attr('method'),
            url : form.attr('action'), //"{{url_for('test')}}"
            data: form.serialize(),
            cache: false,
            beforeSend: function(xhr, settings) {

                $('[type="submit"]').prepend("<span class=\"spinner-border spinner-border-sm mr-2\"></span>");
                $('#flash').hide();
            },
            success: function( data, status, xhr){
                
                if ('application/json' === xhr.getResponseHeader('Content-Type')){
                    window.location.href = data.redirect;
                }else{
                    console.log("not json")
                    $('[type="submit"] .spinner-border' ).remove();
                    $('#flash').html(data);
                    $('#flash').show();
                }
            },
            error: function (data) {
                console.log(data);
            }
        });        

        return false;
    });

/*
<button class="btn btn-primary" disabled>
  <span class="spinner-border spinner-border-sm"></span>
  Loading..
</button>

<input class="btn btn-primary" id="submit" name="submit" type="submit" value="Sign up">
<input class="btn btn-primary" id="submit" name="submit" type="submit" value="Sign up">


<div class="input-group-append">
            <span class="input-group-text input-password-hide" style="cursor: pointer;">
				<i class="fa fa-eye"></i> 
			</span>
</div>

$(function () {
    $('[type="submit"]').
}

$(function () {
    $('[data-toggle="password"]').each(function () {
        var input = $(this);
        var eye_btn = $(this).parent().find('.input-group-text');
        eye_btn.css('cursor', 'pointer').addClass('input-password-hide');
        eye_btn.on('click', function () {
            if (eye_btn.hasClass('input-password-hide')) {
                eye_btn.removeClass('input-password-hide').addClass('input-password-show');
                eye_btn.find('.fa').removeClass('fa-eye').addClass('fa-eye-slash')
                input.attr('type', 'text');
            } else {
                eye_btn.removeClass('input-password-show').addClass('input-password-hide');
                eye_btn.find('.fa').removeClass('fa-eye-slash').addClass('fa-eye')
                input.attr('type', 'password');
            }
        });
    });
});

*/

});