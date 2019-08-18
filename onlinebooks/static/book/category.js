$('document').ready(
    function () {
        $('#SearchButton').click(function () {
            event.preventDefault();
            var book_or_author = $('#searchbar').val();
            if (book_or_author != '') {
                $.get("/books/ajax",
                    {
                        q: book_or_author
                    }).done(function (data) {
                        found_results = `<div class="row">`
                        for (var i = 0; i < data.length; i++) {
                            found_results += `<div class="col-12 col-md-6 col-lg-3 p-1">
                                <div class="book-tile-detail">
                                    <a class="d-block text-center" href="/books/detail/${data[i].id}">
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
                        if(data.length == 0)
                        {
                            found_results += `<div class="col-12 text-center pt-5"><span style="font-size: 1.5rem;">Sorry, no results matched your search. Please 
                            double check for any typos or spelling mistakes</span></div>`;
                        }
                        found_results += '</div>'
                        $("#books-section").html(found_results).addClass("container");
                    });
            }
        });

        $("#searchbar").focus(function(){
            $(this).val("");
        });
    }
)