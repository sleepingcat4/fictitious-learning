import numpy as np
import numpy.typing as npt
from typing import Generator, Optional, Any 

def get_best_response_to_play_count(A: npt.NDArray, play_count: npt.NDArray) -> int:
    utilities = A @ play_count
    return np.random.choice(np.argwhere(utilities == np.max(utilities)).T[0])

def update_play_count(play_count: npt.NDArray, play: int) -> npt.NDArray:
    extra_play = np.zeros(play_count.shape)
    extra_play[play] = 1
    return play_count + extra_play

def fictitious_play(
    A: npt.NDArray, B: npt.NDArray, iterations: int, play_counts: Optional[Any] = None 
) -> Generator:
    if play_counts is None: 
        play_counts = [np.array([0 for _ in range(dimension)]) for dimension in A.shape]
        
    yield play_counts
    
    for repetition in range(iterations):
        plays = [
            get_best_response_to_play_count(matrix, play_count)
            for matrix, play_count in zip((A, B.T), play_counts[::-1])
        ]
        
        play_counts = [
            update_play_count(play_count, play)
            for play_count, play in zip(play_counts, plays)
        ]
        yield play_counts


A = np.array([[1, -1],
              [-1, 1]])

B = -A

fp = fictitious_play(A, B, iterations=10)

for step, play_counts in enumerate(fp):
    print(f"Step {step}: Player 1 - {play_counts[0]}, Player 2 - {play_counts[1]}")