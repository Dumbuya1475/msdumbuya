const nav = document.querySelector(".nav"),
  navOpenBtn = document.querySelector(".navOpenBtn"),
  navCloseBtn = document.querySelector(".navCloseBtn"),
  toggleButton = document.getElementById("theme-toggle"),
  cursor = document.querySelector(".custom-cursor");

// // Navigation Toggle
// navOpenBtn.addEventListener("click", () => {
//   nav.classList.add("openNav");
//   nav.classList.remove("openSearch");
// });

// navCloseBtn.addEventListener("click", () => {
//   nav.classList.remove("openNav");
// });

// Dark Mode Toggle
toggleButton.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");

  // Save user preference in local storage
  if (document.body.classList.contains("dark-mode")) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
});

// Apply saved theme on page load
if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark-mode");
}

// Scroll Fade-in Effect
document.addEventListener("DOMContentLoaded", function () {
  const elements = document.querySelectorAll(".fade-in");

  function checkScroll() {
    elements.forEach((el) => {
      if (el.getBoundingClientRect().top < window.innerHeight * 0.9) {
        el.classList.add("show");
      }
    });
  }

  window.addEventListener("scroll", checkScroll);
  checkScroll(); // Run on page load
});

// Custom Cursor Effect
document.addEventListener("mousemove", (e) => {
  cursor.style.left = `${e.clientX}px`;
  cursor.style.top = `${e.clientY}px`;
});
