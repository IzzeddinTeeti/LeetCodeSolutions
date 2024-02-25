class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}

        swaps = 0
    
        for i in range(0, len(row), 2):
            # Each person's partner can be found by adding 1 if the person is even,
            # or subtracting 1 if the person is odd.
            partner = row[i] ^ 1  # This finds the partner using XOR operation.

            # If the person's partner is not already sitting next to them...
            if row[i + 1] != partner:
                # Find the current position of the partner and the person next to the current person
                partner_pos = pos[partner]

                # Swap the partner with the person who is currently sitting next to the current person
                row[i + 1], row[partner_pos] = row[partner_pos], row[i + 1]

                # Update the positions in the mapping
                pos[row[partner_pos]], pos[row[i + 1]] = pos[row[i + 1]], pos[row[partner_pos]]

                # Increment the swap counter
                swaps += 1

        return swaps
