import numpy as np
import matplotlib.pyplot as plt

# Function to simulate a bandit with a given mean and standard deviation
def bandit(mean, std_dev):
    return np.random.normal(mean, std_dev)

# UCB algorithm
def ucb_bandit(num_bandits, num_rounds, true_means, exploration_parameter):
    num_actions = len(true_means)
    total_rewards = np.zeros(num_actions)
    action_counts = np.zeros(num_actions)
    estimated_means = np.zeros(num_actions)

    rewards_per_round = []

    for _ in range(num_rounds):
        # Select action using UCB strategy
        ucb_values = estimated_means + exploration_parameter * np.sqrt(np.log(np.sum(action_counts)) / (action_counts + 1e-6))
        selected_action = np.argmax(ucb_values)

        # Simulate the selected bandit and observe the reward
        reward = bandit(true_means[selected_action], 1.0)
        total_rewards[selected_action] += reward
        action_counts[selected_action] += 1
        estimated_means[selected_action] = total_rewards[selected_action] / action_counts[selected_action]

        rewards_per_round.append(reward)

    return rewards_per_round

# Number of bandits (actions)
num_bandits = 5

# Number of rounds (iterations)
num_rounds = 1000

# True mean values for each bandit (unknown to the algorithm)
true_means = [2.0, 1.5, 1.0, 2.5, 1.2]

# Exploration parameter for UCB
exploration_parameter = 2.0

# Run UCB algorithm
rewards = ucb_bandit(num_bandits, num_rounds, true_means, exploration_parameter)

# Plot the cumulative reward over rounds
cumulative_rewards = np.cumsum(rewards)
average_rewards = cumulative_rewards / (np.arange(num_rounds) + 1)

plt.plot(average_rewards)
plt.xlabel('Rounds')
plt.ylabel('Average Reward')
plt.title('Upper Confidence Bound (UCB) Algorithm')
plt.show()