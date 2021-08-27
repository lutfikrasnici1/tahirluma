$(function() {
    $('.add-Product').click(function() {
        $.ajax({
            url: '/addproduct',
            data: $('.product-form').serialize(),
            type: 'POST',
            success: function(response) {
                alert("Başarıyla eklendi")
                $("#products-table").load(" #products-table > *");


            },
            error: function(error) {
                alert("Bir hata var")
            }
        });
    });
});



$(function() {
    $('.sell-Product').click(function() {
        $.ajax({
            url: '/solditem',
            data: $('.sold-form').serialize(),
            type: 'POST',
            success: function(response) {
                alert("İşlem tamamlandı")
                $("#sold-table").load(" #sold-table > *");
                $("#products-table").load(" #products-table > *");
            },
            error: function(error) {
                alert("Bir hata var")
            }
        });
    });
});


$(function() {
    $('.buy-Product').click(function() {
        $.ajax({
            url: '/boughtitem',
            data: $('.buy-form').serialize(),
            type: 'POST',
            success: function(response) {
                alert("İşlem tamamlandı")
                $("#products-table").load(" #products-table > *");
                $("#bought-table").load(" #bought-table > *");
            },
            error: function(error) {
                alert("Bir hata var")
            }
        });
    });
});