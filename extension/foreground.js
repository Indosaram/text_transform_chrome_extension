var s = document.createElement('script');
s.src = chrome.runtime.getURL('./script.js');
s.onload = function() {
    this.remove();
};
document.head.appendChild(s);
console.log("Appended script to <head>")