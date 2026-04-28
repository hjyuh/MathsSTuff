package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import com.smpessentials.render.RenderUtils;
import net.minecraft.client.Minecraft;
import net.minecraft.entity.Entity;
import net.minecraft.entity.monster.EntityMob;
import net.minecraft.entity.monster.EntitySlime;
import net.minecraft.entity.monster.EntityGhast;
import net.minecraft.entity.passive.EntityAnimal;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraftforge.client.event.RenderWorldLastEvent;
import org.lwjgl.input.Keyboard;

import java.awt.Color;

public class MobESPModule extends Module implements ModuleManager.RenderableWorld {

    // Colors for different mob types
    private static final Color HOSTILE_COLOR = new Color(255, 50, 50, 180);
    private static final Color PASSIVE_COLOR = new Color(50, 255, 50, 120);
    private static final Color PLAYER_COLOR = new Color(50, 150, 255, 180);

    private boolean showPassive = false;
    private boolean showPlayers = true;

    public MobESPModule() {
        super("Mob ESP", "Highlights hostile mobs so you can spot them", Keyboard.KEY_X);
    }

    @Override
    public void onRenderWorld(RenderWorldLastEvent event) {
        Minecraft mc = Minecraft.getMinecraft();
        EntityPlayer player = mc.thePlayer;
        if (player == null) return;

        float partialTicks = event.partialTicks;

        for (Entity entity : mc.theWorld.loadedEntityList) {
            if (entity == player) continue;
            if (entity.isDead) continue;

            double dist = player.getDistanceToEntity(entity);
            if (dist > 64) continue; // Don't render beyond 64 blocks

            Color color = null;

            if (entity instanceof EntityMob || entity instanceof EntitySlime || entity instanceof EntityGhast) {
                color = HOSTILE_COLOR;
            } else if (showPlayers && entity instanceof EntityPlayer) {
                color = PLAYER_COLOR;
            } else if (showPassive && entity instanceof EntityAnimal) {
                color = PASSIVE_COLOR;
            }

            if (color != null) {
                RenderUtils.drawEntityBoundingBox(entity, color, partialTicks);
            }
        }
    }

    public void setShowPassive(boolean showPassive) {
        this.showPassive = showPassive;
    }

    public void setShowPlayers(boolean showPlayers) {
        this.showPlayers = showPlayers;
    }
}
