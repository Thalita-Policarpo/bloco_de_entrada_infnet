Algoritmo "Comiss�o"
// Autor(a)    : Thalita Ferreira Policarpo Silva
// Data atual  : 09/03/2022

funcao calcularComissao():real
inicio
   retorne (vendas*15) / 100

fimfuncao

funcao calcularSalarioTotal():real
inicio
   retorne salarioFixo + calcularComissao()

fimfuncao

procedimento impressao();
var
   salarioTotal:real
inicio
   salarioTotal <- calcularSalarioTotal()
   escreval("O(a) vendedor(a) ",nome, " tem o sal�rio fixo de R$",salarioFixo,". Com a comiss�o da venda, receber� R$:",salarioTotal)
fimprocedimento

Var
   // Se��o de Declara��es das vari�veis
   nome: caracter

   salarioFixo: real
   vendas: real
   comissao: real

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...

   escreval("nome do Vendedor: ")
   leia(nome)
   escreval("Sal�rio fixo: ")
   leia(salarioFixo)
   escreval("Valor das vendas: ")
   leia(vendas)


   impressao()


   //ler nome do vendedor
   //ler Sal�rio fixo
   //ler total de vendas efetuadas em dinheiro

   //vendedor ganha 15% de comiss�o sobre suas vendas efetuadas

   //Informar seu nome
   //Informar Sal�rio fixo
   //Informar Sal�rio + comiss�o

Fimalgoritmo