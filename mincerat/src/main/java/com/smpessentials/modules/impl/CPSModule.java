package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.FontRenderer;
import net.minecraft.client.gui.ScaledResolution;
import net.minecraft.util.EnumChatFormatting;
import net.minecraftforge.client.event.RenderGameOverlayEvent;
import org.lwjgl.input.Keyboard;
import org.lwjgl.input.Mouse;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class CPSModule extends Module implements ModuleManager.RenderableHUD, ModuleManager.Tickable {

    // Track timestamps of recent clicks within a rolling 1-second window
    private final List<Long> leftClicks = new ArrayList<>();
    private final List<Long> rightClicks = new ArrayList<>();
    private boolean leftWasDown = false;
    private boolean rightWasDown = false;

    public CPSModule() {
        super("CPS Counter", "Displays clicks per second (left + right)", Keyboard.KEY_C);
    }

    @Override
    public void onTick() {
        long now = System.currentTimeMillis();

        // Detect left click edges
        boolean leftDown = Mouse.isButtonDown(0);
        if (leftDown && !leftWasDown) {
            leftClicks.add(now);
        }
        leftWasDown = leftDown;

        // Detect right click edges
        boolean rightDown = Mouse.isButtonDown(1);
        if (rightDown && !rightWasDown) {
            rightClicks.add(now);
        }
        rightWasDown = rightDown;

        // Prune clicks older than 1 second
        pruneOld(leftClicks, now);
        pruneOld(rightClicks, now);
    }

    private void pruneOld(List<Long> clicks, long now) {
        Iterator<Long> it = clicks.iterator();
        while (it.hasNext()) {
            if (now - it.next() > 1000) {
                it.remove();
            }
        }
    }

    @Override
    public void onRenderHUD(RenderGameOverlayEvent.Post event) {
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null || mc.currentScreen != null) return;

        FontRenderer fr = mc.fontRendererObj;
        ScaledResolution sr = new ScaledResolution(mc);

        int leftCPS = leftClicks.size();
        int rightCPS = rightClicks.size();

        String text = EnumChatFormatting.WHITE.toString() + leftCPS +
                EnumChatFormatting.GRAY + " | " +
                EnumChatFormatting.WHITE + rightCPS +
                EnumChatFormatting.GRAY + " CPS";

        // Top-right corner, below FPS counter
        int x = sr.getScaledWidth() - fr.getStringWidth(text) - 4;
        int y = 4 + fr.FONT_HEIGHT + 5; // offset below FPS

        // Background
        int bgWidth = fr.getStringWidth(text) + 6;
        net.minecraft.client.gui.Gui.drawRect(x - 3, y - 2, x + bgWidth - 3, y + fr.FONT_HEIGHT + 1, 0x80000000);

        fr.drawStringWithShadow(text, x, y, 0xFFFFFF);
    }
}
