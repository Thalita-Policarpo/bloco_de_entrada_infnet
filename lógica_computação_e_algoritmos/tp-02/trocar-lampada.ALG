Algoritmo "Trocar l�mpada"
// Autor(a)    : Thalita Ferreira Policarpo Silva
// Data atual  : 09/03/2022

funcao trocarLampada(): caracter
inicio
  escreval("A lampada funciona? ")
  leia(testeLampada)

   se testeLampada = "sim" entao
      retorne "Aproveite o ambiente Iluminado!"
   senao
      escreval("Tem outra lampada? ")
      leia(lampadaNova)

      se lampadaNova = "n�o" entao
         retorne "busque uma lampada nova!"
      senao
         escreval("Tem uma escada? ")
         leia(temEscada)

         se temEscada = "n�o" entao
            retorne "Pegue uma escada emprestada!"
         senao
            escreval("Buscou a escada? ")
            leia(buscarEscada)

            se buscarEscada = "n�o" entao
               retorne "busque uma escada!"
            senao
               escreval("Posicionou a escada em baixo da lampada queimada? ")
               leia(posicaoEscada)

               se posicaoEscada = "n�o" entao
                  retorne "Posicione a escada!"
               senao
                  escreval("Subiu a escada com a lampada nova na m�o? ")
                  leia(subirEscada)

                  se subirEscada = "n�o" entao
                     retorne "Suba a escada com a lampada nova na m�o!"
                  senao
                     escreval("Retirou a lampada queiamada? ")
                     leia(retirarLampada)

                     se retirarLampada = "n�o" entao
                        retorne "Retire a lampada queimada!"
                     senao
                        escreval("Colocou a lampada nova? ")
                        leia(colocarLampada)

                        se colocarLampada = "n�o" entao
                           retorne "Coloque a lammpada nova!"
                        senao
                           escreval("Desceu da escada com a lampada queimada? ")
                           leia(descerEscada)

                           se descerEscada = "n�o" entao
                              retorne "Des�a da escada com a lampada queimada!"
                           senao
                              escreval("Ligou o interruptor para testar a nova lampada? ")
                              leia(ligarLampada)

                              se ligarLampada = "n�o" entao
                                 retorne "Ligue o interruptor para testar a nova lampada!"
                              senao
                                 escreval("A lampada funciona? ")
                                 leia(testeLampadaNova)

                                 se testeLampadaNova = "Sim" entao
                                    retorne "Aproveite o ambiente Iluminado!"
                                 senao
                                    escreval(trocarLampada())
                                 fimse
                              fimse
                           fimse
                        fimse
                     fimse
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse
fimfuncao

procedimento impressao()
var
   resultado: caracter
inicio

   resultado <- trocarLampada()
   escreval(resultado)
fimprocedimento

Var
   // Seção de Declarações das variáveis

   testeLampada    :caracter
   testeLampadaNova:caracter
   lampadaNova     :caracter
   temEscada       :caracter
   buscarEscada    :caracter
   posicaoEscada   :caracter
   subirEscada     :caracter
   retirarLampada  :caracter
   colocarLampada  :caracter
   descerEscada    :caracter
   ligarLampada    :caracter


Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   impressao()

   // perguntar se a lampada funciona
   // perguntar se tem outra lampada
   // perguntar se tem escada
   // perguntar se buscou a escada
   // perguntar se posicionou a escada em baixo da lampada queimada
   // perguntar se subiu a escada com a lampada nova na m�o
   // perguntar se retirou a lampada queiamada
   // perguntar se colocou a lampada nova
   // perguntar se desceu da escada com a lampada queimada
   // perguntar se ligou o interruptor para testar a nova lampada
   // perguntar se a lampada funciona



Fimalgoritmo


