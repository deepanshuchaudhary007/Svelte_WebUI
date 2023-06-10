
$(document).ready(function(){   
    $(document).on('change', "#country_dropdown", function(e) {
        var country_id = $(this).val();
        var country_code = $(this).data('index-data');
        url = "/state/";
        ajaxDropDown(url, "State", country_id);
        html = `<option value="${country_id}" disabled>${country_code}</option>`
        $("#country_code").html(html);
    
    });
    $(document).on('change', "#state_dropdown", function(e) {
        var state_id = $(this).val();
        url = "/city/";
        ajaxDropDown(url, "City", state_id);
    
    });
    $(document).on('click', "#change_you_password", function(e) {
        $('#new_password_modal').modal('show');
    });
    
});


function ajaxDropDown(url, action_for, id) {
    $.ajax({  
        type: "GET",  
        url: url+id,  
        success: function (dataResult) { 
            data = JSON.parse(dataResult) 
            if ( action_for == 'State'){                 
                var state_option = '<option value="-1">----Select Your State----</option>';  
                for (var i = 0; i < data.length; i++) {  
                state_option += '<option value="' + data[i].id + '">' + data[i].state_name + '</option>';  
            }  
            $("#state_dropdown").html(state_option);    
            }else{
                var city_option = '<option value="-1">----Select Your City----</option>';  
                for (var i = 0; i < data.length; i++) {  
                city_option += '<option value="' + data[i].id + '">' + data[i].city_name + '</option>';  
            }  
            $("#city_dropdown").html(city_option);                
            }
              
        }  
    });    
    
}


