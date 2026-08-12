# Manual Test Plan: Unity Hovercraft Simulation

# 1. Objective

The purpose of this test plan is to verify the core mechanics, physics interactions, and audio triggers for the hovercraft simulation. Testing will ensure that the player vehicle interacts correctly with the terrain meshes and that all audio feedback aligns with the game state.

# 2. Scope

**In Scope:**

* Hovercraft movement mechanics (acceleration, deceleration, rotation).
* Collision detection between the hovercraft and terrain meshes/boundaries.
* Triggering and scaling of environmental and mechanical audio.

**Out of Scope:**

* Main menu UI and settings configurations.
* Performance profiling and frame-rate optimization.
* Static Prefabs and Models that are in the scene.

# 3. Test Environment

* **Engine:** Unity Editor
* **OS:** Windows 10
* **Input Device:** Standard QWERTY Keyboard and Mouse

# 4. High-Level Test Scenarios

## 4.1 Hovercraft Mechanics

* **Test Case 01:** Pressing 'W' key accelerates the hovercraft forward smoothly.
* **Test Case 02:** Pressing 'S' key decelerates and reverses the hovercraft.
* **Test Case 03:** Pressing 'A' or 'D' keys rotates the hovercraft correctly on its axis.
* **Test Case 04 (Edge Case):** Verify the hovercraft's maximum speed is capped and does not infinitely accelerate when holding the forward input.

## 4.2. Terrain & Mesh Collisions

* **Test Case 05:** Verify the hovercraft maintains a consistent floating distance above flat terrain meshes.
* **Test Case 06:** Hovercraft angles itself appropriately when navigating up an inclined terrain mesh.
* **Test Case 07 (Edge Case):** Dropping from a high elevation prevents the hovercraft from clipping through the floor mesh.
* **Test Case 08 (Negative Test):** The hovercraft successfully collides with boundary walls and does not pass outside the playable map.


## 4.3. Audio Triggers
* **Test Case 09:** Idle engine audio plays on a loop when the hovercraft is stationary.
* **Test Case 10:** The engine audio pitch increases dynamically as the hovercraft accelerates.
* **Test Case 11:** Distinct impact sound effect triggers immediately upon colliding with a terrain wall.