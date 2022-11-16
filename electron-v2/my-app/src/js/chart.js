const {airac} = require("./airac.js");




function chart(value) {
    const url = "https://www.sia.aviation-civile.gouv.fr/dvd/eAIP_"+airac()+"/Atlas-VAC/PDF_AIPparSSection/VAC/AD/AD-2."+value+".pdf";
    return url;
}


module.exports = {chart};