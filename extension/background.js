console.log("Start transformation!");

chrome.tabs.onActivated.addListener(() => {
  injectScript();
});

async function injectScript() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ["foreground.js"],
  });
}
