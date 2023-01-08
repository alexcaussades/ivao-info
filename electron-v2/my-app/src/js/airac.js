const airac_data = require("../../data/airac-dic.json");
const dateTime = new Date();

const month = dateTime.getMonth() + 1;
let day = dateTime.getDate();
const year = dateTime.getFullYear();

// crée une regex pour trouver le combien de chiffre sont present dans la date

day = day.toString().padStart(2, "0");

const airac_Year = airac_data[year];
const airac_Month = airac_Year[month];

function airac() {
  if (airac_Year) {
    if (airac_Month) {
      if (day >= airac_Month.day) {
        return (
          airac_Month.day + "_" + airac_Month.month + "_" + airac_Year[0].year
        );
      }
    }else{
      // Patch de secour logiciel pour le bug de l'airac fin 2022
      return airac_data[2022][13].day + "_" + airac_data[2022][13].month + "_" + airac_data[2022][0].year;
    }
  }
}



module.exports = { airac };
