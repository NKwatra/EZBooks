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
            $('#SearchButton').click(function () {
                event.preventDefault();
                var book_or_author = $('#searchbar').val();
                if (book_or_author != '') {
                    $.get("/books/" + $('h1').text() + "/ajax",
                        {
                            q: book_or_author
                        }).done(function (data) {
                            found_results = `<div class="row">`
                            for (var i = 0; i < data.length; i++) {
                                found_results += `<div class="col-12 col-md-6 col-lg-3 p-1">
                                    <div class="book-tile-detail">
                                        <a class="d-block text-center" href="#">
                                            <img src="/media/${data[i].cover_image}" alt="cover image of ${data[i].title}" class="cover-img">
                                            <div class="mt-md-2">
                                                <p class="book-title">${data[i].title}</p>
                                                <p class="text-muted pl-3 small my-0">By ${data[i].author}</p>
                                                <div class="my-0 d-flex justify-content-around">
                                                    <div class="my-0 text-center rating-background">
                                                        ${data[i].avg_rating}&nbsp;<i class="fas fa-star"></i>
                                                    </div>
                                                     <p class="my-0 font-weight-bold">₹${ data[i].price}</p>
                                                </div>
                                            </div>
                                        </a>
                                    </div>
                                </div>`;
                            }
                            $("#books-section").html(found_results).addClass('container');
                        });
                }
            })    
    }
)