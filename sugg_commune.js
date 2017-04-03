$(function(){
  $("#commune").autocomplete({
    minLength:3,
    source: function( request, response ) {
	      $.ajax({
		  url: 'http://localhost:8888/recupVilles',
		  dataType:'jsonp',
		  type:"GET",
		  success: function (data) {
		     reponse($.map(data, function (element) {
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
	$('#submit').click(function(){
		var res;
			$.ajax({
				url : 'http://localhost:8888/ville/' + $('#commune').val(),
				dataType:'json',
				success:function(data){
					alert(data.Installation);
					res = data.Installation;
				},
				error : function(resultat, statut, erreur){
					 alert(resultat + statut + erreur);

				},
			       complete : function(resultat, statut){
					alert(resultat);
			       }
			});
	    var table = $('#tableau');

	    var tr = document.createElement('tr');
	    table.append(tr);
	     
	    var td = document.createElement('td');
	    tr.append(td);
	    var tdText = document.createTextNode(res);
	    td.append(tdText);
	});
});
