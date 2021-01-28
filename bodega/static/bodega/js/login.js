$(function () {
    $('#btnIngresar').on('click', function () {
        var username, contraseña;
        username = $("#username").val();
        contraseña = $("#contraseña").val();
        

        
        if(username == " "){
            alert("Ingrese un usuario valido por favor");
            return false;
    
        }
        else if(contraseña == ""){
            alert("El campo contraseña está vacio");
            return false;
                
        } 
        
        
        

        
        

    })
    
})
