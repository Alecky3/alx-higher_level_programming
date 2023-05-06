$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(res)
	{
		let titles = res.results.map(movie=>{
			return `<li>${movie.title}</li>`
		}
		)
		$("UL#list_movies").append(...titles);
	}
)
