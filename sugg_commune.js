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
	      $.ajax({
		  url: 'http://localhost:8888/recupVilles',
		  dataType:'jsonp',
		  success: function (data) {
			alert('Works');
		     reponse($.map(data, function (element) {
			alert(element.Installation);
		          return element.Installation;
		      }));
		  },
		  error: function (jqXHR,textStatus,errorThrown) {
		      alert(textStatus);
			alert(errorThrown);
		      response([]);
		  }
	      });
	}
  });
});
