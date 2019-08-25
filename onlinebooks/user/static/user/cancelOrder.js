$('document').ready(function(){

    function showModal(message)
    {
        let loginModal = `<div class="modal fade" id="confirmModal" tabindex="-1" role="dialog" aria-labelledby="loginModalTitle" aria-hidden="true">
           <div class="modal-dialog modal-dialog-centered" role="document">
             <div class="modal-content">
               <div class="modal-header">
                 <h5 class="modal-title" id="loginModalTitle">Cancel It?</h5>
                 <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                   <span aria-hidden="true">&times;</span>
                 </button>
               </div>
               <div class="modal-body">
                ${message}
               </div>
               <div class="modal-footer">
                 <button type="button" class="btn btn-success" data-dismiss="modal">No</button>
                 <button type="button" class="btn btn-danger" id="yesButton">Yes</button>
               </div>
             </div>
           </div>
         </div>`
            $('body').append(loginModal);
            $("#confirmModal").modal();
    }

    $('.cancel-btn').click(function(){
        var id = $(this).attr("data-id");
        var currButton = $(this);
        showModal("Are you sure you want to cancel to order?");
        $("#yesButton").click(function(){
            $("#confirmModal").modal('hide');
            $.get(`/order/cancel/${id}`)
            .done(function(data){
                if(data["deleted"]){
                    currButton.parents('.order-container').remove();
                    $("#removed-alert").css("visibility", "visible").fadeTo(2000, 500).slideUp(500);
                    let heading = $("#orders-count").text();
                    let value = parseInt(heading.split("(")[1])
                    $("#orders-count").text(`my wishlist(${value -1})`);
                }else{
                    alert("Some error occured please try again later");
                }
            });
        });
    });
});