$(document).ready(function () {
    BindVehiculos();
});

$('#btnSubmit').click(function () {

    let patenteValue = $('#txtPatente').val();
    let marcaName = $('#txtMarca').val();
    let modeloName = $('#txtModelo').val();
    let categoriaValue = $('#txtCategoria').val();

    $.ajax({
        type: 'POST',
        dataType: 'json',
        data: {
            "patente": patenteValue,
            "marca": marcaName,
            "modelo": modeloName,
            "categoria": categoriaValue
        },

        url: "http://127.0.0.1:8000/api/Vehiculo/",
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            alert(err_msg);
        },
        success: function (result) {
         
            BindVehiculos();
            alert('Se guardo correctamente.');

            $('#txtPatente').val("");
            $('#txtMarca').val("");
            $('#txtLastModelo').val("");
            $('#txtCategoria').val("");
        }
    });
});

function BindVehiculos() {
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: "http://127.0.0.1:8000/api/Vehiculo/", success: function (result) {
           
            var totalCount = result.length;
            var structureDiv = "";
            
            for (let i = 0; i < totalCount; i++) {
                structureDiv += "<tr>" +
                    "     <td>" + result[i].patente + "</td>" +
                    "      <td>" + result[i].marca + "</td>" +
                    "             <td>" + result[i].modelo + "</td>" +
                    "              <td>" + result[i].categoria + "</td>" +
                    "              <td><button class='btn btn-link' onclick='return confirm(\"¿estas seguro que quieres eliminar el vehiculo de la lista?\",DeleteRow(" +result[i].patente+ "))'>Eliminar</button></td>" + 
                    "              <td><button class='btn btn-link' onclick='return confirm(\"¿estas seguro que quieres modificar?\",ModifyRow(" +result[i].patenteValue+ "))'>Modificar</button></td>" +   
                    "           </tr>";
            }

            $("#divBody").html(structureDiv);
      
        }
    });

}

function DeleteRow(patente) {
    
    $.ajax({
        type: 'DELETE',
        dataType: 'json',

        url: "http://127.0.0.1:8000/api/Vehiculo/"+patente+"/",
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            alert(err_msg);
        },
        success: function (result) {
      
            BindVehiculos();
        }
    });
}

function ModifyRow(patente) {
    
    $.ajax({
        type: 'PUT',
        dataType: 'json',

        url: "http://127.0.0.1:8000/api/Vehiculo/"+patente+"/",
        error: function (xhr, status, error) {

            var err_msg = ''
            for (var prop in xhr.responseJSON) {
                err_msg += prop + ': ' + xhr.responseJSON[prop] + '\n';
            }

            alert(err_msg);
        },
        success: function (result) {
      
            ModVehiculo();
        }
    });
}
