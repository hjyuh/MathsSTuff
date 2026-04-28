package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.FontRenderer;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.util.EnumChatFormatting;
import net.minecraft.util.MathHelper;
import net.minecraftforge.client.event.RenderGameOverlayEvent;
import org.lwjgl.input.Keyboard;

public class CoordinatesHUDModule extends Module implements ModuleManager.RenderableHUD {

    public CoordinatesHUDModule() {
        super("Coords HUD", "Displays coordinates, direction, and biome", Keyboard.KEY_H);
    }

    @Override
    public void onRenderHUD(RenderGameOverlayEvent.Post event) {
        Minecraft mc = Minecraft.getMinecraft();
        EntityPlayer player = mc.thePlayer;
        if (player == null || mc.currentScreen != null) return;

        FontRenderer fr = mc.fontRendererObj;

        int x = MathHelper.floor_double(player.posX);
        int y = MathHelper.floor_double(player.posY);
        int z = MathHelper.floor_double(player.posZ);

        String facing = getCardinalDirection(player.rotationYaw);
        String biome = mc.theWorld.getBiomeGenForCoords(player.getPosition()).biomeName;

        String line1 = EnumChatFormatting.WHITE + "XYZ: " +
                EnumChatFormatting.GREEN + x +
                EnumChatFormatting.WHITE + " / " +
                EnumChatFormatting.GREEN + y +
                EnumChatFormatting.WHITE + " / " +
                EnumChatFormatting.GREEN + z;

        String line2 = EnumChatFormatting.WHITE + "Facing: " +
                EnumChatFormatting.AQUA + facing +
                EnumChatFormatting.GRAY + " | " +
                EnumChatFormatting.WHITE + "Biome: " +
                EnumChatFormatting.AQUA + biome;

        int padding = 4;

        // Draw background
        int bgWidth = Math.max(fr.getStringWidth(line1), fr.getStringWidth(line2)) + padding * 2;
        int bgHeight = fr.FONT_HEIGHT * 2 + padding * 2 + 2;
        net.minecraft.client.gui.Gui.drawRect(
            padding - 2, padding - 2,
            padding + bgWidth, padding + bgHeight,
            0x80000000
        );

        fr.drawStringWithShadow(line1, padding, padding, 0xFFFFFF);
        fr.drawStringWithShadow(line2, padding, padding + fr.FONT_HEIGHT + 2, 0xFFFFFF);
    }

    private String getCardinalDirection(float yaw) {
        float adjusted = MathHelper.wrapAngleTo180_float(yaw);
        if (adjusted >= -45 && adjusted < 45) return "South (+Z)";
        if (adjusted >= 45 && adjusted < 135) return "West (-X)";
        if (adjusted >= -135 && adjusted < -45) return "East (+X)";
        return "North (-Z)";
    }
}
