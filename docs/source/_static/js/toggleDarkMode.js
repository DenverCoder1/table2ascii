function setCookie(cname, cvalue, exdays = 365) {
    const date = new Date();
    date.setTime(date.getTime() + exdays * 24 * 60 * 60 * 1000);
    const expires = "expires=" + date.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    const name = cname + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookies = decodedCookie.split(";");
    for (const c of cookies) {
        let cookie = c;
        while (cookie.charAt(0) == " ") {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

function toggleDarkMode() {
    if (DarkReader.isEnabled()) {
        DarkReader.disable();
        setCookie("darkMode", "false");
    } else {
        DarkReader.enable();
        setCookie("darkMode", "true");
    }
}

window.addEventListener("load", function () {
    const topbar = document.querySelector(".header-article__right");
    topbar.innerHTML += `<button type="button" class="headerbtn" data-toggle="tooltip"
                data-placement="bottom" onclick="toggleDarkMode()" aria-label="Toggle dark mode"
                title="" data-original-title="Toggle dark mode">
                <span class="headerbtn__icon-container">
                    <i class="fas fa-moon"></i>
                </span>
            </button>`;
    topbar.style.opacity = "1";
    if (getCookie("darkmode") == "true") {
        DarkReader.enable();
    } else if (getCookie("darkmode") == "false") {
        DarkReader.disable();
    } else {
        DarkReader.auto();
    }
});

DarkReader.auto();
