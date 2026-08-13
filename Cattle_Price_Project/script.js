// whether javascript is connected to the webpage 
// alert("JavaScript is connected");

// ====================
// Smooth scrolling
// ====================
document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", function(event){
        const target = document.querySelector(this.getAttribute("href"));
        if(target){
            event.preventDefault();
            target.scrollIntoView({behavior:"smooth"});
        }
    });
});

// ===================
// Fade into sections
// ===================
const sections = document.querySelectorAll("section");
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.classList.add("show");
        }
    });
});
sections.forEach(section => {
    observer.observe(section);
});
