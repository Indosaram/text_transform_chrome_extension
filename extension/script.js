console.log("Foreground");

document.addEventListener("mouseup", () => {
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
      });
  }
});
