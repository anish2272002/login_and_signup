const form_label=document.querySelectorAll("label")
const form_input=document.querySelectorAll("input")

form_label.forEach((elem)=>{elem.classList.add('form-label')})
form_input.forEach((elem)=>{elem.classList.add('form-control')})

function progress(){
    let length=0;
    const interval=setInterval(()=>{
        length=length+10;
        if(length>100){
            clearInterval(interval);
        }else{
            document.querySelector(".progress-bar").style.width=length+'%';
        }
    },50)
}
const progress_eles=document.querySelectorAll("#progress-init")
progress_eles.forEach((elem)=>{elem.addEventListener("click",progress)});