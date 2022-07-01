const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarrLinks = document.getElementsByClassName('navbarr-links')[0]

toggleButton.addEventListener('click', () => {
  navbarrLinks.classList.toggle('active')
})