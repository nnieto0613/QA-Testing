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

# 3. Test Environment

* **Engine:** Unity Editor
* **OS:** Windows 11 / macOS 14
* **Input Device:** Standard QWERTY Keyboard and Mouse

# 4. High-Level Test Scenarios

# 4.1 Hovercraft Mechanics

* **Test Case 01:** Verify the hovercraft accelerates forward smoothly when the 'W' key is pressed.
* **Test Case 02:** Verify the hovercraft decelerates and reverses when the 'S' key is pressed.
* **Test Case 03:** Verify the hovercraft rotates correctly on its axis when the 'A' or 'D' keys are pressed.
* **Test Case 04 (Edge Case):** Verify the hovercraft's maximum speed is capped and does not infinitely accelerate when holding the forward input.

# 4.2. Terrain & Mesh Collisions

* **Test Case 05:** Verify the hovercraft maintains a consistent floating distance above flat terrain meshes.
* **Test Case 06:** Verify the hovercraft appropriately angles itself when navigating up an inclined terrain mesh.
* **Test Case 07 (Edge Case):** Verify the hovercraft cannot clip through the floor mesh when dropping from a high elevation.
* **Test Case 08 (Negative Test):** Verify the hovercraft successfully collides with boundary walls and does not pass outside the playable map.


# 4.3. Audio Triggers
* **Test Case 09:** Verify the idle engine audio plays on a loop when the hovercraft is stationary.
* **Test Case 10:** Verify the engine audio pitch increases dynamically as the hovercraft accelerates.
* **Test Case 11:** Verify a distinct impact sound effect triggers immediately upon colliding with a terrain wall.