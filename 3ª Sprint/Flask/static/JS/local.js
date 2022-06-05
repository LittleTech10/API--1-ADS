// JavaScript code
function pesquise_local() {
    let input = document.getElementById('navegar').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('col-4 mt-2');
      
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="";         
        }
    }
}

