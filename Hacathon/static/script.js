// Function to detect if the browser is Chrome
function isChromeBrowser() {
    const userAgent = navigator.userAgent.toLowerCase();
    return /chrome/.test(userAgent) && !/edge|edg|opera/.test(userAgent);
}

// Function to detect if the device is mobile or Android OS
function isMobileOrAndroid() {
    const userAgent = navigator.userAgent.toLowerCase();
    return /iphone|ipad|ipod|android|mobile|tablet/.test(userAgent);
}

// Combined check on page load
window.onload = function () {
    // Check for Chrome browser
    if (!isChromeBrowser()) {
        alert("This webpage can only be accessed using Google Chrome.");
        document.body.innerHTML = `<h1 style="color:red; text-align:center;">Access Denied: Please use Google Chrome to view this site.</h1>`;
        return;
    }

    // Check for mobile or Android OS
    if (isMobileOrAndroid()) {
        alert("This webpage can only be accessed on a desktop or laptop.");
        document.body.innerHTML = `<h1 style="color:red; text-align:center;">Access Denied: Please use a desktop or laptop to view this site.</h1>`;
        return;
    }
};
