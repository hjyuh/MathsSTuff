package com.smpessentials.modules;

import com.smpessentials.modules.impl.*;
import net.minecraftforge.client.event.RenderGameOverlayEvent;
import net.minecraftforge.client.event.RenderWorldLastEvent;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.fml.common.eventhandler.SubscribeEvent;
import net.minecraftforge.fml.common.gameevent.TickEvent;

import java.util.ArrayList;
import java.util.List;

public class ModuleManager {

    private final List<Module> modules = new ArrayList<>();

    public void registerAll() {
        // v1 modules
        modules.add(new FullbrightModule());
        modules.add(new CoordinatesHUDModule());
        modules.add(new MobESPModule());
        modules.add(new FreelookModule());
        modules.add(new DeathWaypointsModule());

        // v1.1 modules
        modules.add(new FPSModule());
        modules.add(new CPSModule());
        modules.add(new FreecamModule());
        modules.add(new AutoSprintModule());
    }

    public List<Module> getModules() {
        return modules;
    }

    @SuppressWarnings("unchecked")
    public <T extends Module> T getModule(Class<T> clazz) {
        for (Module m : modules) {
            if (clazz.isInstance(m)) {
                return (T) m;
            }
        }
        return null;
    }

    public Module getModuleByName(String name) {
        for (Module m : modules) {
            if (m.getName().equalsIgnoreCase(name)) {
                return m;
            }
        }
        return null;
    }

    // ── Event forwarding ──────────────────────────────────

    @SubscribeEvent
    public void onRenderOverlay(RenderGameOverlayEvent.Post event) {
        if (event.type != RenderGameOverlayEvent.ElementType.TEXT) return;

        for (Module m : modules) {
            if (m.isEnabled() && m instanceof RenderableHUD) {
                ((RenderableHUD) m).onRenderHUD(event);
            }
        }
    }

    @SubscribeEvent
    public void onRenderWorld(RenderWorldLastEvent event) {
        for (Module m : modules) {
            if (m.isEnabled() && m instanceof RenderableWorld) {
                ((RenderableWorld) m).onRenderWorld(event);
            }
        }
    }

    @SubscribeEvent
    public void onClientTick(TickEvent.ClientTickEvent event) {
        if (event.phase != TickEvent.Phase.END) return;

        for (Module m : modules) {
            if (m.isEnabled() && m instanceof Tickable) {
                ((Tickable) m).onTick();
            }
        }
    }

    @SubscribeEvent
    public void onDeath(LivingDeathEvent event) {
        for (Module m : modules) {
            if (m.isEnabled() && m instanceof DeathListener) {
                ((DeathListener) m).onDeath(event);
            }
        }
    }

    // ── Module capability interfaces ──────────────────────

    public interface RenderableHUD {
        void onRenderHUD(RenderGameOverlayEvent.Post event);
    }

    public interface RenderableWorld {
        void onRenderWorld(RenderWorldLastEvent event);
    }

    public interface Tickable {
        void onTick();
    }

    public interface DeathListener {
        void onDeath(LivingDeathEvent event);
    }
}
