const { shell, ipcRenderer } = require("electron");
const { Notification } = require("electron");
const os = require("os");
const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";



const imgbtn =
  "https://api.iconify.design/ic:baseline-cell-tower.svg?color=%23ffffff";
// search atc callsign du formulaire de recherche la test.html

/** création du systeme d'enregistrement de donnée de electron en variable */
//localStorage.removeItem("plateform");
console.log(localStorage.getItem("plateform"));

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("tableauAtc").hidden = true;
});

document.addEventListener("submit", function () {
  let value = document.getElementById("search-atc").value;
  value = value.toUpperCase();
  fetch(dataIvao)
    .then((response) => response.json()) // one extra step
    .then((data) => {
      console.log(data.clients.atcs);
      //rechercher les données dans le tableau atcs
      data.clients.atcs.forEach((atc) => {
        if (atc.callsign.includes(value)) {
          // cretion d'un array pour stocker les données
          let result = [];
          result.push(atc);
          //affichage les données sur le array
          result.forEach((element) => {
            console.log(element.callsign);
            document.getElementById("tableauAtc").hidden = false;
            document.getElementById("table-atc").innerHTML += `<tr><td>${
              element.callsign
            }</td><td>${
              element.atcSession.frequency
            } MHz</td><td><button class="btn btn-primary" id="plateform" value="${element.callsign}">More Information</button></td></tr>`;
          }
          );
        }
      });
    });
});

document.addEventListener("click", function (e) {
  if (e.target && e.target.id == "plateform") {
    console.log(e.target.value);
    localStorage.setItem("plateform", e.target.value);
    window.location.href = "plateform.html";
  }
});