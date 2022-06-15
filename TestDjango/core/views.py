from django.shortcuts import render

# Create your views here.
def indexV3(request):
    return render(request,'core/indexV3.html')


def CarroComprasV2(request):
    return render(request, 'core/CarroComprasV2.html')

def enviar(request):
    return render(request, 'core/enviar.html')


def FormularioV12(request):
    return render(request, 'core/FormularioV12.html')


def MicuentaV2(request):
    return render(request, 'core/MicuentaV2.html')


def MiPedidoV2(request):
    return render(request, 'core/MiPedidoV2.html')


def ProductosListar(request):
    return render(request, 'core/Productos Listar.html')


def SuscFundV2(request):
    return render(request, 'core/SuscFundV2.html')


def CatalogoCompleto(request):
    return render(request, 'core/CatalogoCompleto.html')


def compra(request):
    return render(request, 'core/compra.html')
