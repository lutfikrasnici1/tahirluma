function changeComponent(div) {
    if(div == "urunler"){
        document.getElementById("urunler").hidden = false;
        document.getElementById("girdiler").hidden = true;
        document.getElementById("ciktilar").hidden = true;
    }else if(div == "girdiler"){
        document.getElementById("urunler").hidden = true;
        document.getElementById("girdiler").hidden = false;
        document.getElementById("ciktilar").hidden = true;
    }else if(div == "ciktilar"){
        document.getElementById("urunler").hidden = true;
        document.getElementById("girdiler").hidden = true;
        document.getElementById("ciktilar").hidden = false;
    }
  }