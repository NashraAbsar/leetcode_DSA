from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        
        # Count total frequencies
        counts = Counter(s)
        odd_chars = [c for c, count in counts.items() if count % 2 == 1]
        
        # A palindrome can have at most one character with an odd frequency
        if len(odd_chars) > 1:
            return ""
        if n % 2 == 1 and len(odd_chars) != 1:
            return ""
        if n % 2 == 0 and len(odd_chars) != 0:
            return ""
            
        mid_char = odd_chars[0] if n % 2 == 1 else ""
        half_counts = {c: count // 2 for c, count in counts.items()}
        
        candidates = []
        
        # Case 1: The first half matches target's first half exactly
        target_half = target[:m]
        target_half_counts = Counter(target_half)
        
        possible = True
        for c, count in target_half_counts.items():
            if half_counts.get(c, 0) != count:
                possible = False
                break
        if n % 2 == 1 and target[m] != mid_char:
            possible = False
            
        if possible:
            p_same = target_half + mid_char + target_half[::-1]
            if p_same > target:
                candidates.append(p_same)
                
        # Case 2: Divergence happens at index i < m (in the first half)
        for i in range(m):
            pref = target[:i]
            pref_counts = Counter(pref)
            
            # Check if we can even match the prefix up to i-1
            if any(half_counts.get(c, 0) < count for c, count in pref_counts.items()):
                continue
                
            rem_counts = {c: half_counts.get(c, 0) - pref_counts.get(c, 0) for c in half_counts}
            
            # Try a character strictly greater than target[i] at position i
            for char in sorted(rem_counts.keys()):
                if char > target[i] and rem_counts[char] > 0:
                    cur_rem = rem_counts.copy()
                    cur_rem[char] -= 1
                    
                    # Fill the rest of the first half with the smallest available characters
                    rest = []
                    for c in sorted(cur_rem.keys()):
                        rest.extend([c] * cur_rem[c])
                    
                    first_half = pref + char + "".join(rest)
                    p = first_half + mid_char + first_half[::-1]
                    if p > target:
                        candidates.append(p)
                        
        # Case 3: First half matches target exactly, divergence happens at the middle element
        if n % 2 == 1:
            pref = target[:m]
            pref_counts = Counter(pref)
            if all(half_counts.get(c, 0) == count for c, count in pref_counts.items()):
                if mid_char > target[m]:
                    p = pref + mid_char + pref[::-1]
                    if p > target:
                        candidates.append(p)
                        
        return min(candidates) if candidates else ""
