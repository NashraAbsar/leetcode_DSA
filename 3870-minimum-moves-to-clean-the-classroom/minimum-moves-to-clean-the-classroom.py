
from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and assign an index to every L
        start = None
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)

        # No litter
        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        # best[r][c][mask] = maximum energy remaining
        # when we reach (r,c) having collected mask
        best = [
            [
                [-1] * (1 << k)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        sr, sc = start
        best[sr][sc][0] = energy

        # row, col, remaining energy, collected mask, moves
        q = deque()
        q.append((sr, sc, energy, 0, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == full_mask:
                return moves

            # With 0 energy, we cannot make another move.
            # We can only continue if we are ALREADY on R,
            # but reset happens when entering R, so normally
            # e will already have been restored there.
            if e == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = e - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                # Entering R immediately restores energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Already reached this state with more energy
                if best[nr][nc][new_mask] >= new_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1

