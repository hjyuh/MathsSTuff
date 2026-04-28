package com.smpessentials;

import com.smpessentials.modules.ModuleManager;
import com.smpessentials.render.FreelookCameraHandler;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;

@Mod(modid = SMPEssentials.MODID, name = SMPEssentials.NAME, version = SMPEssentials.VERSION)
public class SMPEssentials {

    public static final String MODID = "smpessentials";
    public static final String NAME = "SMP Essentials";
    public static final String VERSION = "1.0.0";

    @Mod.Instance(MODID)
    public static SMPEssentials instance;

    private ModuleManager moduleManager;

    @Mod.EventHandler
    public void preInit(FMLPreInitializationEvent event) {
        moduleManager = new ModuleManager();
    }

    @Mod.EventHandler
    public void init(FMLInitializationEvent event) {
        moduleManager.registerAll();
        MinecraftForge.EVENT_BUS.register(new KeybindHandler(moduleManager));
        MinecraftForge.EVENT_BUS.register(moduleManager);
        new FreelookCameraHandler().register();
        System.out.println("[SMP Essentials] Loaded " + moduleManager.getModules().size() + " modules.");
    }

    public ModuleManager getModuleManager() {
        return moduleManager;
    }
}
