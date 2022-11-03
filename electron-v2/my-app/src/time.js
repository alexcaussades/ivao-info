const { shell, ipcRenderer } = require("electron");
const { Notification } = require("electron");
const os = require("os");
//const path = require("path");
const fs = require("fs");

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
const fileCreatetrue = "✅ Les fichiers ont été créés avec succès ! \r\n Version:  1.0.0";
document.getElementById("files").innerHTML = fileCreatetrue;

//function qui permet d'ouvrir le dossier des logs
function openFolder() {
  shell.openPath(pathLogs);
}
