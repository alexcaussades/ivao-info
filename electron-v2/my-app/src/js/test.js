const { shell, ipcRenderer } = require("electron");
const { Notification } = require("electron");
const {compareVid, getVid } = require("../js/friends.js");
const os = require("os");
const fs = require("fs");
const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";

const imgbtn =
  "https://api.iconify.design/ic:baseline-cell-tower.svg?color=%23ffffff";
// search atc callsign du formulaire de recherche la test.html

/** création du systeme d'enregistrement de donnée de electron en variable */
//localStorage.removeItem("plateform");
console.log(localStorage.getItem("plateform"));
const dir = os.homedir();
//chemain du fichier a creer appdata est un dossier caché
const path = dir + "\\AppData\\Roaming\\info-ivao";
const pathLogs = path + "\\logs";
const pathFriends = path + "\\friends";
const pathPrefences = path + "\\preferences";

//recupere les preferences
const preferences = fs.readFileSync(pathPrefences + "\\preferences.json");
const preferencesJson = JSON.parse(preferences);

//recupere les amis
// const friends
// = fs.readFileSync
// (pathFriends + "\\friends.json");
// const friendsJson = JSON.parse(friends);

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("tableauAtc").hidden = true;
});

if (preferencesJson.active == true) {
  document.getElementById("warning-pfofile").hidden = true;
  document.getElementById("met").disabled = false;
  document.getElementById("friend").disabled = false;
  document.getElementById("pref_plateforme").disabled = false;
  document.getElementById("pref_plateforme").innerHTML =
    preferencesJson.preference_platform;
  document.getElementById("online").disabled = false;
} else {
  document.getElementById("warning-pfofile").hidden = false;
}
getVid();
compareVid();

document.addEventListener("submit", function () {
  let value = document.getElementById("search-atc").value;
  value = value.toUpperCase();
  fetch(dataIvao)
    .then((response) => response.json()) // one extra step
    .then((data) => {
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
            ).innerHTML += `<tr><td>${element.callsign}</td><td>${element.atcSession.frequency} MHz</td><td><button class="btn btn-primary" id="plateform" value="${element.callsign}">More Information</button></td></tr>`;
          });
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

/** preference plateform */
document.getElementById("pref_plateforme").innerHTML = (preferencesJson.preference_platform ? preferencesJson.preference_platform : "IVAO");

document.getElementById("vid").value = preferencesJson.vid;
document.getElementById("preference").value =
  preferencesJson.preference_platform;
document.getElementById("code_dev").value = preferencesJson.code_dev;
document.getElementById("token_metar").value = preferencesJson.token_metar;

document.addEventListener("submit", () => {
  let vid = document.getElementById("vid").value;
  let prefrence_platform = document.getElementById("preference").value;
  let code_dev = document.getElementById("code_dev").value;
  let token_metar = document.getElementById("token_metar").value;
  /** creation du fichier au format json des preferency  */
  const data = {
    vid: vid,
    preference_platform: prefrence_platform,
    code_dev: code_dev,
    token_metar: token_metar,
    active: true,
  };
  const dataJson = JSON.stringify(data);
  /** verifier si les valeur du vid exixte */
  if (vid == "") {
    console.log("vide");
  } else {
    fs.writeFile(pathPrefences + "\\preferences.json", dataJson, (err) => {
      if (err) throw err;
      console.log("Data written to file");
    });
  }
});

document.addEventListener("keyup", function (e) {
  if (e.target && e.target.id == "icao") {
    /** creation de la variable pour stocker les données de l'input */
    document.getElementById("returnMetar").hidden = true;
    let icao = document.getElementById("icao").value;
    icao = icao.toUpperCase();
    /** regex qui compte le nombre lettre */
    let regex = /[A-Z]/g;
    let count = icao.match(regex).length;

    if (count == 4) {
      let srmetar = icao;
      /** fetch avec auth  */
      fetch("https://avwx.rest/api/metar/" + srmetar, {
        headers: {
          Authorization: "Token " + preferencesJson.token_metar,
        },
      })
        .then((response) => response.json()) // one extra step
        .then((data) => {
          document.getElementById("returnMetar").hidden = false;
          document.getElementById("returnMetar").innerHTML = data.raw;
        });
    }
  }
});

setInterval(function () {
  fetch(dataIvao)
    .then((response) => response.json())
    .then((data) => {
      data.clients.atcs.forEach((atc) => {
        if (atc.userId == preferencesJson.vid) {
          document.getElementById("online").classList.remove("btn-dark");
          document.getElementById("online").classList.add("btn-success");
          document.getElementById("online").innerHTML = "Online";
        }
      });
    });
}, 10000);

setInterval(function () {
  fetch(dataIvao)
    .then((response) => response.json())
    .then((data) => {
      data.clients.pilots.forEach((atc) => {
        if (atc.userId == preferencesJson.vid) {
          document.getElementById("online").classList.remove("btn-dark");
          document.getElementById("online").classList.add("btn-success");
          document.getElementById("online").innerHTML = "Online";
        }
      });
    });
}, 10000);


setInterval(function () {
  fetch(dataIvao)
    .then((response) => response.json())
    .then((data) => {
      data.clients.atcs.forEach((atc) => {
        if (atc.callsign.includes(preferencesJson.preference_platform)) {
          document.getElementById("pref_plateforme").classList.remove("btn-secondary");
          document.getElementById("pref_plateforme").classList.add("btn-success");
          document.getElementById("pref_plateforme").onclick = function () {
            localStorage.setItem("plateform", preferencesJson.preference_platform);
            window.location.href = "plateform.html";
          };
          document.getElementById("pref_plateforme").innerHTML = preferencesJson.preference_platform;
        }
      });
    });
}, 10000);
