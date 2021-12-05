 //for modal pop up

 function displaymodal(){
    document.getElementById("modal").style.display="block";
  }

  function closemodal(){
    document.getElementById("modal").style.display="none";
  }
  

  function gray(){
    document.getElementById("display").style.filter="grayscale(100%)";

  }

  function invert(){
    document.getElementById("display").style.filter = "invert(100%)";

  }
  function bright(){
    document.getElementById("display").style.filter = "brightness(130%)";
    document.getElementById("display").style.overflowy = "initial";

  }

  function increasefont(){
    document.getElementById("display").style.fontSize = "x-large";
  }

  function decreasefont() {
    document.getElementById("display").style.fontSize = "x-small";
    
  }

  function normalfont() {
    document.getElementById("display").style.fontSize = "initial";
    
  }
  function undoinvert(){
    location.reload();
  }

  function Login() {
    location.replace("login.html")
  }
