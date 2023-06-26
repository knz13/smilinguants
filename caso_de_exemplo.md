
* As classes de Comida, Parede e Formiga derivam de classe ObjetoSimulado


* Tela de simulação

    * Contém os dados da simulação atual

    * Tem registro do mapa

    * A cada loop, renderiza tudo no mapa e atualiza tudo que está no mapa

* Mapa

    * Possui função Update que atualiza tudo que está no mapa

    * Durante o update, cada elemento pode mudar de lugar (atualiza o mapa)

* ObjetoSimulado

    * Se atualizar (função que recebe o mapa atual)

    * Pode colidir com outro ObjetoSimulado (os dois recebem o evento -> Função que passa o objeto que colidiu)

