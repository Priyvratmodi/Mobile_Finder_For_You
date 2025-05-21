document.getElementById("ratingForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const payload = {
    "RAM": document.getElementById("ram").value,
    "Processor": document.getElementById("processor").value,
    "Battery": document.getElementById("battery").value,
    "Front Camera": document.getElementById("frontCamera").value,
    "Back Camera": document.getElementById("backCamera").value,
    "Screen Size": document.getElementById("screenSize").value
  };

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
  .then(res => res.json())
  .then(data => {
    let result = "<strong>Predicted Ratings:</strong><br>";
    for (let key in data) {
      result += `➤ ${key}: ${data[key]} / 10<br>`;
    }
    document.getElementById("output").innerHTML = result;
  });
});
