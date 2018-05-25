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
		})
	});
	
	$(this).on('click', '.game-list li', function() {
		console.log($(this).text());
		selectedGame = $(this).text();
		
		$.get(urlBase + "similarity/" + selectedGame, (data)=> {
			similarGames = data;
			similarGames.length=5;
			updateGameList();
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
	
	$('.similar-list').html("");
	
	$('.similar-list').append("<b>" + selectedGame + "</b>");
	for(game of similarGames) {
		$('.similar-list').append(
			"<li>" + game[0] + " | <b>" + Number((game[1] * 100).toFixed(1)) + "%<b/></li>"
		);
	}
	
}