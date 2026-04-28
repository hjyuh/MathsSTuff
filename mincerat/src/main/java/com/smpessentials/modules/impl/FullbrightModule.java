package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import net.minecraft.client.Minecraft;
import org.lwjgl.input.Keyboard;

public class FullbrightModule extends Module implements ModuleManager.Tickable {

    private float previousGamma = -1f;

    public FullbrightModule() {
        super("Fullbright", "Maximizes gamma so you can see in the dark", Keyboard.KEY_B);
    }

    @Override
    protected void onEnable() {
        Minecraft mc = Minecraft.getMinecraft();
        previousGamma = mc.gameSettings.gammaSetting;
        mc.gameSettings.gammaSetting = 100f;
    }

    @Override
    protected void onDisable() {
        Minecraft mc = Minecraft.getMinecraft();
        if (previousGamma >= 0) {
            mc.gameSettings.gammaSetting = previousGamma;
        } else {
            mc.gameSettings.gammaSetting = 1.0f;
        }
    }

    @Override
    public void onTick() {
        // Keep gamma pinned in case something resets it
        Minecraft.getMinecraft().gameSettings.gammaSetting = 100f;
    }
}
