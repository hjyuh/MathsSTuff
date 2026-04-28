# SMP Essentials — Forge 1.8.9

A lightweight QoL mod for your SMP with friends.

## Modules & Keybinds

| Module          | Key       | Description                                      |
|-----------------|-----------|--------------------------------------------------|
| Fullbright      | `B`       | Max gamma — see everything, no torches needed    |
| Coords HUD      | `H`       | Shows XYZ, facing direction, and biome on-screen |
| Mob ESP          | `X`       | Highlights hostile mobs (and optionally players) |
| Freelook         | `Left Alt`| **Hold** to look around without rotating body    |
| Death Waypoints  | `J`       | Marks your death locations with a beacon & label |

All modules toggle on/off with a chat notification (except Freelook which is hold-to-use).

## Setup

### Prerequisites
- Java 8 JDK
- IntelliJ IDEA or Eclipse

### Steps

1. **Download the Forge 1.8.9 MDK** from https://files.minecraftforge.net/net/minecraftforge/forge/index_1.8.9.html
2. Extract the MDK zip into a folder
3. **Replace** the `src/` folder and `build.gradle` in the MDK with the ones from this project
4. Copy `mcmod.info` into `src/main/resources/`
5. Open a terminal in the project folder and run:
   ```bash
   # Generate IDE workspace
   ./gradlew setupDecompWorkspace

   # For IntelliJ:
   ./gradlew idea

   # For Eclipse:
   ./gradlew eclipse
   ```
6. Open the project in your IDE
7. Run the Minecraft client from your IDE to test (`./gradlew runClient` also works)
8. To build the final .jar:
   ```bash
   ./gradlew build
   ```
   The jar will be in `build/libs/SMPEssentials-1.0.0.jar`

### Installing
Drop the built `.jar` into your `.minecraft/mods/` folder (with Forge 1.8.9 installed).

## Project Structure

```
src/main/java/com/smpessentials/
├── SMPEssentials.java          # Main mod entry point
├── KeybindHandler.java         # Keybind → module toggle router
├── modules/
│   ├── Module.java             # Base module class
│   ├── ModuleManager.java      # Registry + event forwarding
│   └── impl/
│       ├── FullbrightModule.java
│       ├── CoordinatesHUDModule.java
│       ├── MobESPModule.java
│       ├── FreelookModule.java
│       └── DeathWaypointsModule.java
└── render/
    ├── RenderUtils.java        # GL rendering helpers
    └── FreelookCameraHandler.java
```

## Adding New Modules

1. Create a new class in `modules/impl/` extending `Module`
2. Implement any of the interfaces: `Tickable`, `RenderableHUD`, `RenderableWorld`, `DeathListener`
3. Register it in `ModuleManager.registerAll()`
4. Done — the event system handles the rest

## License
Do whatever you want with it. It's for your SMP.
