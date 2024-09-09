$(document).ready(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $("#myFormRegisterVoucher").submit(function(event) {
        event.preventDefault();
        
        const fullName = $(this).find('input[name="full_name"]').val()
        const phone = $(this).find('input[name="phone"]').val()
        const email = $(this).find('input[name="email"]').val()

        const csrftoken = getCookie('csrftoken');
        $.ajax({
            method: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-Requested-With", "XMLHttpRequest");
            },
            url: urlRegisterVoucher,
            data: {
                fullName,
                phone,
                email,
                csrfmiddlewaretoken: csrftoken
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: () => {

                toastr.success('Gửi thông thông tin thành công...!')
            },
            error: () => {

                toastr.error('Gửi thông thông tin thất bại...!')
            } 
        })
        

        

    })
})