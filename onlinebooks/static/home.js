$(document).ready(
    function()
    {
        // var move = 0;
        // var last = null;
        $('.scroll-background').click(
            function()
        {
            // if(last != null &&  !last.is($(this)))
            //     move = 0;
           // move += $(this).parent().width();
            $(this).parent().animate({
                scrollLeft: $(this).parent().scrollLeft() + $(this).parent().width()
            }, "slow", function(){
                $(this).siblings('.scroll-background-left').addClass('d-md-block');
                if(Math.abs($(this).get(0).scrollWidth - $(this).scrollLeft() - $(this).outerWidth()) <= 10)
                {
                    $(this).children('.scroll-background').removeClass('d-md-block');
                } 
            });
           // last = $(this);       
                
        });
        $('.scroll-background-left').click(
            function()
        {
            // if(last.parent().siblings('.scroll-background-left').is($(this)))
            //     move -= last.parent().width();
            // else
            //     move = $(this).siblings('.category-books-container').scrollLeft() - $(this).siblings('.category-books-container').width();

            // if (move < 0)
            //     move = 0;    
            var container = $(this).siblings('.category-books-container');  
            container.animate({
                scrollLeft : container.scrollLeft() - container.width()
            }, "slow", function(){
                $(this).children('.scroll-background').addClass('d-md-block')
                if($(this).scrollLeft() == 0)
                    $(this).siblings('.scroll-background-left').removeClass('d-md-block')
            });    
        });
    }
)