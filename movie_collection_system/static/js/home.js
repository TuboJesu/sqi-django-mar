document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const clearSearch = document.getElementById("clear-search");
    const movieCards = document.querySelectorAll(".movie-card");

    searchInput.addEventListener("input", function () {
        const query = searchInput.value.toLowerCase();

        // Show "X" if text is entered, hide otherwise
        clearSearch.style.display = query.length > 0 ? "inline" : "none";

        movieCards.forEach(card => {
            const title = card.getAttribute("data-title");
            card.style.display = title.includes(query) ? "block" : "none";
        });
    });

    clearSearch.addEventListener("click", function () {
        searchInput.value = "";
        clearSearch.style.display = "none";

        movieCards.forEach(card => {
            card.style.display = "block"; // Show all movies again
        });
    });
});
