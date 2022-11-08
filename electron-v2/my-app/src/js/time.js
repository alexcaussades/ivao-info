const { shell, ipcRenderer } = require("electron");
const { Notification } = require("electron");
const os = require("os");
//const path = require("path");
const fs = require("fs");
const { airac } = require("../js/airac.js");
const package = require("../../package.json");

//recupere le non de la machine

//recupere le chemin du fichier
const dir = os.homedir();
//chemain du fichier a creer appdata est un dossier caché
const path = dir + "\\AppData\\Roaming\\info-ivao";
const pathLogs = path + "\\logs";
const pathFriends = path + "\\friends";
const pathPrefences = path + "\\preferences";
//verification si le dossier existe
if (!fs.existsSync(path)) {
  //creation du dossier
  fs.mkdirSync(path);
}

if (!fs.existsSync(pathLogs)) {
  //creation du fichier
  fs.mkdirSync(pathLogs);
  fs.appendFile(
    pathLogs + "\\log.txt",
    "Création du fichier log " + new Date() + "\r\n",
    function (err) {
      if (err) throw err;
      console.log("Saved!");
    }
  );
}

if (!fs.existsSync(pathFriends)) {
  //creation du fichier
  fs.mkdirSync(pathFriends);
  fs.appendFile(
    pathLogs + "\\log.txt",
    "Création du dossier friends " + new Date() + "\r\n",
    function (err) {
      if (err) throw err;
      console.log("Saved!");
    }
  );
}

if (!fs.existsSync(pathPrefences)) {
  //creation du fichier
  fs.mkdirSync(pathPrefences);
  fs.appendFile(
    pathLogs + "\\log.txt",
    "Création du dossier préfrences " + new Date() + "\r\n",
    function (err) {
      if (err) throw err;
      console.log("Saved!");
    }
  );
}

//ecriture dans le fichier
const ecriture = "ouverture de l'application | " + new Date() + "\r\n";
fs.appendFile(pathLogs + "\\log.txt", ecriture, function (err) {
  if (err) throw err;
  console.log("Saved!");
});
const fileCreatetrue =
  "✅ Les fichiers ont été créés avec succès ! \r\n Version:  " +
  package.version +
  " " +
  package.versionName +
  "\r\n";
document.getElementById("files").innerHTML = fileCreatetrue;

document.getElementById("result").innerHTML =
  " AIRAC: <strong>" + airac() + "</strong>";
document.getElementById("profil").innerHTML =
  " Profil: <strong>Aucun </strong>";
//function qui permet d'ouvrir le dossier des logs
function openFolder() {
  shell.openPath(pathLogs);
}

function openFeeadback() {
  shell.openExternal(package.bugs.url);
}

function openGithub() {
  shell.openExternal(package.repository.url);
}

function openIvao() {
  shell.openExternal("https://www.ivao.aero");
}
