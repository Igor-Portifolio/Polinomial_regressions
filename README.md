# Polinomial Regressions

## Português

Este projeto aborda a aplicação teórica do método dos mínimos
quadrados.

O arquivo `data.py` é responsável por gerar pontos aleatórios, entre 
0 e 100, que servirão como exemplo para a construção da função 
aproximadora.

No arquivo `Linear_alg_logic.py` estão as funções, como `coef`, 
que retornam os coeficientes que melhor aproximam a função 
com base nas entradas dos pontos x, y e no grau do polinômio. 
Também há a função que monta a função polinomial com base
nesses coeficientes.

O arquivo `Regressions.py` é o módulo principal, onde estão
as entradas do usuário: quantos pontos deseja gerar e 
qual grau do polinômio deseja para a aproximação. Além 
disso, ele importa os demais módulos e gera um gráfico 
ilustrativo.

<p align="center">
  <img src="images/image_10points_degree3.png" alt="Regressão polinomial: 10 pontos, grau 3" width="500">
  <br>
  <em>Figura 1: Exemplo de regressão com 10 pontos e grau 3</em>
</p>

---

## English

This project covers the theoretical application of the least
squares method.

The file `data.py` is responsible for generating random points, between 0 and 100,
that serve as examples for building the approximating 
function.

In the file `Linear_alg_logic.py`, there are functions such as 
`coef` that return the coefficients that best fit the function 
based on the inputs x, y points and the degree of the 
polynomial. There is also a function that constructs the 
polynomial function based on these coefficients.

The file `Regressions.py` is the main module, which contains 
the user inputs: how many points to generate and the degree 
of the polynomial for approximation. It also imports the other
modules and creates an illustrative graph.

<p align="center">
  <img src="images/image_10points_degree3.png" alt="Polynomial regression: 10 points, degree 3" width="500">
  <br>
  <em>Figure 1: Example of polynomial regression with 10 points and degree 3</em>
</p>
