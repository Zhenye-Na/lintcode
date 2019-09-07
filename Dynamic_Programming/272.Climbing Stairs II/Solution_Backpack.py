class Solution:

    def climbStairs2(self, num_of_stairs):

        different_steps_could_be_taken = [1, 2, 3]

        num_of_ways = [1] + [0 for _ in range(num_of_stairs)]
        for stairs_to_climb in range(1, len(num_of_ways)):
            for steps in different_steps_could_be_taken:
                if stairs_to_climb < steps:
                    continue
                num_of_ways[stairs_to_climb] += num_of_ways[stairs_to_climb - steps]

        return num_of_ways[-1]
