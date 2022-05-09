$(document).ready(function() {
    alert('paso1')
    $.getJSON('http://127.0.0.1:8000/api/lista_contactos', function(data) {
        console.log(data)
        var Contacto = data;
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth() + 1; //January is 0!
        var yyyy = today.getFullYear();
        if (dd < 10) {
            dd = '0' + dd;
        }
        if (mm < 10) {
            mm = '0' + mm;
        }

        today = dd + '/' + mm + '/' + yyyy;

        $('#fecha').html(today);
        $('#id_contacto').html(Contacto.id_contacto);
        $('#nombre').html(Contacto.nombre);
        $('#correo').html(Contacto.correo);
    }).fail(function() {
        console.log('Error al consumir la API!');
    });

});