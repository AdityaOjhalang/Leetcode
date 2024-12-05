class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_players = set()
        loss_count = defaultdict(int)

        # Populate all_players and loss_count
        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            loss_count[loser] += 1

        # Categorize players
        no_losses = [player for player in all_players if loss_count[player] == 0]
        one_loss = [player for player in loss_count if loss_count[player] == 1]

        # Sort the result lists
        return [sorted(no_losses), sorted(one_loss)]
            