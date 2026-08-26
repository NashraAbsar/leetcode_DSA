class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # If the total number of '1's is less than k, no beautiful substring exists
        if s.count('1') < k:
            return ""
        
        ans = ""
        min_len = float('inf')
        left = 0
        ones_count = 0
        
        # Expand the window using the right pointer
        for right in range(len(s)):
            if s[right] == '1':
                ones_count += 1
                
            # Shrink the window from the left as long as it contains exactly k '1's
            while ones_count == k:
                # A valid beautiful substring must start and end with '1' to be minimal length
                if s[left] == '1':
                    current_len = right - left + 1
                    current_str = s[left:right + 1]
                    
                    # Update if we find a shorter length, or a lexicographically smaller string of the same length
                    if current_len < min_len:
                        min_len = current_len
                        ans = current_str
                    elif current_len == min_len:
                        if current_str < ans:
                            ans = current_str
                    
                    # Decrement count since we are about to move the left pointer past a '1'
                    ones_count -= 1
                
                left += 1
                
        return ans
