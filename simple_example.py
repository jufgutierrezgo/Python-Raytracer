import numpy as np
import sightpy as sp

# Create a scene
scene = sp.Scene()

# Define an emissive material (light source)
light_material = sp.Emissive(emission_color=np.array([1.0, 1.0, 1.0]), intensity=10.0)

# Define a sphere as the light source
light = sp.Sphere(center=np.array([0, 5, 0]), radius=0.5, material=light_material)

# Add the light source to the scene
scene.add(light)

# Define a camera
camera = sp.Camera(position=np.array([0, 1, -5]), look_at=np.array([0, 1, 0]))

# Render the scene
renderer = sp.render(scene, camera)
image = renderer.render()

# Save the image
sp.save_image(image, "output.png")
