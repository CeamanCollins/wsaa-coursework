function getAllCustomers(callback){
    $.ajax(
        {
            "url" : "/customers",
            "method": "GET",
            "data": "",
            "dataType": "JSON",
            "success": function(result){
                callback(result)
            },
            "error": function(xhr,status,error){
                console.log("error: "+status+" message: "+error);
            }
        }
    );
}
function getCustomerById(id, callback){
    $.ajax(
        {
            "url" : "/customers/"+id,
            "method": "GET",
            "data": "",
            "dataType": "JSON",
            "success": function(result){
                callback(result)
            },
            "error": function(xhr,status,error){
                console.log("error: "+status+" message: "+error);
            }
        }
    );
}
function createCustomer(customer, callback){
    $.ajax(
        {
            "url" : "/customers/"+customer.id,
            "method": "POST",
            "data": JSON.stringify(customer),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8"
            "success": function(result){
                callback(result)
            },
            "error": function(xhr,status,error){
                console.log("error: "+status+" message: "+error);
            }
        }
    );
}
function updateCustomer(customer, callback){
    $.ajax(
        {
            "url" : "/customers/"+customer.id,
            "method": "PUT",
            "data": JSON.stringify(customer),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8"
            "success": function(result){
                callback(result)
            },
            "error": function(xhr,status,error){
                console.log("error: "+status+" message: "+error);
            }
        }
    );
}
function getAllPizzas(callback){
    $.ajax(
        {
            "url" : "/pizzas",
            "method": "GET",
            "data": "",
            "dataType": "JSON",
            "success": function(result){
                callback(result)
            },
            "error": function(xhr,status,error){
                console.log("error: "+status+" message: "+error);
            }
        }
    );
}




function processGetAll(result){
console.log("in process")
console.log(result)
}
getAll(processGetAll)
//getAll()
