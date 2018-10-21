
function openModal()
{
    var modal = document.getElementById("modalBuyId");
   modal.style.display = "block";
}

window.onclick = function(event) {
    var modal = document.getElementById("modalBuyId");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function closeModal()
{
   var modal = document.getElementById("modalBuyId");
   modal.style.display = "none";
}
