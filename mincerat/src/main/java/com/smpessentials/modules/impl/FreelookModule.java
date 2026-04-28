package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import net.minecraft.client.Minecraft;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraftforge.client.event.RenderGameOverlayEvent;
import net.minecraftforge.fml.common.gameevent.TickEvent;
import org.lwjgl.input.Keyboard;
import org.lwjgl.input.Mouse;

/**
 * Freelook - Hold the keybind to rotate the camera independently of your player.
 *
 * Unlike the other modules, this one is "hold to activate" rather than toggle.
 * The camera yaw/pitch are captured when you press the key, and mouse movement
 * updates only the camera while held. On release, the camera snaps back.
 */
public class FreelookModule extends Module implements ModuleManager.Tickable {

    private boolean active = false;
    private float cameraYaw;
    private float cameraPitch;
    private float playerYaw;
    private float playerPitch;

    public FreelookModule() {
        super("Freelook", "Hold key to look around without moving your body", Keyboard.KEY_LMENU); // Left Alt
    }

    @Override
    public void onTick() {
        // Freelook uses hold-mode: we check the key state every tick
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null) return;

        boolean keyDown = Keyboard.isKeyDown(getDefaultKey());

        if (keyDown && !active) {
            // Just pressed: capture current rotation
            active = true;
            playerYaw = mc.thePlayer.rotationYaw;
            playerPitch = mc.thePlayer.rotationPitch;
            cameraYaw = playerYaw;
            cameraPitch = playerPitch;
        } else if (!keyDown && active) {
            // Just released: restore player rotation
            active = false;
            mc.thePlayer.rotationYaw = playerYaw;
            mc.thePlayer.rotationPitch = playerPitch;
            mc.thePlayer.rotationYawHead = playerYaw;
        }

        if (active) {
            // The player's actual aim stays locked
            mc.thePlayer.rotationYaw = playerYaw;
            mc.thePlayer.rotationPitch = playerPitch;
            mc.thePlayer.rotationYawHead = playerYaw;

            // Camera follows mouse via the render view entity trick
            // We override the render pitch/yaw in the camera event
            // For 1.8.9, we can set the player's prev rotations to fake camera
            // A cleaner approach uses EntityViewRenderEvent, but this works:
            cameraYaw += Mouse.getDX() * 0.15f;
            cameraPitch -= Mouse.getDY() * 0.15f;
            cameraPitch = Math.max(-90f, Math.min(90f, cameraPitch));
        }
    }

    public boolean isActive() {
        return active && isEnabled();
    }

    public float getCameraYaw() {
        return cameraYaw;
    }

    public float getCameraPitch() {
        return cameraPitch;
    }
}
