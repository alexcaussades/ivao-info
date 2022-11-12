const { shell, ipcRenderer, pushNotifications } = require("electron");
const { Notification } = require("electron");
const os = require("os");
const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";
console.log(localStorage.getItem("plateform"));

let airport = localStorage.getItem("plateform");
airport = airport.split("_");
console.log(airport[0]);

fetch(dataIvao)
  .then((response) => response.json()) // one extra step
  .then((data) => {
    //recherche de l'atc dans le tableau atcs
    data.clients.atcs.forEach((atc) => {
      if (atc.callsign.includes(localStorage.getItem("plateform"))) {
        //affichage des données
        document.getElementById("frequency").innerHTML =
          atc.atcSession.frequency;
        document.getElementById("callsign").innerHTML = atc.callsign;
        document.getElementById("atis_revision").innerHTML = atc.atis.revision;
        document.getElementById("atis_name_airport").innerHTML =
          atc.atis.lines[1];
        document.getElementById("atis_metar").innerHTML = atc.atis.lines[3];
        document.getElementById("atis_rwy").innerHTML = atc.atis.lines[4];
      }
    });
  });

fetch(dataIvao)
  .then((response) => response.json()) // one extra step
  .then((data) => {
    data.clients.pilots.forEach((pilot) => {
      if (pilot.flightPlan.departureId == airport[0]) {
        console.log(pilot.callsign);
      }
    });
  });


