Algoritmo "Comissão"
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
   escreval("O(a) vendedor(a) ",nome, " tem o salário fixo de R$",salarioFixo,". Com a comissão da venda, receberá R$:",salarioTotal)
fimprocedimento

Var
   // Seção de Declarações das variáveis
   nome: caracter

   salarioFixo: real
   vendas: real
   comissao: real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...

   escreval("nome do Vendedor: ")
   leia(nome)
   escreval("Salário fixo: ")
   leia(salarioFixo)
   escreval("Valor das vendas: ")
   leia(vendas)


   impressao()


   //ler nome do vendedor
   //ler Salário fixo
   //ler total de vendas efetuadas em dinheiro

   //vendedor ganha 15% de comissão sobre suas vendas efetuadas

   //Informar seu nome
   //Informar Salário fixo
   //Informar Salário + comissão

Fimalgoritmo