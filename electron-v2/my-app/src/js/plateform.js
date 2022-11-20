const { shell, ipcRenderer, pushNotifications } = require("electron");
const { Notification } = require("electron");
const os = require("os");
const { mainModule } = require("process");
const { chart } = require("../js/chart.js");
const Online = require("../js/class/timeOnline.js");
const { online } = require("../js/class/timeOnline.js");
const { rating } = require("../js/class/ratings.js");
const Rating = require("../js/class/ratings.js");

const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";

/** creation d'une boite de dialog depuis electron */

document.getElementById("btn").addEventListener("click", () => {
  ipcRenderer.send("open-file-dialog-for-file");
});

let airport = localStorage.getItem("plateform");
airport = airport.split("_");

let departureId = [];
let arrivalId = [];

fetch(dataIvao)
  .then((response) => response.json()) // one extra step
  .then((data) => {
    //recherche de l'atc dans le tableau atcs
    data.clients.atcs.forEach((atc) => {
      if (atc.callsign.includes(localStorage.getItem("plateform"))) {
        let onlineTime = new Online(atc.createdAt);
        document.getElementById("online").innerHTML = onlineTime.getOnline();
        console.log(atc.rating);
        let rating = new Rating();
        document.getElementById("grade").innerHTML = "<img src="+rating.getRating(4, "ATC", "img")+">";
        

        //affichage des données
        document.getElementById("callsign").innerHTML = atc.callsign;
        document.getElementById("atis_revision").innerHTML = atc.atis.revision;
        document.getElementById("atis_name_airport").innerHTML =
          atc.atis.lines[1];
        document.getElementById("atis_metar").innerHTML = atc.atis.lines[3];
        document.getElementById("atis_rwy").innerHTML = atc.atis.lines[4];
        document.getElementById("frequency").innerHTML =
          atc.atcSession.frequency;
        let userId = atc.userId;
      }
    });
  });

setInterval(() => {
  fetch(dataIvao)
    .then((response) => response.json()) // one extra step
    .then((data) => {
      //recherche de l'atc dans le tableau atcs
      data.clients.atcs.forEach((atc) => {
        if (atc.callsign.includes(localStorage.getItem("plateform"))) {
          //affichage des données
          let onlineTime = new Online(atc.createdAt);
          document.getElementById("online").innerHTML = onlineTime.getOnline();
          document.getElementById("atis_revision").innerHTML =
            atc.atis.revision;
          //document.getElementById("atis_name_airport").innerHTML = atc.atis.lines[1];
          document.getElementById("atis_metar").innerHTML = atc.atis.lines[3];
          document.getElementById("atis_rwy").innerHTML = atc.atis.lines[4];
          //document.getElementById("frequency").innerHTML = atc.atcSession.frequency;
          //let userId = atc.userId;
          //console.log(userId);
        }
      });
    });
}, 10000);

fetch(dataIvao)
  .then((response) => response.json()) // one extra step
  .then((data) => {
    data.clients.pilots.forEach((pilot) => {
      if (pilot.flightPlan.departureId == airport[0]) {
        //crée un array avec les vols avec plusieur ajout de 0 à la fin
        departureId.push(pilot.callsign);
        document.getElementById("depart_count").innerHTML = departureId.length;
      }
    });
  });

setInterval(() => {
  departureId = [];
  fetch(dataIvao)
    .then((response) => response.json()) // one extra step
    .then((data) => {
      data.clients.pilots.forEach((pilot) => {
        if (pilot.flightPlan.departureId == airport[0]) {
          //crée un array avec les vols avec plusieur ajout de 0 à la fin
          departureId.push(pilot.callsign);
          document.getElementById("depart_count").innerHTML =
            departureId.length;
        }
      });
    });
}, 10000);

fetch(dataIvao)
  .then((response) => response.json()) // one extra step
  .then((data) => {
    data.clients.pilots.forEach((pilot) => {
      if (pilot.flightPlan.arrivalId == airport[0]) {
        //crée un array avec les vols avec plusieur ajout de 0 à la fin
        arrivalId.push(pilot.callsign);
        document.getElementById("arrival_count").innerHTML = arrivalId.length;
      }
    });
  });

setInterval(() => {
  arrivalId = [];
  fetch(dataIvao)
    .then((response) => response.json()) // one extra step
    .then((data) => {
      data.clients.pilots.forEach((pilot) => {
        if (pilot.flightPlan.arrivalId == airport[0]) {
          //crée un array avec les vols avec plusieur ajout de 0 à la fin
          arrivalId.push(pilot.callsign);
          document.getElementById("arrival_count").innerHTML = arrivalId.length;
        }
      });
    });
}, 10000);

/** onclick chatvac function ajoue de URL dans la balise a */
document.getElementById("chartvac").addEventListener("click", function () {
  document.getElementById("chartvaclogiciel").href = chart(airport[0]);
});
