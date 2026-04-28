package com.smpessentials.modules.impl;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import net.minecraft.client.Minecraft;
import org.lwjgl.input.Keyboard;

public class AutoSprintModule extends Module implements ModuleManager.Tickable {

    public AutoSprintModule() {
        super("Auto Sprint", "Automatically sprints when moving forward", Keyboard.KEY_V);
    }

    @Override
    public void onTick() {
        Minecraft mc = Minecraft.getMinecraft();
        if (mc.thePlayer == null || mc.currentScreen != null) return;

        // Sprint when the player is moving forward and not sneaking/using items
        if (mc.thePlayer.moveForward > 0
                && !mc.thePlayer.isSneaking()
                && !mc.thePlayer.isUsingItem()
                && !mc.thePlayer.isCollidedHorizontally
                && mc.thePlayer.getFoodStats().getFoodLevel() > 6) {
            mc.thePlayer.setSprinting(true);
        }
    }
}
