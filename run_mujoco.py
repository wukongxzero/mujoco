import gymnasium as gym
import time

# Create environment with GUI
env = gym.make("Ant-v5", render_mode="human")
obs, info = env.reset()

try:
    while True:
        action = env.action_space.sample()  # random action
        obs, reward, terminated, truncated, info = env.step(action)
        
        # Reset environment if episode ends
        if terminated or truncated:
            obs, info = env.reset()
        
        time.sleep(0.01)  # adjust for smooth animation

except KeyboardInterrupt:
    print("Simulation stopped by user.")

# Close the environment (window closes here)
env.close()
