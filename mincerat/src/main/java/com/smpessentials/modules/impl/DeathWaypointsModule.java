package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import com.smpessentials.render.RenderUtils;
import net.minecraft.client.Minecraft;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.util.BlockPos;
import net.minecraft.util.ChatComponentText;
import net.minecraft.util.EnumChatFormatting;
import net.minecraftforge.client.event.RenderWorldLastEvent;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import org.lwjgl.input.Keyboard;

import java.awt.Color;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class DeathWaypointsModule extends Module
        implements ModuleManager.RenderableWorld, ModuleManager.DeathListener {

    private static final Color DEATH_COLOR = new Color(255, 60, 60, 200);
    private static final int MAX_WAYPOINTS = 5;
    private static final SimpleDateFormat TIME_FMT = new SimpleDateFormat("HH:mm");

    private final List<DeathPoint> deathPoints = new ArrayList<>();

    public DeathWaypointsModule() {
        super("Death Waypoints", "Marks where you died with a beacon", Keyboard.KEY_J);
    }

    @Override
    public void onDeath(LivingDeathEvent event) {
        if (!(event.entity instanceof EntityPlayer)) return;

        Minecraft mc = Minecraft.getMinecraft();
        if (event.entity != mc.thePlayer) return;

        EntityPlayer player = mc.thePlayer;
        int x = (int) Math.floor(player.posX);
        int y = (int) Math.floor(player.posY);
        int z = (int) Math.floor(player.posZ);

        DeathPoint dp = new DeathPoint(x, y, z, System.currentTimeMillis());
        deathPoints.add(0, dp);

        // Cap to MAX_WAYPOINTS
        while (deathPoints.size() > MAX_WAYPOINTS) {
            deathPoints.remove(deathPoints.size() - 1);
        }

        // Notify in chat
        String msg = EnumChatFormatting.RED + "[SMP Essentials] " +
                EnumChatFormatting.WHITE + "Death location saved: " +
                EnumChatFormatting.YELLOW + x + ", " + y + ", " + z;
        player.addChatMessage(new ChatComponentText(msg));
    }

    @Override
    public void onRenderWorld(RenderWorldLastEvent event) {
        for (int i = 0; i < deathPoints.size(); i++) {
            DeathPoint dp = deathPoints.get(i);
            String label = EnumChatFormatting.RED + "☠ Death" +
                    (deathPoints.size() > 1 ? " #" + (i + 1) : "") +
                    EnumChatFormatting.GRAY + " (" + dp.x + ", " + dp.y + ", " + dp.z + ")" +
                    EnumChatFormatting.DARK_GRAY + " " + TIME_FMT.format(new Date(dp.timestamp));

            // Fade older waypoints
            float alpha = 1.0f - (i * 0.15f);
            Color color = new Color(
                DEATH_COLOR.getRed(), DEATH_COLOR.getGreen(), DEATH_COLOR.getBlue(),
                (int) (DEATH_COLOR.getAlpha() * alpha)
            );

            RenderUtils.drawWaypointBeacon(dp.x, dp.y, dp.z, color, label, event.partialTicks);
        }
    }

    public void clearWaypoints() {
        deathPoints.clear();
    }

    // ── Inner data class ──────────────────────────────────

    private static class DeathPoint {
        final int x, y, z;
        final long timestamp;

        DeathPoint(int x, int y, int z, long timestamp) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.timestamp = timestamp;
        }
    }
}
