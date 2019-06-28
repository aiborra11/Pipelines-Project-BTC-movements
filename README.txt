La idea de este proyecto es:
1. Importar un CSV en el que se muestre el precio del BTC/5mins.
2. Importar el order-book y el volumen a traves de una API de BitMex.
3. Agrupar las ordenes por tiempo (5mins) y compararlas con el volumen.
4. Si el orderbook muestra pocas operaciones pero rompe muchos niveles de soporte/resistncia == ha entrado un operador.
5. Si el orderbook muestra muchas operaciones y no consigue romper niveles de soporte/resistencia en un periodo corto de tiempo = compradores de a pie.

