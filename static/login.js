function verificaDados(){
    matricula = document.getElementsByName("txt_login")[0].value
    senha = document.getElementsByName("senha_login")[0].value
    if(matricula === "" || senha === "") {
        alert("Por favor preencha seus dados!");
        return false;
    }
    return true;
}