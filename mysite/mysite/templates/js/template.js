$(function() {
	/*$(".loginform").hide();*/
	$(".login").click(function(event) {
		$(".loginform").show();
		$(".loginform").load("/login");
	});
	$(".close").click(function(event) {
		$(".loginform").hide();
	});
});
