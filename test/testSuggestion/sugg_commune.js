$(function(){
  $("#commune").autocomplete({
    minLength:3,
    source: function (request, response) {
      let url = "/recupVilles";
      $.ajax({
          url: url,
          datatType:'json',
          cache:false,
          data: {
            query: request.term
          },
          success: function (data) {
              var transformed = $.map(data, function (element) {
                  return {
                        label: element.Nom,
                  };
              });
              response(transformed);
          },
          error: function (data) {
              alert(data);
              response([]);
          }
      });
    },
  });
});
