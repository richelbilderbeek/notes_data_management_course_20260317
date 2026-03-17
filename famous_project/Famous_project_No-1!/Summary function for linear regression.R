set.seed(93274)                 # Create random data
my_x <- rnorm(1000)
my_y <- rnorm(1000) + my_x

mod <- lm(my_y ~ my_x)          # Estimate linear regression model

summary(mod)                    # Apply summary function to model