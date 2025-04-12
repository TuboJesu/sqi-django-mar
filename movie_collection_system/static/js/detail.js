document.addEventListener("DOMContentLoaded", () => {
    const card = document.querySelector(".movie-card");
    card.style.opacity = 0;
    card.style.transform = "translateY(40px)";
    setTimeout(() => {
        card.style.transition = "all 0.6s ease";
        card.style.opacity = 1;
        card.style.transform = "translateY(0)";
    }, 100);
});
