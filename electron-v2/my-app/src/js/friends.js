const { v4: uuidv4 } = require("uuid");
const fs = require("fs");
const os = require("os");
//console.log(uuidv4());

const dataIvao = "https://api.ivao.aero/v2/tracker/whazzup";

const dir = os.homedir();
//chemain du fichier a creer appdata est un dossier caché
const path = dir + "\\AppData\\Roaming\\info-ivao";
const pathLogs = path + "\\logs";
const pathFriends = path + "\\friends";
const pathPrefences = path + "\\preferences";
let vid = [];
let vidreturn = [];
let online_friends_atc = [];
let online_friends_pilots = [];

let friends = [];

function getVid() {
  /** recherce dans le dossier friens les fichiers */
  fs.readdir(pathFriends, (err, files) => {
    files.forEach((file) => {
      /** lecture du fichier  dans le dossier*/
      const friends = fs.readFileSync(pathFriends + "\\" + file);
      const friendsJson = JSON.parse(friends);
      /** recherche dans le fichier json les données */
      vid.push(friendsJson.vid);
      vidreturn = vid;
      /** crée un retour en json  */
      const vidreturnJson = JSON.stringify(vidreturn);
      /** ecriture du fichier json */
      fs.writeFileSync(pathFriends + "\\vid.json", vidreturnJson);
    });
  });
}

/** comparer les elemnents du fichier vid.json avec celle de IVAO */
function compareVid() {
  online_friends_atc = [];
  online_friends_pilots = [];
  const vid = fs.readFileSync(pathFriends + "\\vid.json");
  const vidJson = JSON.parse(vid);
  fetch(dataIvao)
    .then((response) => response.json()) // one extra step
    .then((data) => {
      //rechercher les données dans le tableau atcs
      data.clients.atcs.forEach((atc) => {
        vidJson.forEach((vid) => {
          if (atc.userId == vid) {
            online_friends_atc.push(atc.callsign);
            //console.log(atc.callsign);
            friends.push(online_friends_atc);
          }
        });
      });
      data.clients.pilots.forEach((pilots) => {
        vidJson.forEach((vid) => {
          if (pilots.userId == vid) {
            online_friends_pilots.push(pilots.callsign);
            //console.log(pilots.callsign);
            friends.push(online_friends_pilots);
          }
        });
      });
      document.getElementById("friends_online").innerHTML = friends.length;
      
    });
}

module.exports = {
  getVid,
  compareVid,
};

//compareVid();