/*==================== SHOW NAVBAR ====================*/
const showMenu = (headerToggle, navbarId) =>{
  const toggleBtn = document.getElementById(headerToggle),
  nav = document.getElementById(navbarId)
  
  // Validate that variables exist
  if(headerToggle && navbarId){
      toggleBtn.addEventListener('click', ()=>{
          // We add the show-menu class to the div tag with the nav__menu class
          nav.classList.toggle('show-menu')
          // change icon
          toggleBtn.classList.toggle('bx-x')
      })
  }
}
showMenu('header-toggle','navbar')

/*==================== LINK ACTIVE ====================*/
const linkColor = document.querySelectorAll('.nav__link')

function colorLink(){
  linkColor.forEach(l => l.classList.remove('active'))
  this.classList.add('active')
}

linkColor.forEach(l => l.addEventListener('click', colorLink))

const targetDiv = document.getElementById("form");
const updbtm = document.getElementById("update");
const btn = document.getElementById("toggle");
function btnfunction () {
  console.log("Hello world1!");
  if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
  } else {
    targetDiv.style.display = "block";
  }
  if (btn.style.display !== "none") {
    btn.style.display = "none";
  } else {
    btn.style.display = "block";
  }
};

function updfunction () {
  if (targetDiv.style.display !== "none") {
    targetDiv.style.display = "none";
  } else {
    targetDiv.style.display = "block";
  }
  if (btn.style.display !== "none") {
    btn.style.display = "none";
  } else {
    btn.style.display = "block";
  }
};