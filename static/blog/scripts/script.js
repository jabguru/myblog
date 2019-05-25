var nav = document.getElementsByTagName('nav')[0];
var collapse = document.getElementById('toggle-menu');
var mobileMenu = document.getElementById('mobile-menu');

function addStyleToNav() {
	nav.classList.add("shadow");
}

function removeStyleFromNav() {
	nav.classList.remove("shadow");
}

function toggleMenu() {
	mobileMenu.classList.toggle('mobile-hidden');
}

window.addEventListener("scroll", addStyleToNav);
window.addEventListener("mouseup", removeStyleFromNav);

collapse.addEventListener('click', toggleMenu);


