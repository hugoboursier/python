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
            ville: extractLast( request.term )
          }, response );
        },
/*function (request, response) {
	      let url = "/recupVilles";
	      $.ajax({
		  url: url,
		  datatType:'json',
		  cache:false,
		  method:'GET',
		  success: function (data) {
		      var transformed = $.map(data, function (element) {
		          return {
		                label: element.ville,
		          };
		      });
		      response(transformed);
		  },
		  error: function (data) {
		      alert(data);
		      response([]);
		  }
	      });
	    }*/
  });
});
