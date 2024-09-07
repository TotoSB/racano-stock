function showMenu(){
    var menu = document.getElementById('hide-menu');
    menu.style.marginLeft = "0px"
}

function hideMenu(){
    document.getElementById('hide-menu').style.marginLeft = "100vw";
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