window.addEventListener("load", function (event) {
    subtitle = document.getElementsByClassName("subtitle")[0];
    style = window.getComputedStyle(subtitle)
    console.log(style.marginLeft, style.marginRight);
});