import numpy as np
import matplotlib.pyplot as plt

# Function to simulate a bandit with a given mean and standard deviation
def bandit(mean, std_dev):
    return np.random.normal(mean, std_dev)

# Thompson Sampling algorithm
def thompson_sampling(num_bandits, num_rounds, true_means, true_std_devs):
    num_actions = len(true_means)
    total_rewards = np.zeros(num_actions)
    action_counts = np.zeros(num_actions)

    rewards_per_round = []

    for _ in range(num_rounds):
        # Sample from the posterior distribution for each bandit
        samples = [np.random.normal(total_rewards[i] / (action_counts[i] + 1e-6), true_std_devs[i] / np.sqrt(action_counts[i] + 1e-6))
                   for i in range(num_actions)]

        # Select action with the highest sampled value
        selected_action = np.argmax(samples)

        # Simulate the selected bandit and observe the reward
        reward = bandit(true_means[selected_action], true_std_devs[selected_action])
        total_rewards[selected_action] += reward
        action_counts[selected_action] += 1

        rewards_per_round.append(reward)

    return rewards_per_round

# Number of bandits (actions)
num_bandits = 5

# Number of rounds (iterations)
num_rounds = 1000

# True mean values for each bandit (unknown to the algorithm)
true_means = [2.0, 1.5, 1.0, 2.5, 1.2]

# True standard deviation values for each bandit (unknown to the algorithm)
true_std_devs = [1.0, 0.8, 0.5, 1.2, 1.0]

# Run Thompson Sampling algorithm
rewards = thompson_sampling(num_bandits, num_rounds, true_means, true_std_devs)

# Plot the cumulative reward over rounds
cumulative_rewards = np.cumsum(rewards)
average_rewards = cumulative_rewards / (np.arange(num_rounds) + 1)

plt.plot(average_rewards)
plt.xlabel('Rounds')
plt.ylabel('Average Reward')
plt.title('Thompson Sampling Algorithm')
plt.show()