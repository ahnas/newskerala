$(document).on('submit', 'form.ajax', function(e) {
    e.preventDefault();
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var isReset = $this.hasClass('reset');
    var isReload = $this.hasClass('reload');
    var isRedirect = $this.hasClass('redirect');

    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",

        success: function(data) {

            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
            var redirect = data.redirect;
            var redirect_url = data.redirect_url;

            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                Swal.fire({
                    title: title,
                    text: message,
                    icon: 'success',
                }).then(function() {
                    if (isRedirect == 'true') {
                        window.location.href = redirect_url;
                    }
                    if (isReload == 'true') {
                        window.location.reload();
                    }
                    if (isReset == 'true') {
                        window.location.reset();
                    }
                });

            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    text: message,
                    icon: "error"
                });

            }
        },
        error: function(data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                text: message,
                icon: "error"
            });
        }
    });
});
