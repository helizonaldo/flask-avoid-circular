$(document).ready(function () {

	toastr.options = {
		"closeButton": true,
		"debug": false,
		"newestOnTop": false,
		"progressBar": true,
		"positionClass": "toast-bottom-right",
		"preventDuplicates": false,
		"onclick": null,
		"showDuration": "300",
		"hideDuration": "1000",
		"timeOut": "5000",
		"extendedTimeOut": "1000",
		"showEasing": "swing",
		"hideEasing": "linear",
		"showMethod": "fadeIn",
		"hideMethod": "fadeOut"
	}
	


	jQuery('form').submit(function(ev){
        ev.preventDefault();
		var form = $(this)
        jQuery.ajax({
            type: form.attr('method'),
            url : form.attr('action'),
            data: form.serialize(),
            cache: false,
            beforeSend: function(xhr, settings) {

                $('[type="submit"]').prepend("<span class=\"spinner-border spinner-border-sm mr-2\"></span>");
                $('#flash').hide();
            },
            success: function( data, status, xhr){
                
                if ('application/json' === xhr.getResponseHeader('Content-Type')){

					if (data.status == "success"){

						toastr.success(data.msg,"Success");  
					}

                }else{
                    console.log("not json")
                    $('#flash').html(data);
					$('#flash').show();

				}
				$('[type="submit"] .spinner-border' ).remove();

            },
            error: function (data) {
                console.log(data);
            }
        });        

        return false;
    });

////////////////////////////////////////////////////////////////////////////

	$(".col a").click(function(event){
		event.preventDefault();
		var href = $(this).attr("href");
		$.ajax = ({
		   url: href,
		   type: "GET",
		   //data: {id:id},
		   dataType: "JSON",
		   cache: false,
           beforeSend: function(xhr, settings) {
			 alert("oi");
		   },
		   success: function( data, status, xhr){
                
                if ('application/json' === xhr.getResponseHeader('Content-Type')){

					if(data.remove){
						$(this).parent( ".col" ).remove();
					}

				}

		   },
		   error: function(data){
				  console.log(data);
			}
		});
	  });

////////////////////////////////////////////////////////////////////////////

	$('#dismiss, .overlay').on('click', 
		function () {
			// hide sidebar
			$('#sidebar').removeClass('active');
			// hide overlay
			$('.overlay').removeClass('active');
	});


	$('#sidebarCollapse').on('click', 
		function () {
			// open sidebar
			$('#sidebar').addClass('active');
			// fade in the overlay
			$('.overlay').addClass('active');
			$('.collapse.in').toggleClass('in');
			$('a[aria-expanded=true]').attr('aria-expanded', 'false');
	});

	$('#navbarSideButton').on('click', 
		function() {
			$('#navbarSide').addClass('reveal');
	});


});
