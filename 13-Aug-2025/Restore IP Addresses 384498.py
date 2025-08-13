# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, parts):
            # If we already have 4 parts and used all characters
            if len(parts) == 4:
                if start == len(s):
                    res.append(".".join(parts))
                return

            # Try parts of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]
                
                # Skip if leading zero or > 255
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return res
