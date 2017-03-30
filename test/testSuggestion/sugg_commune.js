$(function(){
  $('#commune').autocomplete({
    minLength: 2,
    source: "http://infoweb-ens/~jacquin-c/codePostal/commune.php?commune",
    select: function(e, ui) {
        alert(ui.item.value);
    }
  });
});
