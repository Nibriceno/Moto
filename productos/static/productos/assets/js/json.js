function traer(){
    $.ajax({
    type: "GET" ,
    url:"https://randomuser.me/api/" ,
    success:function(data){
  
    var res;
    for (let item of  data.results){
    
    res +="<tr><td>"+item.name.title+"</td><td>"+item.name
    .first+"</td><td>"+item.location.street.name+" "+
    item.location.street.number+"</td><td><img src='"+
    item.picture.medium+"'/></td></tr>";
    }
   
    $("#cuerpoTable").empty(res);

    
    $("#cuerpoTable").append(res);
    
    },Error:function(e){
        alert("No se pudo realizar");
    }
    
    });
    return false;
    alert("acabo la funcion");
}