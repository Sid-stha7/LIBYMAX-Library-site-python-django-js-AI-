//for modal pop up

function displaymodal(){
    document.getElementById("modal").style.display="block";
  }

  function closemodal(){
    document.getElementById("modal").style.display="none";
  }
  

  function gray(){
    document.getElementById("body-section").style.filter = "grayscale(100%)";
    document.getElementById("body-section").style.top = "-130px";


  }

  function invert(){
    document.getElementById("body-section").style.filter = "invert(100%)";
    document.getElementById("body-section").style.top = "-130px";

  }
  function bright(){
    document.getElementById("body-section").style.filter = "brightness(130%)";
    document.getElementById("body-section").style.overflowy = "initial";
    document.getElementById("body-section").style.top = "-130px";


  }

  function increasefont(){
    document.getElementById("body-section").style.fontSize = "x-large";
  }

  function decreasefont() {
    document.getElementById("body-section").style.fontSize = "x-small";
    
  }

  function normalfont() {
    document.getElementById("body-section").style.fontSize = "initial";
    
  }
  function undoinvert(){
    location.reload();
  }

  function Login() {
    location.replace("login.html")
  }

 

