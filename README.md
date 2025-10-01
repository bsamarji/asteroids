# Asteroids 🛸☄️

## Description

I have developed a replica of the asteroids video game in python, using the pygame library to practice object-orientated programming (OOP).

## Setup

I used the uv package manager for project management, so you need to have the uv package manager installed and you can use the `uv sync` command to install the packages specified in the uv.lock file.

## Usage

Once you'vre re-created the environment, just run the command below to run the game:

```
uv run main.py
```

The controls are:

- W key: forwards
- S key: backwards
- A key: pivot left
- D key: pivot right
- Space key: shoot bullets

You can also use cmd + q on Mac (or equivalent command on another OS) to quit the game.

## New Features 👀

The game is fully playable, however I would like to get around to adding features from the list of improvements below to enhance the user experience of the game:

- Add a scoring system
- Implement multiple lives and re-spawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped
