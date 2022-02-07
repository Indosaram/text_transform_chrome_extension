console.log("Foreground");
var div = document.createElement("div");
div.setAttribute("id", "customPopup");
Object.assign(div.style, {
  fontSize: "13px",
  zIndex: 1000,
  display: "block",
  position: "relative",
  background: "black",
  color: "white",
});
document.body.insertBefore(div, document.body.firstChild);

document.addEventListener("mouseup", () => {});

onmouseup = function (event) {
  var text = document.getSelection().toString();
  if (text !== "") {
    fetch("http://localhost:8000/text", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({
        text: text,
      }),
    })
      .then((res) => {
        return res.json();
      })
      .then((json) => {
        console.log(json);

        html = `<ul>
        <li>Keywords: ${json.keywords}</li>
        <li>Abs summary: ${json.abs_summary}</li>
        <li>Ext summary: ${json.ext_summary}</li>
        </ul>`;

        document.getElementById("customPopup").innerHTML = html;
        document.getElementById("customPopup").style.left = event.pageX + "px";
        document.getElementById("customPopup").style.top = event.pageY + "px";
      });
  }
};
