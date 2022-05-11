document.getElementById('predict-btn').addEventListener("click", hideFormDiv);
document.getElementById('back-btn').addEventListener('click', hideResultDiv)

function hideFormDiv(){
   document.getElementById('form-div').classList.add('disp-none')
   document.getElementById('result-div').classList.remove('disp-none')
}

function hideResultDiv(){
    document.getElementById('result-div').classList.add('disp-none')
    document.getElementById('form-div').classList.remove('disp-none')
}

