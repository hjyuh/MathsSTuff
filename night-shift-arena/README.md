# Night Shift Arena

Original browser multiplayer horror prototype inspired by asymmetric night-shift survival games.

## Run

```powershell
npm install
npm start
```

Open `http://localhost:4173` in two browser tabs or two devices on the same network. Pick one guard and one mascot to start a round.

## Controls

- `WASD`: move
- Mouse: look around after clicking the game
- `Shift`: sprint
- `Q`: guard left office shutter
- `E`: guard right office shutter
- `C`: guard camera monitor
- `Esc`: release pointer lock

## Current Mechanics

- Free 3D movement in a small building
- WebSocket multiplayer state sync
- Guard and mascot roles
- Articulated guard and animatronic rigs with idle/walk motion
- First-person guard/mascot viewmodels
- Guard office with desk consoles, monitors, cameras, wall displays, and left/right shutters
- Shared round timer
- Guard power meter and shutter controls
- Mascot tagging/capture win condition

This deliberately uses original names, map, and visual design instead of copyrighted FNAF characters or assets.
