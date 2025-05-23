# Fictitious Learning Algorithm

Fictitious learning algorithm is a Nash Equilibrium algorithm for bimatrix games. It's one of the earliest algorithms in the field for defining such games outcome, first published in 1951 and unpublished published in 1949. The game is cornerstone in Game theory and modern Computer Science and in-this, I am going to softly explain it. 


## Defining the algorithm

There are two players who either alternate or provide their hands simultaneously in a finite outcome game and it reaches a state despite basing strategy on past hands probability distribution that the game reaches Nash equilibrium. 

Many Computer Science branch from poker model development to GANs have resorted to Fictitious learning to solve their problem. In recent moments, its been explored under the pretext of RL (Reinforcement learning). 


## What are the deviations from original learning rule?

It is one trickled in algorithm history. Fictitious learning have two subclass:

1. Alternate Theory of players strategy  
2. Simultaneously played strategy

Among both, second is most popular and most cases it seems to be only existing which is defiantly false as Brown in 1951 and even in RAND report of 1949 proposed Alternate theory and it does have merit despite there have been proof both been similar and latter to be easily understandable. But, for a very minute class of nondegenerate ordinal potential games, theory 1, hold importance. It is considered an open problem in the field. 


## Code implementation

I have written a okaywish code to explain both SFP and AFP. There can be errors as I am not an expert in the field of Game theory and I am learning. Both of the code can be run. 


## Papers and learning resources

1. Explained Fictitious learning with Lemma: https://econwpa.ub.uni-muenchen.de/econ-wp/game/papers/0503/0503008.pdf  
2. Stanford's note on this subject: https://web.stanford.edu/~rjohari/teaching/notes/336_lecture6_2007.pdf  

---

## Next plan

I will add the gambling part of this learning rule. 
