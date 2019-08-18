$('document').ready(
    function () {
        var getCookie = function (name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        var csrfSafeMethod = function (method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $('.edit-link').click(function () {
            if ($(this).text() == 'Edit') {
                $(this).text("Update");
                $(this).siblings('.col-12').attr("contenteditable", true).focus();
            } else {
                $(this).text("Edit");
                $(this).siblings('.col-12').attr("contenteditable", false).focusout();
                var value = $(this).siblings('.col-12').text();
                const key = $(this).siblings('.col-10').text().toLowerCase().replace(" ", "_");
                let updateData = [key, value]
                var currentSegments = window.location.pathname.split("/");
                $.post(`/accounts/ajax/update/${currentSegments[currentSegments.length - 1]}`, {
                    'attribute': updateData
                }).done(function (data) {
                    $("#updated-alert").css("visibility", "visible").fadeTo(2000, 500).slideUp(500);
                });
            }

        })
    });