# Beats uses the changes in dynamics to change the shape size of the cube animation. The larger the dynamics, the larger the object created.

"""Sudo Code
define TakeInAudio(Audio)
= takes in audio sample, deduces overall magnitude of loudness on 1.0 scale, and builds appropriate shape based on value. Shapes could be squares or circles.

Input: array of volumes

Output: animation sequence

Requirements: delta = time interval between samples
