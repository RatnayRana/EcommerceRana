$(function () {
    $('.quantity-right-plus').unbind('click').bind('click',function(e){
        e.preventDefault()
        var $qty=$(this).closest('div').find('#quantity_Value');
        var currentVal = parseInt($qty.val());
          // Log the current value
        if (!isNaN(currentVal)) {
            if (currentVal<10){
                currentVal = currentVal+1
                $qty.val(currentVal)

                addToCartAjax(currentVal);
            }
        }
        console.log(currentVal);
    });

    $('.quantity-right-minus').unbind('click').bind('click',function(e){
        e.preventDefault()
        var $qty=$(this).closest('div').find('#quantity_Value');
        var currentVal = parseInt($qty.val());
          // Log the current value
        if (!isNaN(currentVal)) {
            if (currentVal>1){
                currentVal = currentVal-1
                $qty.val(currentVal)

                addToCartAjax(currentVal);
            }
        }

    })
    function addToCartAjax(currentVal) {
        $.ajax({
            type: "GET",
            url: '/addToCart/',
            data: {
                "currentVal": currentVal,
            },
            dataType: "json",
            success: function (data) {            
            },
            error: function () {
        
            }
        });
    }
});
