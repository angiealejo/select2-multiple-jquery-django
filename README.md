# select2-multiple-jquery-django
Ejemplo del uso de plugin select2 de jquery con Django y API Django Rest Framework.

1. El formulario html se renderiza con template-tags de Django
2. Se utiliza un modelform con el modelo "Articulo"
3. Para crear el campo de almacenes en el formulario html unicamente se agrega una etiqueta select con el id "id_almacenes" para poder acceder al componente desde jquery
4. Se puede crear un form adicional para el campo almacen y renderizarlo en el template del formulario pero no lo creí necesario para este caso en específico.
