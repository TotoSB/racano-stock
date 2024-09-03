let vid = document.getElementById("myVideo");

function Pause() {
    if (vid.className === "paused"){
        vid.play();
        let btn = document.getElementById("butoncito");
        btn.classList.remove("fa-play");
        btn.classList.add("fa-pause");
        vid.classList.remove("paused");
    }
    else {
        vid.pause();
        let btn = document.getElementById("butoncito");
        btn.classList.remove("fa-pause");
        btn.classList.add("fa-play");
        vid.classList.add("paused");
    }
}