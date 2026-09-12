import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        # Pair each interval with its original index: (l, r, weight, original_index)
        A = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        
        # Sort primarily by start time
        A.sort(key=lambda x: x[0])
        
        n = len(A)
        starts = [x[0] for x in A]
        
        # dp[i][j] stores a tuple: (max_weight, list_of_sorted_indices)
        # i ranges from 0 to n, j ranges from 0 to 4
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        # Build the DP table bottom-up from right to left
        for i in range(n - 1, -1, -1):
            l, r, w, idx = A[i]
            # Binary search for the first interval that starts after this one ends
            next_i = bisect.bisect_right(starts, r)
            
            for j in range(1, 5):
                # Option 1: Skip the current interval
                skip_w, skip_res = dp[i + 1][j]
                
                # Option 2: Choose the current interval
                take_w_next, take_res_next = dp[next_i][j - 1]
                take_w = w + take_w_next
                take_res = sorted([idx] + take_res_next)
                
                # Compare both options
                if take_w > skip_w:
                    dp[i][j] = (take_w, take_res)
                elif skip_w > take_w:
                    dp[i][j] = (skip_w, skip_res)
                else:
                    # Weights are tied; pick the lexicographically smaller list
                    if take_res < skip_res:
                        dp[i][j] = (take_w, take_res)
                    else:
                        dp[i][j] = (skip_w, skip_res)
                        
        # The answer is the best subset of at most 4 intervals from index 0
        return dp[0][4][1]
