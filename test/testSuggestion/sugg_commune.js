$(function(){
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }
  $("#commune").autocomplete({
    minLength:3,
    source: function( request, response ) {
          $.getJSON( "/recupVilles", {
            term: extractLast( request.term )
          }, response );
        },
/*function (request, response) {
      let url = "/recupVilles";
      $.ajax({
          url: url,
          datatType:'json',
          cache:false,
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
    },*/
  });
});
