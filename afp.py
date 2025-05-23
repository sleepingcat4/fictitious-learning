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

def alternating_fictitious_play(
    A: npt.NDArray, B: npt.NDArray, iterations: int, play_counts: Optional[Any] = None
) -> Generator:
    if play_counts is None:
        play_counts = [np.zeros(d) for d in A.shape]

    yield play_counts

    for iteration in range(iterations):
        player_to_update = iteration % 2

        if player_to_update == 0:
            play = get_best_response_to_play_count(A, play_counts[1])
            play_counts[0] = update_play_count(play_counts[0], play)
        else:
            play = get_best_response_to_play_count(B.T, play_counts[0])
            play_counts[1] = update_play_count(play_counts[1], play)

        yield play_counts


A = np.array([[1, -1],
              [0, 2]])

B = -A

fp = alternating_fictitious_play(A, B, iterations=10)

for step, play_counts in enumerate(fp):
    print(f"Step {step}: Player 1 - {play_counts[0]}, Player 2 - {play_counts[1]}")
