package com.smpessentials.render;

import com.smpessentials.SMPEssentials;
import com.smpessentials.modules.impl.FreelookModule;
import net.minecraftforge.client.event.EntityViewRenderEvent;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;

/**
 * Overrides the camera orientation when Freelook is active.
 * Register this on the Forge event bus separately.
 */
public class FreelookCameraHandler {

    public void register() {
        MinecraftForge.EVENT_BUS.register(this);
    }

    @SubscribeEvent
    public void onCameraSetup(EntityViewRenderEvent.CameraSetup event) {
        FreelookModule freelook = SMPEssentials.instance.getModuleManager().getModule(FreelookModule.class);
        if (freelook == null || !freelook.isActive()) return;

        event.yaw = freelook.getCameraYaw();
        event.pitch = freelook.getCameraPitch();
        event.roll = 0;
    }
}
