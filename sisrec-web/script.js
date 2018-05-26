let urlBase = "http://localhost:5000/sisrec/api/"

let games = [];

let selectedGame = '';

let similarGames = [];

$(document).ready(function() {
	$.get(urlBase + "categorias", (data)=> {
		for(categoria of data) {
			$(".categoria-list").append(
				"<li>" + categoria + "</li>"
			);
		}
	})
	
	$(this).on('click', '.categoria-list li', function() {
		console.log($(this).text());
		
		$.get(urlBase + "categorias/" + $(this).text(), (data)=> {
			games = data;
			updateGameList();
			$('.game').hide(500);
			$('.similar').hide(500);
			$('.games').hide(500);
			$('.games').show(500);
		})
	});
	
	$(this).on('click', '.game-list li', function() {
		console.log($(this).text());
		selectedGame = $(this).text();
		
		$.get(urlBase + "similarity/" + selectedGame, (data)=> {
			similarGames = data;
			similarGames.length=5;
			updateGameList();
			$('.game').hide(500);
			$('.game').show(500);
			$('.similar').hide(500);
			$('.similar').show(500);
		})
	});
});

function updateGameList() {
	$('.game-list').html("");
	
	for(game of games) {
		$('.game-list').append(
			"<li>" + game + "</li>"
		);
	}
	
	$('.game').html("");
	
	$('.game').append("<b>" + selectedGame + "</b>");
	
	$('.similar-list').html("");
	
	for(game of similarGames) {
		$('.similar-list').append(
			"<li>" + game[0] + " | <b>" + Number((game[1] * 100).toFixed(1)) + "%<b/></li>"
		);
	}
	
}