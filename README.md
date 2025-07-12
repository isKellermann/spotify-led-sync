# Spotify Led Sync
- Changing LED's colors based the song being played on spotify.

## Project Goal
- Build a system that reads the currently playing Spotify song on a computer, extracts the dominant color from the song’s album art, and sends it to an STM32 microcontroller which controls RGB LEDs accordingly.

## Tech Stack

- Spotify API 
- Python 
- STM32F446RE
- UART serial communication

## Hardware

- STM32F446RE
- USB to Serial connection (via ST-Link)
- WS2812B LED strip
