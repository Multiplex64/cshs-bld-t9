`EHS COMPUTER SCIENCE HONORS SOCIETY BUILD DIVISION`
# TEAM 9

# Static Photo Generator

## Project Overview

This project is aimed to create software that can combine multiple frames of a video or a collection of photos into one image that removes moving objects. This project needs a completely still background to function, and does not use AI technology to artificially guess a background.

Example: A photographer may want to get a photo of a famous building like the White House. They can set up their camera and take multiple photos from the same location. However, pedestrians will likely appear somewhere in the photo at any given time, which may be undesired. Instead of using AI tools that can incorrectly guess what could be behind unwanted objects, the photographer can take a continuous video and put the frames into this software, which will strip all the moving people and replace them with the background from other frames.

## How it Will Work

When a video is taken of a static background, each pixel spends most of its time the same color, but changes occasionally when a moving object comes into frame. Our software can take all the frames and remove pixels that stray far from the averages, and use that to generate a single clear image.

## Development

This repository has just been created, so things are still in a bit of disarray. For now, we are in the phase of creating prototype ideas. Any created prototypes should go inside its own folder. [More Info Here.](prototypes/README.md)