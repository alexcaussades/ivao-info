const { shell, ipcRenderer } = require("electron");
const Store = require("electron-store");
const { Notification } = require("electron");
const os = require("os");

const store = new Store();
const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";
// search atc callsign du formulaire de recherche la test.html

/** recuperer le données du formulaire en reception des donées via submit */
const form = document.querySelector("testing");

document.addEventListener("DOMContentLoaded", () => {
  console.log("charegement des données");
  document.getElementById("tableauAtc").hidden = true;
  store.set("atc", "atc");
  store.set("pilot", "pilot");
  console.log(store.get("atc"));
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
            document.getElementById(
              "table-atc"
            ).innerHTML += `<tr><td>${element.callsign}</td><td>${element.atcSession.frequency} Mhz</td><td><form > <input name="get_plateform" type="hidden" id="plateform" value="${element.callsign}"> <button class="btn btn-primary" id="testh" type="submit"><img class="text-center" src="https://api.iconify.design/ic:baseline-cell-tower.svg?color=%23ffffff"></button></form></td></tr>`;
          });
        }
      });
    });
});
