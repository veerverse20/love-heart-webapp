import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Main heart coordinates (big one)
t = np.linspace(0, 2 * np.pi, 1000)
x_main = 16 * np.sin(t)**3
y_main = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Mini hearts (orbiting)
num_mini_hearts = 12
angles = np.linspace(0, 2*np.pi, num_mini_hearts, endpoint=False)
r = 22  # orbit radius

# Heart shape for orbiting hearts
t_mini = np.linspace(0, 2 * np.pi, 100)
x_heart = 1.5 * 16 * np.sin(t_mini)**3 / 20
y_heart = 1.5 * (13 * np.cos(t_mini) - 5 * np.cos(2*t_mini) - 2 * np.cos(3*t_mini) - np.cos(4*t_mini)) / 20

# Setup the plot
fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.axis('off')

# Plot main heart
main_line, = ax.plot([], [], lw=3, color='deeppink')
glow = ax.scatter([], [], s=0.5, color='hotpink', alpha=0.03)

# Mini hearts (scatter plots)
mini_hearts = [ax.plot([], [], color='pink', lw=1)[0] for _ in range(num_mini_hearts)]

# Message
msg = "To My Queen 👑\nI'm Sorry, Please Smile Again 🥺💕"
plt.text(0, -25, msg, fontsize=14, color='white', ha='center', fontweight='bold', family='monospace')

# Animation function
def animate(i):
    # Main heart animation
    main_line.set_data(x_main[:i], y_main[:i])
    glow.set_offsets(np.column_stack((x_main[:i], y_main[:i])))

    # Rotate mini hearts around the center
    for idx, heart in enumerate(mini_hearts):
        angle = angles[idx] + i * 0.02
        cx = r * np.cos(angle)
        cy = r * np.sin(angle)
        heart.set_data(cx + x_heart, cy + y_heart)

    return [main_line, glow] + mini_hearts

# Run animation
ani = FuncAnimation(fig, animate, frames=len(x_main), interval=2, blit=True)
plt.show()
