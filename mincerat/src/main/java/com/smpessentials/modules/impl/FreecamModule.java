package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import com.smpessentials.render.RenderUtils;
import net.minecraft.client.Minecraft;
import net.minecraft.client.entity.EntityOtherPlayerMP;
import net.minecraft.client.settings.KeyBinding;
import net.minecraft.util.ChatComponentText;
import net.minecraft.util.EnumChatFormatting;
import net.minecraftforge.client.event.RenderWorldLastEvent;
import org.lwjgl.input.Keyboard;
import org.lwjgl.input.Mouse;

/**
 * Freecam — detach from your player and fly around as an invisible camera.
 *
 * Your player stays in place (server sees no movement). The camera moves
 * freely with WASD + space/shift, mouse controls look direction.
 * Great for scouting caves with Fullbright.
 *
 * Toggle on/off with the keybind. On disable, snaps back to player position.
 */
public class FreecamModule extends Module implements ModuleManager.Tickable, ModuleManager.RenderableWorld {

    private double camX, camY, camZ;
    private float camYaw, camPitch;
    private double playerX, playerY, playerZ;
    private float playerYaw, playerPitch;
    private float flySpeed = 0.5f;

    // Fake player entity to show where you actually are
    private EntityOtherPlayerMP fakePlayer;

    public FreecamModule() {
        super("Freecam", "Fly around as an invisible camera (your body stays still)", Keyboard.KEY_G);
    }

    @Override
    protected void onEnable() {
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null) return;

        // Save player state
        playerX = mc.thePlayer.posX;
        playerY = mc.thePlayer.posY;
        playerZ = mc.thePlayer.posZ;
        playerYaw = mc.thePlayer.rotationYaw;
        playerPitch = mc.thePlayer.rotationPitch;

        // Initialize camera at player position
        camX = playerX;
        camY = playerY;
        camZ = playerZ;
        camYaw = playerYaw;
        camPitch = playerPitch;

        // Create a fake player entity so you can see where your body is
        try {
            fakePlayer = new EntityOtherPlayerMP(mc.theWorld, mc.thePlayer.getGameProfile());
            fakePlayer.copyLocationAndAnglesFrom(mc.thePlayer);
            fakePlayer.rotationYawHead = mc.thePlayer.rotationYaw;
            mc.theWorld.addEntityToWorld(-1337, fakePlayer);
        } catch (Exception e) {
            fakePlayer = null;
        }
    }

    @Override
    protected void onDisable() {
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null) return;

        // Restore player position (client-side only)
        mc.thePlayer.setPositionAndRotation(playerX, playerY, playerZ, playerYaw, playerPitch);

        // Remove fake player
        if (fakePlayer != null) {
            mc.theWorld.removeEntityFromWorld(-1337);
            fakePlayer = null;
        }
    }

    @Override
    public void onTick() {
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null || mc.currentScreen != null) return;

        // ── Handle mouse look ──
        float dx = Mouse.getDX() * 0.15f;
        float dy = Mouse.getDY() * 0.15f;
        camYaw += dx;
        camPitch -= dy;
        camPitch = Math.max(-90f, Math.min(90f, camPitch));

        // ── Handle movement (WASD + Space/Shift) ──
        double motionX = 0, motionY = 0, motionZ = 0;

        float yawRad = (float) Math.toRadians(camYaw);
        float cosYaw = (float) Math.cos(yawRad);
        float sinYaw = (float) Math.sin(yawRad);

        // Speed boost with Ctrl
        float speed = Keyboard.isKeyDown(Keyboard.KEY_LCONTROL) ? flySpeed * 3f : flySpeed;

        // Forward/back (W/S)
        if (Keyboard.isKeyDown(mc.gameSettings.keyBindForward.getKeyCode())) {
            motionX -= sinYaw * speed;
            motionZ += cosYaw * speed;
        }
        if (Keyboard.isKeyDown(mc.gameSettings.keyBindBack.getKeyCode())) {
            motionX += sinYaw * speed;
            motionZ -= cosYaw * speed;
        }

        // Strafe (A/D)
        if (Keyboard.isKeyDown(mc.gameSettings.keyBindLeft.getKeyCode())) {
            motionX += cosYaw * speed;
            motionZ += sinYaw * speed;
        }
        if (Keyboard.isKeyDown(mc.gameSettings.keyBindRight.getKeyCode())) {
            motionX -= cosYaw * speed;
            motionZ -= sinYaw * speed;
        }

        // Up/Down (Space/Shift)
        if (Keyboard.isKeyDown(mc.gameSettings.keyBindJump.getKeyCode())) {
            motionY += speed;
        }
        if (Keyboard.isKeyDown(mc.gameSettings.keyBindSneak.getKeyCode())) {
            motionY -= speed;
        }

        camX += motionX;
        camY += motionY;
        camZ += motionZ;

        // ── Move the actual player entity to the camera pos for rendering ──
        // This is client-side only — server still sees the original position
        mc.thePlayer.setPositionAndRotation(camX, camY, camZ, camYaw, camPitch);
        mc.thePlayer.rotationYawHead = camYaw;

        // Prevent the player from sending movement packets
        mc.thePlayer.motionX = 0;
        mc.thePlayer.motionY = 0;
        mc.thePlayer.motionZ = 0;

        // Keep the fake player at the original location
        if (fakePlayer != null) {
            fakePlayer.setPositionAndRotation(playerX, playerY, playerZ, playerYaw, playerPitch);
            fakePlayer.rotationYawHead = playerYaw;
        }
    }

    @Override
    public void onRenderWorld(RenderWorldLastEvent event) {
        // Optionally render a label above the fake player so you can find your body
        if (fakePlayer != null) {
            net.minecraft.client.renderer.entity.RenderManager rm = Minecraft.getMinecraft().getRenderManager();
            double rx = fakePlayer.posX - rm.viewerPosX;
            double ry = fakePlayer.posY + fakePlayer.height + 0.5 - rm.viewerPosY;
            double rz = fakePlayer.posZ - rm.viewerPosZ;
            RenderUtils.drawWorldText(EnumChatFormatting.YELLOW + "Your Body", rx, ry, rz);
        }
    }

    public float getFlySpeed() {
        return flySpeed;
    }

    public void setFlySpeed(float flySpeed) {
        this.flySpeed = flySpeed;
    }
}
