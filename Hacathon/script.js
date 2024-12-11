// Function to detect if the browser is Google Chrome (excluding Brave and other Chromium-based browsers)
function isGoogleChrome() {
    const userAgent = navigator.userAgent.toLowerCase();
    const isChrome = /chrome/.test(userAgent) && !/edge|edg|opera|brave/.test(userAgent);
    const isBrave = !!navigator.brave || userAgent.includes("brave");
    return isChrome && !isBrave;
}

// Function to detect if the device is mobile or Android OS, even in "desktop mode"
function isMobileOrAndroid() {
    const userAgent = navigator.userAgent.toLowerCase();

    // Detect Android or Mobile
    const isAndroid = /android/.test(userAgent);
    const isMobileDevice = /iphone|ipad|ipod|mobile|tablet/.test(userAgent);

    // Extra check for small screen sizes
    const isSmallScreen = window.innerWidth < 768; // Common breakpoint for mobile devices

    return isAndroid || isMobileDevice || isSmallScreen;
}

// Combined check on page load
window.onload = function () {
    // Check if the browser is Google Chrome
    if (!isGoogleChrome()) {
        alert("This webpage can only be accessed using Google Chrome.");
        document.body.innerHTML = `<h1 style="color:red; text-align:center;">Access Denied: Please use Google Chrome to view this site.</h1>`;
        return;
    }

    // Check if the device is mobile or Android OS
    if (isMobileOrAndroid()) {
        alert("This webpage can only be accessed on a desktop or laptop.");
        document.body.innerHTML = `<h1 style="color:red; text-align:center;">Access Denied: Please use a desktop or laptop to view this site.</h1>`;
        return;
    }
};

const loginholder = document.getElementById('loginholder');
const loginbx = document.getElementsByClassName('loginbx')
const regibx = document.getElementsByClassName('regibx');
    loginholder.addEventListener('click', () => {
        loginholder.style.display = 'none'; // Hide the loginholder
    });

    loginbx.addEventListener('click', () => {
        loginbx.style.display = 'none'; // Hide the loginholder
    });

    regibx.addEventListener('click', () => {
        regibx.style.display = 'none'; // Hide the loginholder
    });