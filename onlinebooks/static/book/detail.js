$('document').ready(function () {

    function showModal(message)
    {
        let loginModal = `<div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="loginModalTitle" aria-hidden="true">
           <div class="modal-dialog modal-dialog-centered" role="document">
             <div class="modal-content">
               <div class="modal-header">
                 <h5 class="modal-title" id="loginModalTitle">Login to continue</h5>
                 <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                   <span aria-hidden="true">&times;</span>
                 </button>
               </div>
               <div class="modal-body">
                ${message}
               </div>
               <div class="modal-footer">
                 <button type="button" class="btn btn-primary" data-dismiss="modal">Close</button>
               </div>
             </div>
           </div>
         </div>`
            $('body').append(loginModal);
            $("#loginModal").modal();
    }

    $("#wishlist-icon").click(function () {
        var currPathSegments = window.location.pathname.split("/");
        if ($('#navbarDropdownMenuLink').length) {
            $(this).toggleClass("fas far");
            $.get("/books/ajax/wishlist", 
            {
                'bookId': currPathSegments[currPathSegments.length - 1],
                'add': $(this).hasClass("fas")
            }).done(function(data){
                if(data["added"])
                    $("#wishlisted-alert").css("visibility", "visible").fadeTo(1500, 500).slideUp(500);
                else
                $("#removed-alert").css("visibility", "visible").fadeTo(1500, 400).slideUp(500);  
            });
        } else {
            showModal("Please login to add this book to wishlist");
            $("#loginModal").on('hidden.bs.modal', function () {
                window.location.replace(`/authenticate/?next=/books/detail/${currPathSegments[currPathSegments.length - 1]}`);
            });
        }
    });

    $("#rateButton").click(function(e){
        if($('#navbarDropdownMenuLink').length == 0)
            {
                e.preventDefault();
                showModal("Please login to rate this product");
                $("#loginModal").on("hidden.bs.modal", function(){
                    window.location.replace(e.target.href);
                })
            }  
    })
});