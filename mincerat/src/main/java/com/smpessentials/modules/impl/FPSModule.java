package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.FontRenderer;
import net.minecraft.client.gui.ScaledResolution;
import net.minecraft.util.EnumChatFormatting;
import net.minecraftforge.client.event.RenderGameOverlayEvent;
import org.lwjgl.input.Keyboard;

public class FPSModule extends Module implements ModuleManager.RenderableHUD {

    public FPSModule() {
        super("FPS Counter", "Displays current FPS on screen", Keyboard.KEY_F);
    }

    @Override
    public void onRenderHUD(RenderGameOverlayEvent.Post event) {
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null || mc.currentScreen != null) return;

        FontRenderer fr = mc.fontRendererObj;
        ScaledResolution sr = new ScaledResolution(mc);

        int fps = Minecraft.getDebugFPS();

        // Color based on FPS thresholds
        EnumChatFormatting color;
        if (fps >= 60) {
            color = EnumChatFormatting.GREEN;
        } else if (fps >= 30) {
            color = EnumChatFormatting.YELLOW;
        } else {
            color = EnumChatFormatting.RED;
        }

        String text = color.toString() + fps + " FPS";

        // Top-right corner
        int x = sr.getScaledWidth() - fr.getStringWidth(text) - 4;
        int y = 4;

        // Background
        int bgWidth = fr.getStringWidth(text) + 6;
        net.minecraft.client.gui.Gui.drawRect(x - 3, y - 2, x + bgWidth - 3, y + fr.FONT_HEIGHT + 1, 0x80000000);

        fr.drawStringWithShadow(text, x, y, 0xFFFFFF);
    }
}
