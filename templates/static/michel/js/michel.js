	$(function(){
		var timeout = "";
		var sub = $(".sub-nav")
		$(".sub").mouseover(function(){
			clearTimeout(timeout);
			$(sub).fadeIn();
		}).mouseleave(function(){
			timeout  = setTimeout(function(){$(sub).fadeOut();},50);
		});
		$(".sub-nav").mouseover(function(){
			clearTimeout(timeout);
		}).mouseleave(function(){
			timeout  = setTimeout(function(){$(sub).fadeOut();},50);
		});
	});

