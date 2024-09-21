function showMenu(){
    var menu = document.getElementById('hide-menu');
    menu.style.marginLeft = "0px"
    menu.style.display = "flex"
}

function hideMenu(){
    document.getElementById('hide-menu').style.marginLeft = "100vw";
    document.getElementById('hide-menu').style.display = "none";
}

window.addEventListener('scroll', function() {
    if (window.scrollY > 0) {
        hideMenu();
    }
});

// .hide-menu {
//     width: 100vw;
//     background-color: #ccc;
//     height: 100vh;
//     display: none;
//     position: absolute;
//     z-index: 2000;
// }