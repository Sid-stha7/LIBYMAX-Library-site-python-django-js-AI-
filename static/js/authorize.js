  //for the popup slider(SignIN/SignUP overlay)
  const signUpButton = document.getElementById('signUp');
  const signInButton = document.getElementById('signIn');
  const container = document.getElementById('popup-container');
  
  signUpButton.addEventListener('click',() => container.classList.add('right-panel-active'));
  
  signInButton.addEventListener('click',() => container.classList.remove('right-panel-active'));
  
  //for displaying the popup 
  
  document.getElementById("button").addEventListener("click",function(){
      document.querySelector(".popup-container").style.display="flex";
      document.querySelector(".content").style.opacity="0.2";
      document.querySelector(".content").style.zIndex="-1";
  })

  //for authentication 

  const email = document.getElementById('email');
  const password = document.getElementById('pass');

  document.getElementById('login').addEventListener("click" , function(){
    if(
      document.getElementById("email") === "dummyemail@xyz.com" &&
    document.getElementById("pass")==="jobdeals123"
    ){
         location.replace("Profile.html")
    }else{
      alert("Invalid Email or Password.");
    }
  })


  //for modal pop up

function displaymodal(){
  document.getElementById("modal").style.display="block";
}

function closemodal(){
  document.getElementById("modal").style.display="none";
}


function gray(){
  document.getElementById("bodydisplay").style.filter = "grayscale(100%)";
  // document.getElementById("body-section").style.top = "-130px";


}

function invert(){
  document.getElementById("bodydisplay").style.filter = "invert(100%)";
  // document.getElementById("body-section").style.top = "-130px";

}
function bright(){
  document.getElementById("bodydisplay").style.filter = "brightness(130%)";
}

function increasefont(){
  document.getElementById("bodydisplay").style.fontSize = "x-large";
}

function decreasefont() {
  document.getElementById("bodydisplay").style.fontSize = "x-small";
  
}

function normalfont() {
  document.getElementById("bodydisplay").style.fontSize = "initial";
  
}
function undoinvert(){
  location.reload();
}

function Login() {
  location.replace("login.html")
}
