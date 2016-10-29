Title: Zero knowledge proofs
Date: 2016-10-29 10:00
Tags: cryptography, zero-knowledge, snarks
Category: Programming articles

Zero knowledge proofs are a powerful cryptographical concept, but they might be complex and hard to grasp at first. Let's start exploring the subject with a simple example, which I first read [here](http://mathoverflow.net/a/22628).

## A classic example

Imagine you are playing snooker with your color-blind friend and you want to prove to him that red and green billard balls are distinguishable to you. Since you get more points for sinking the green ball then the red ones, and you want to win with your friend (evil!), you don't want to reveal which ball is which; you just want to prove that the balls are differently-colored.

The proof would go as follows: you give both balls to your friend, so that he is holding each in one hand. You can see in which hand he holds each of the balls, but you don't tell him which is which. Next, you ask the friend to put his both hands behind his back, and either switch the balls exactly once, or leave them be. When the friend shows you his hands again, you have to "guess" if he switched the balls or not. Notice that you don't reveal which ball is which- you just have to say whether he switched the balls or not.

If the balls are identical, you have 1/2 chance to guess correctly what action was performed. Since you can just look at the colors, you can easily judge whether or not he switched them. Now this means that your friend is 1/2 certain that you are not lying (he remembers whether he switched the balls or not). To convince him further, you just have to repeat this "proof" multiple times in the row. If you repeat the proof *t* times, the probability that you successfully keep deceiving your friend drops significantly, to *(1/2)^t*. After 10 proofs, there is only *0.0009765625%* chance that you guessed correctly if the balls are identical.

This proof is **zero knowledge**: you never reveal which ball is which, and your friend never learns how to distinguish the balls. This proof is also **interactive**: you repeat this procedure multiple times to raise the probability of truthfulness.

What would be an analogical non-zero-knowledge proof? You can place different labels on both balls. Your friend would show you either of the balls concealing the label and ask you which label it must have. Again, if the process is repeated, your friend gains confidence that there is a difference other than the labels in the balls which he can't percieve.

## A more complex (and more mathematical) example

In this example, let's consider the problem of graph isomorphism. We are given two graphs *G1* and *G2* and want to check if they are the same after "disentangling" the edges. Mathematically, let's assume that a graph *G* has *n* vertices and a list of edges, where each edge *(u, v)* is defined by a pair of vertice indexes. Graphs *G1* and *G2* are isomorphic if there exists a permutation *P* of numbers *{1, 2, .., n}* such that for each edge *(u, v)* from *G1* there exists an edge *(P(u), P(v))* in *G2*. We don't know a polynomial time algorithm that [solves this problem](https://en.wikipedia.org/wiki/Graph_isomorphism_problem).

* To be continued ... *
