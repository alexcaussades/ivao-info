const { ivaoDataAtcCallsingJocker } = require("./ivaofiles");
const { dialog } = require("electron");
const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";
// search atc callsign du formulaire de recherche la test.html

/** recuperer le données du formulaire en reception des donées via submit */
const form = document.querySelector("testing");

document.addEventListener("DOMContentLoaded", () => {
  console.log("charegement des données");
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
          result.push(atc.callsign);
          console.log(result.length);
          //affichage les données sur le array
          result.forEach((element) => {
            console.log(element);
            document.getElementById("tableauAtc").hidden = false;
            document.getElementById(
              "table-atc"
            ).innerHTML += `<tr><td>${element}</td></tr>`;
          });
        }
      });
    });
});
