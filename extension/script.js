var popupId = "customPopup";

function addCSS() {
  var popupElement = document.getElementById(popupId);

  var width = "300px";
  var height = "500px";

  Object.assign(popupElement.style, {
    background: "black",
    color: "white",
    width: width,
    height: height,
  });
}

function preparePopup() {
  var popupElement = document.getElementById(popupId);
  if (popupElement) {
    popupElement.remove();
  }

  var div = document.createElement("div");
  div.setAttribute("id", "customPopup");
  Object.assign(div.style, {
    fontSize: "16px",
    zIndex: 1000,
    display: "block",
    position: "absolute",
    margin: "auto",
    padding: "20px",
  });
  document.body.appendChild(div);

  document.addEventListener("mouseup", () => {});
}

function closePopup() {
  var popupElement = document.getElementById(popupId);
  popupElement.remove();
}

onmouseup = function (event) {
  preparePopup();
  var text = document.getSelection().toString();
  if (text !== "") {
    html = `<div class="spinner"></div>
    <style>
    @keyframes spinner {
      from {transform: rotate(0deg); }
      to {transform: rotate(360deg);}
    }
     
    .spinner {
      box-sizing: border-box;
      position: absolute;
      top: 50%;
      left: 50%;
      width: 64px;
      height: 64px;
      margin-top: -32px;
      margin-left: -32px;
      border-radius: 50%;
      border: 8px solid transparent;
      border-top-color: #f19022;
      border-bottom-color: #f19022;
      animation: spinner .8s ease infinite;
      background: black;
    }</style>`;
    var popupElement = document.getElementById(popupId);
    popupElement.innerHTML = html;
    popupElement.style.left = event.pageX + "px";
    popupElement.style.top = event.pageY + "px";

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
        json_data = json;
        console.log(json);

        ext_summaries = json.ext_summary.split(". ");

        html = `<div id="summary">
          <div id="keyword__button">
          <h3>키워드</h3>
          <div id="button" onclick="closePopup()" style="cursor:pointer">x</div>
          </div>
          <ul>
            ${json.keywords
              .map((keyword) => {
                return `<li>#${keyword.replace(" ", "_")}</li>`;
              })
              .join("")}
          </ul>
          <hr class="solid">

          <h3>AI 생성 요약</h3>
          <p>${json.abs_summary}</p>

          <hr class="solid">
          <h3>세줄 요약</h3>
          <ul>
            <li>${ext_summaries[0]}</li>
            <li>${ext_summaries[1]}</li>
            <li>${ext_summaries[2]}</li>
          </ul>
        <div>
        <style>
        
        #summary > ul, #summary > ul > li:nth-child(3) > ul{
          list-style-type: circle;
          list-style-position: inside;
          padding-left: 2px;
        }
        
        #summary > hr.solid {
          border-top: 3px solid #bbb;
        }

        #summary > h3 {
          margin-top: 10px;
        }

        #keyword__button {
          display: flex;
          justify-content: space-between;
        }

        #close {
          color: white;
        }
        </style>`;

        addCSS();
        var popupElement = document.getElementById(popupId);
        popupElement.innerHTML = html;
        popupElement.style.left = event.pageX + "px";
        popupElement.style.top = event.pageY + "px";
      });
  }
};
