/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_almacenes = window.location.origin + "/api/almacenes/"

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    formulario = new TargetaFormulario()
})

/*-----------------------------------------------*\
            OBJETO: Targeta Formulario
\*-----------------------------------------------*/
function TargetaFormulario(){

	this.$almacenes = $('#id_almacenes')
	this.init()

}

TargetaFormulario.prototype.init = function () {
	var csrftoken = $("[name=csrfmiddlewaretoken]").val()
    this.$almacenes.select2(
    	{ 
    		language: "es",
    		//minimumInputLength: 1,
		}
	)

	 $.ajax(
		{
		 	url: url_almacenes,
	        headers: { "X-CSRFToken": csrftoken },
	        data: function (params) {
			      return {
			        id: params.id, // search term
			        clave: params.clave,
			        descripcion: params.descripcion

			      }
			    },
	        dataType:"json",
	        type:"GET"
	    }
    ).done(function(data)
	    {
	        $.each(data, function(index, item) 
		        {
		            $("#id_almacenes").append($('<option>').attr('value',item.pk).text(item.clave+"–"+item.descripcion))
		        }
	        )
	                
	    }
    )
    

}