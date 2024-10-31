# Upper Confidence Bound (UCB) in R

## Importing the Dataset
dataset <- read.csv("Ads_CTR_Optimisation.csv")
# View(dataset) # nolint

## Implementing Upper Confidence Bound (UCB)
N <- 10000 # nolint
d <- 10

ads_selected <- integer()
nums_of_selections <- integer(d)
sums_of_rewards <- integer(d)
total_reward <- 0

for (n in 1:N){
    ad <- 0
    max_upper_bound <- 0
    for (i in 1:d) {
        if (nums_of_selections[i] > 0) {
            avg_reward <- sums_of_rewards[i] / nums_of_selections[i]
            delta_i <- sqrt(3 / 2 * log(n) / nums_of_selections[i])
            upper_bound <- avg_reward + delta_i
        } else {
           upper_bound <- 1e400
        }

        if (upper_bound > max_upper_bound) {
            max_upper_bound <- upper_bound
            ad <- i
        }
    }
    ads_selected <- append(ads_selected, ad)
    nums_of_selections[ad] <- nums_of_selections[ad] + 1

    reward <- dataset[n, ad]
    sums_of_rewards[ad] <- sums_of_rewards[ad] + reward
    total_reward <- total_reward + reward
}

## Visualising the results - Histogram
hist(ads_selected,
     col = "blue",
     main = "Histogram of Ads Selections",
     xlab = "Ads",
     ylab = "Number of times each Ad was Selected")