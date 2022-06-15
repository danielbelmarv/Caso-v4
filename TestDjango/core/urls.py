from django.urls import path
from.views import *


urlpatterns =[
        path('', indexV3, name="index"),
        path('CarroComprasV2/',CarroComprasV2 , name="CarroComprasV2"),
        path('enviar/', enviar, name="enviar"),
        path('FormularioV12/', FormularioV12, name="FormularioV12"),
        path('MicuentaV2/', MicuentaV2, name="MicuentaV2"),
        path('MiPedidoV2/', MiPedidoV2, name="MiPeidoV2"),
        path('SuscFundV2/', SuscFundV2, name="SuscFundV2"),
        path('Catalogocompleto/',Catalogocompleto,name="CatalogoCompleto"),
        path('compra/', compra, name="compra")
]