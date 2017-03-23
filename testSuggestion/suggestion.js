$(function(){
    $.ajax({
        url: '{{ url_for("ville") }}'
    }).done(function (data) {
        $('#function_name').autocomplete({
            source: data,
            minLength: 2
        });
    });
  $('#commune').autocomplete({
      source : runPyScript();
  });
});
