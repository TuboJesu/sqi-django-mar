document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const clearSearch = document.getElementById("clear-search");
    const genreSelect = document.getElementById("genre-select"); // Updated ID
    const movieCards = document.querySelectorAll(".movie-card");

    // SEARCH FUNCTIONALITY
    searchInput.addEventListener("input", function () {
        const query = searchInput.value.toLowerCase();
        clearSearch.style.display = query.length > 0 ? "inline" : "none";
        filterMovies();
    });

    // CLEAR SEARCH FUNCTIONALITY
    clearSearch.addEventListener("click", function () {
        searchInput.value = "";
        clearSearch.style.display = "none";
        genreSelect.value = "---"; // Reset filter dropdown
        filterMovies();
    });

    // FILTER FUNCTIONALITY (Instantly triggers on selection)
    genreSelect.addEventListener("change", function () {
        filterMovies();
    });

    function filterMovies() {
        const query = searchInput.value.toLowerCase();
        const selectedGenre = genreSelect.value.toLowerCase();

        movieCards.forEach(card => {
            const title = card.getAttribute("data-title").toLowerCase();
            const genre = card.getAttribute("data-genre").toLowerCase();

            // Show only movies that match both search query and filter, or show all if reset
            if ((selectedGenre === "---" || genre === selectedGenre) && title.includes(query)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
        const messages = document.querySelectorAll('#message-container li');
        
        messages.forEach(function(message) {
            setTimeout(function() {
                message.classList.add('fade-out');
                setTimeout(function() {
                    message.style.display = 'none';
                }, 500); // Match with CSS transition duration
            }, 5000); // 5 seconds before starting the fade-out
        });
    });

