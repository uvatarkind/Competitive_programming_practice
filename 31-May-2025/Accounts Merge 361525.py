# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        rank = [0] * len(accounts)

        def find(n1):
            ans = parent[n1]
            while ans != parent[ans]:
                parent[ans] = parent[parent[ans]]  # path compression
                ans = parent[ans]
            return ans
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                parent[p1] = p2
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p2] = p1
                rank[p1] += 1
            return 1

        # Step 1: map email to account and union account
        email_to_account = {}
        for accountId, accountData in enumerate(accounts):
            for i in range(1, len(accountData)):
                email = accountData[i]
                if email in email_to_account:
                    union(accountId, email_to_account[email])
                else:
                    email_to_account[email] = accountId

        # Step 2: group by main account
        group_by_account = defaultdict(list)
        for email, accountId in email_to_account.items():
            main_account_id = find(accountId)
            group_by_account[main_account_id].append(email)

        # Step 3: build the result
        result = []
        for accountId, emails in group_by_account.items():
            data = [accounts[accountId][0]]
            data.extend(sorted(emails))
            result.append(data)
        
        return result