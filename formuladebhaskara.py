#LIB UTILIZADA

import math

#ADICIONAR VALORES
a = 10 
b = 20
c = 30

#PASSO A PASSO DAS CONTAS
resultadoparteum = ( -1 *  b )
resultadopartedois = int((b** 2-4*a*c))
resultadodaraiz= int(math.sqrt(-1 * resultadopartedois))
resultadodadivisao = ( 2 * a  )

#CALCULO FINAL
resultadofinal =  (- 1 * resultadoparteum - resultadodaraiz / resultadodadivisao )  

#CONDIÇÕES
if resultadofinal <= 0:
    print("Delta nao tem raiz real")
    print("Delta nao tem  uma raiz ")
else: 
    print("Delta tem duas raizes e o valor é: ", int(resultadofinal))
 

      


             
