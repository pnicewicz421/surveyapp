$(document).ready(function() {
	
	$(".form-inline").click(function() {
		// get the JSON
		//$("." + answer).text("Processing");

		$.post('/processresponse',  {
			answer: $('input[name="answer"]').val()
			}).done(function(data) {
			$("." + answer).text("Processed " + data.answer)
		}).fail(function() {
			$("." + answer).text("Could not process");
		});
			
		

	});
	
	

});