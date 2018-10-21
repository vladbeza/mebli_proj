var maxHeight = 0;

//document.addEventListener("DOMContentLoaded", function(event) {
//    justify()
//});

$(document).ready(function() {

    justify();
    var details = document.getElementsByClassName("details_btn");
    for (i = 0; i < details.length; i++)
    {
        $(details[i]).css({'bottom':'100%'});
    };
});


window.onresize = justify();

function justify()
{
   $(".col-product_review").each(function(){
  if ( $(this).height() > maxHeight )
  {
    maxHeight = $(this).height();
   }
    });

    $(".col-product_review").height(maxHeight);

}

