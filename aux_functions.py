#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:15:02 2019

@author: marius
"""

import numpy as np

# Move all users in a random direct (diagonal included)
def move_random(scenario):
    # Original locations
    locations = scenario['user_locations']
    
    # Edges of box
    xlim = scenario['xlim']
    ylim = scenario['ylim']
    
    # All possible movement operators
    movement_ops = np.asarray([-1, 0, 1])
    
    # For each user
    for user_idx in range(locations.shape[0]):
        # Generate possible new coordinates
        new_x = locations[user_idx][0] + movement_ops
        new_y = locations[user_idx][1] + movement_ops
        # Filter invalid ones
        new_x = new_x[(new_x >= xlim[0]) & (new_x <= xlim[1])]
        new_y = new_y[(new_y >= ylim[0]) & (new_y <= ylim[1])]
        # And pick a random one
        new_x = new_x[np.random.choice(len(new_x))]
        new_y = new_y[np.random.choice(len(new_y))]
        # Save new location
        locations[user_idx] = np.asarray([new_x, new_y])
    
    # Write new locations
    scenario['user_locations'] = locations
    
    # Return new dictionary
    return scenario

# One-step power adjustment scheme
def user_power_adjust(scenario, user_update_idx, sinr_update):
    # TODO: Perform update only for users in user_update_idx with the value in sinr_update
    return 0