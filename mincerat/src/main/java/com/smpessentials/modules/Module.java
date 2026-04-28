package com.smpessentials.modules;

import org.lwjgl.input.Keyboard;

public abstract class Module {

    private final String name;
    private final String description;
    private final int defaultKey;
    private boolean enabled;

    public Module(String name, String description, int defaultKey) {
        this.name = name;
        this.description = description;
        this.defaultKey = defaultKey;
        this.enabled = false;
    }

    public void toggle() {
        enabled = !enabled;
        if (enabled) {
            onEnable();
        } else {
            onDisable();
        }
    }

    protected void onEnable() {}
    protected void onDisable() {}

    public String getName() { return name; }
    public String getDescription() { return description; }
    public int getDefaultKey() { return defaultKey; }
    public boolean isEnabled() { return enabled; }
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}
