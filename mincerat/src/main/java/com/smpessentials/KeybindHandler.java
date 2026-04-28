package com.smpessentials;

import com.smpessentials.modules.Module;
import com.smpessentials.modules.ModuleManager;
import com.smpessentials.modules.impl.FreelookModule;
import net.minecraft.client.Minecraft;
import net.minecraft.util.ChatComponentText;
import net.minecraft.util.EnumChatFormatting;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;
import net.minecraftforge.fml.common.gameevent.InputEvent;
import org.lwjgl.input.Keyboard;

public class KeybindHandler {

    private final ModuleManager moduleManager;

    public KeybindHandler(ModuleManager moduleManager) {
        this.moduleManager = moduleManager;
    }

    @SubscribeEvent
    public void onKeyPress(InputEvent.KeyInputEvent event) {
        if (Minecraft.getMinecraft().thePlayer == null) return;
        if (Minecraft.getMinecraft().currentScreen != null) return;

        int key = Keyboard.getEventKey();
        if (!Keyboard.getEventKeyState()) return; // Only on key down

        for (Module module : moduleManager.getModules()) {
            // Skip freelook — it uses hold mode, handled in its own tick
            if (module instanceof FreelookModule) continue;

            if (module.getDefaultKey() == key) {
                module.toggle();
                notifyToggle(module);
            }
        }
    }

    private void notifyToggle(Module module) {
        String status = module.isEnabled()
                ? EnumChatFormatting.GREEN + "ON"
                : EnumChatFormatting.RED + "OFF";

        String msg = EnumChatFormatting.GOLD + "[SMP Essentials] " +
                EnumChatFormatting.WHITE + module.getName() + ": " + status;

        Minecraft.getMinecraft().thePlayer.addChatMessage(new ChatComponentText(msg));
    }
}
