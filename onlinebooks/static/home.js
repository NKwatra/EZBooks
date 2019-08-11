$(document).ready(
    function () {
        $('.scroll-background').click(
            function () {
                $(this).parent().animate({
                    scrollLeft: $(this).parent().scrollLeft() + $(this).parent().width()
                }, "slow", function () {
                    $(this).siblings('.scroll-background-left').addClass('d-md-block');
                    if (Math.abs($(this).get(0).scrollWidth - $(this).scrollLeft() - $(this).outerWidth()) <= 10) {
                        $(this).children('.scroll-background').removeClass('d-md-block');
                    }
                });

            });
        $('.scroll-background-left').click(
            function () {
                var container = $(this).siblings('.category-books-container');
                container.animate({
                    scrollLeft: container.scrollLeft() - container.width()
                }, "slow", function () {
                    $(this).children('.scroll-background').addClass('d-md-block')
                    if ($(this).scrollLeft() == 0)
                        $(this).siblings('.scroll-background-left').removeClass('d-md-block')
                });
            });
        $('.book-tile').hover(
            function() {
                $(this).children('.hidden-title').addClass('d-lg-block');
            }, function(){
                $(this).children('.hidden-title').removeClass('d-lg-block');
            }
        );    
    }
)