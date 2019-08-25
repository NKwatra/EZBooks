$('document').ready(function(){
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


    $(".delete-icon").click(function(e){
        var currElement = $(this)
        e.preventDefault();
        $.post("/accounts/wishlist/remove", {"book_id": currElement.attr("data-id")})
         .done(function(data){
             currElement.parents('.no-decor').remove();
             $("#removed-alert").css("visibility", "visible").fadeTo(2000, 500).slideUp(500);
             let heading = $("#wishlist-count").text();
             let value = parseInt(heading.split("(")[1])
             $("#wishlist-count").text(`my wishlist(${value -1})`);
         });
    });
})