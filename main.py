#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:18:32 2019

@author: marius
"""

import numpy as np

from aux_functions import init_scenario
from aux_functions import move_random, update_sinr
from aux_functions import user_power_adjust
from aux_functions import capacity_reward

from matplotlib import pyplot as plt

## Control global seed
#global_seed = 2019
#np.random.seed(global_seed)

## System parameters
# Box limits
xlim = np.asarray([0, 60])
ylim = np.asarray([0, 60])
# Epsilon distance stabilizer
# If two users have the same coordinates, replace their pairwise distance with this
epsilon_distance = 1e-2

# Number of users
num_users = 4
# Valid power levels
p_steps = 40
p_valid = np.logspace(0, 1, p_steps)
# Noise power (universal)
noise_power = 10 ** (-30 / 10)
# User SINR (QOS) requirements
eta = 10 ** (-3 * np.ones((num_users,)) / 10)
# Reward penalty for not satisfying QoS
eta_penalty = -1

# Number of timesteps (can also be infinite)
num_steps = 1000

## Scenario dictionary
scenario = init_scenario(num_users, xlim, ylim, epsilon_distance,
                         noise_power, p_valid, eta,
                         eta_penalty)

## Time evolution
reward_hist = []
# For each timestep
for time_idx in range(num_steps):
    # Increment user locations
    scenario = move_random(scenario)
    
    # Update SINR values
    scenario = update_sinr(scenario)
    
    # Pick random user
    random_user_idx = np.random.randint(low=0, high=num_users)
    
    # Send SINR update to a specific user
    scenario = user_power_adjust(scenario, random_user_idx)
        
    # Receive new sum-rate as reward
    reward = capacity_reward(scenario)
    
    # Store metrics
    reward_hist.append(reward)

# Convert to arrays
reward_hist = np.asarray(reward_hist)
# Plot
plt.figure(); plt.plot(reward_hist, '--'); plt.show()