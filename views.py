# ----------------- API ALMACENES ----------------- #


class AlmacenAPI(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('clave', 'descripcion',)


# ----------------- ARTICULOS ----------------- #


class ArticuloCreateView(View):
    def __init__(self):
        self.template_name = 'articulo/formulario.html'

    def get(self, request):
        formulario = ArticuloForm()
        contexto = {
            'form': formulario,
            'operation': "Nuevo"
        }
        return render(request, self.template_name, contexto)

    @transaction.atomic
    def post(self, request):

        formulario = ArticuloForm(request.POST)
        almacenes = request.POST.getlist('almacenes')
        punto_transaccion = transaction.savepoint()
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            articulo = Articulo()
            articulo.clave = datos_formulario.get('clave')
            articulo.descripcion = datos_formulario.get('descripcion')
            articulo.tipo = datos_formulario.get('tipo')
            articulo.udm = datos_formulario.get('udm')
            articulo.clave_jde = datos_formulario.get('clave_jde')
            articulo.save()

            for almacen in almacenes:
                obj_almacen = Almacen.objects.get(id=almacen)
                Stock.objects.create(articulo=articulo, almacen=obj_almacen)

            if punto_transaccion:
                transaction.savepoint_commit(punto_transaccion)
            else:
                transaction.savepoint_rollback(punto_transaccion)

            return redirect(
                reverse('inventarios.articulos_lista')
            )
        contexto = {
            'form': formulario,
        }

        return render(request, self.template_name, contexto)