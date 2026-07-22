---
layout: project
title: ENDSTATION
permalink: /projects/endstation/index.html
tagline: "Classic Dice-Gambling Game in a grungy subway."
description: "Win dice, upgrade your set, and create synergies. My first fully released solo project — a dice roguelike adaptation of 10,000 / Farkel with PS-X style visuals."
hero: /assets/images/endstation-library_hero.png
role: Solo Developer
year: 2025–2026
status: Released
engine: Godot 4.4
platform: PC (Steam)
cta:
  - { label: "Play on Steam",   url: "https://store.steampowered.com/app/4240810/ENDSTATION/" }
  - { label: "Devlog on Bluesky", url: "https://bsky.app/profile/bal-duin.bsky.social" }
gallery:
  - { src: /assets/images/endstation-Godot_v4.4.1-stable_win64_mQRzBoyDLK.png, alt: "Subway platform scene" }
  - { src: /assets/images/endstation-Godot_v4.4.1-stable_win64_kontq7b21A.png, alt: "Dice-rolling gameplay" }
  - { src: /assets/images/endstation-Godot_v4.4.1-stable_win64_AfTvoEIXay.png, alt: "Upgrade selection" }
  - { src: /assets/images/endstation-Godot_v4.4.1-stable_win64_mL223rmi6p.png, alt: "In-game UI" }
---

## Game Design

Adaptation of *10,000* / *Farkel*. The goal: transform a proven, simple dice game into a fun videogame by adding special dice and rules. Each run introduces new dice with unique abilities — players combine them to build synergies, chase high scores, and unlock more powerful sets as they progress.

## Game Art

Retro PS-X aesthetic. All 3D assets are modelled and textured in Blender, with an additional post-processing shader built in Godot to push the look further. The game renders at 1024×576, limited to a quarter of the color-space with PS-X style dithering — a deliberate constraint that gave the project a strong, cohesive visual identity.

## Tech Art

Custom Godot shaders handle the dithering and color-bleed effects. The pipeline was kept lean to ship within the time budget.

## Project

A solo project with two goals: learn the process of releasing a game on Steam, and find out how fast I could develop a fun game end-to-end. Answer to the second question: about five months from prototype to release.
