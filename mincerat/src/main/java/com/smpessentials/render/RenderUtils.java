package com.smpessentials.render;

import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.FontRenderer;
import net.minecraft.client.renderer.GlStateManager;
import net.minecraft.client.renderer.Tessellator;
import net.minecraft.client.renderer.WorldRenderer;
import net.minecraft.client.renderer.entity.RenderManager;
import net.minecraft.client.renderer.vertex.DefaultVertexFormats;
import net.minecraft.entity.Entity;
import net.minecraft.util.AxisAlignedBB;
import org.lwjgl.opengl.GL11;

import java.awt.Color;

public class RenderUtils {

    /**
     * Draws a bounding box around an entity in world space.
     */
    public static void drawEntityBoundingBox(Entity entity, Color color, float partialTicks) {
        RenderManager rm = Minecraft.getMinecraft().getRenderManager();

        double x = entity.lastTickPosX + (entity.posX - entity.lastTickPosX) * partialTicks - rm.viewerPosX;
        double y = entity.lastTickPosY + (entity.posY - entity.lastTickPosY) * partialTicks - rm.viewerPosY;
        double z = entity.lastTickPosZ + (entity.posZ - entity.lastTickPosZ) * partialTicks - rm.viewerPosZ;

        float halfWidth = entity.width / 2.0f;
        AxisAlignedBB box = new AxisAlignedBB(
            x - halfWidth, y, z - halfWidth,
            x + halfWidth, y + entity.height, z + halfWidth
        );

        drawBoundingBox(box, color);
    }

    /**
     * Draws a wireframe box.
     */
    public static void drawBoundingBox(AxisAlignedBB bb, Color color) {
        GlStateManager.pushMatrix();
        GlStateManager.enableBlend();
        GlStateManager.disableTexture2D();
        GlStateManager.disableDepth();
        GlStateManager.tryBlendFuncSeparate(GL11.GL_SRC_ALPHA, GL11.GL_ONE_MINUS_SRC_ALPHA, 1, 0);
        GL11.glLineWidth(2.0f);

        float r = color.getRed() / 255f;
        float g = color.getGreen() / 255f;
        float b = color.getBlue() / 255f;
        float a = color.getAlpha() / 255f;

        Tessellator tess = Tessellator.getInstance();
        WorldRenderer wr = tess.getWorldRenderer();

        wr.begin(GL11.GL_LINE_STRIP, DefaultVertexFormats.POSITION_COLOR);

        // Bottom face
        wr.pos(bb.minX, bb.minY, bb.minZ).color(r, g, b, a).endVertex();
        wr.pos(bb.maxX, bb.minY, bb.minZ).color(r, g, b, a).endVertex();
        wr.pos(bb.maxX, bb.minY, bb.maxZ).color(r, g, b, a).endVertex();
        wr.pos(bb.minX, bb.minY, bb.maxZ).color(r, g, b, a).endVertex();
        wr.pos(bb.minX, bb.minY, bb.minZ).color(r, g, b, a).endVertex();

        // Top face
        wr.pos(bb.minX, bb.maxY, bb.minZ).color(r, g, b, a).endVertex();
        wr.pos(bb.maxX, bb.maxY, bb.minZ).color(r, g, b, a).endVertex();
        wr.pos(bb.maxX, bb.maxY, bb.maxZ).color(r, g, b, a).endVertex();
        wr.pos(bb.minX, bb.maxY, bb.maxZ).color(r, g, b, a).endVertex();
        wr.pos(bb.minX, bb.maxY, bb.minZ).color(r, g, b, a).endVertex();

        tess.draw();

        // Vertical edges
        wr.begin(GL11.GL_LINES, DefaultVertexFormats.POSITION_COLOR);
        wr.pos(bb.maxX, bb.minY, bb.minZ).color(r, g, b, a).endVertex();
        wr.pos(bb.maxX, bb.maxY, bb.minZ).color(r, g, b, a).endVertex();

        wr.pos(bb.maxX, bb.minY, bb.maxZ).color(r, g, b, a).endVertex();
        wr.pos(bb.maxX, bb.maxY, bb.maxZ).color(r, g, b, a).endVertex();

        wr.pos(bb.minX, bb.minY, bb.maxZ).color(r, g, b, a).endVertex();
        wr.pos(bb.minX, bb.maxY, bb.maxZ).color(r, g, b, a).endVertex();

        tess.draw();

        GlStateManager.enableDepth();
        GlStateManager.enableTexture2D();
        GlStateManager.disableBlend();
        GlStateManager.popMatrix();
    }

    /**
     * Draws a waypoint beacon at a position in world space.
     */
    public static void drawWaypointBeacon(double x, double y, double z, Color color, String label, float partialTicks) {
        RenderManager rm = Minecraft.getMinecraft().getRenderManager();

        double renderX = x - rm.viewerPosX;
        double renderY = y - rm.viewerPosY;
        double renderZ = z - rm.viewerPosZ;

        // Draw the beacon line from y=0 to y=256
        GlStateManager.pushMatrix();
        GlStateManager.enableBlend();
        GlStateManager.disableTexture2D();
        GlStateManager.disableDepth();
        GlStateManager.tryBlendFuncSeparate(GL11.GL_SRC_ALPHA, GL11.GL_ONE_MINUS_SRC_ALPHA, 1, 0);
        GL11.glLineWidth(2.0f);

        float r = color.getRed() / 255f;
        float g = color.getGreen() / 255f;
        float b = color.getBlue() / 255f;

        Tessellator tess = Tessellator.getInstance();
        WorldRenderer wr = tess.getWorldRenderer();

        wr.begin(GL11.GL_LINES, DefaultVertexFormats.POSITION_COLOR);
        wr.pos(renderX + 0.5, -rm.viewerPosY, renderZ + 0.5).color(r, g, b, 0.5f).endVertex();
        wr.pos(renderX + 0.5, 256 - rm.viewerPosY, renderZ + 0.5).color(r, g, b, 0.5f).endVertex();
        tess.draw();

        GlStateManager.enableDepth();
        GlStateManager.enableTexture2D();
        GlStateManager.disableBlend();
        GlStateManager.popMatrix();

        // Draw label
        if (label != null && !label.isEmpty()) {
            drawWorldText(label, renderX + 0.5, renderY + 1.5, renderZ + 0.5);
        }
    }

    /**
     * Renders text at a position in world space (billboard style).
     */
    public static void drawWorldText(String text, double x, double y, double z) {
        Minecraft mc = Minecraft.getMinecraft();
        FontRenderer fr = mc.fontRendererObj;
        RenderManager rm = mc.getRenderManager();

        GlStateManager.pushMatrix();
        GlStateManager.translate(x, y, z);

        // Billboard: always face the camera
        GlStateManager.rotate(-rm.playerViewY, 0, 1, 0);
        GlStateManager.rotate(rm.playerViewX, 1, 0, 0);

        float scale = 0.025f;
        GlStateManager.scale(-scale, -scale, scale);

        GlStateManager.disableDepth();
        GlStateManager.enableBlend();

        int halfWidth = fr.getStringWidth(text) / 2;

        // Background
        net.minecraft.client.gui.Gui.drawRect(-halfWidth - 2, -2, halfWidth + 2, fr.FONT_HEIGHT + 1, 0x80000000);

        fr.drawStringWithShadow(text, -halfWidth, 0, 0xFFFFFF);

        GlStateManager.enableDepth();
        GlStateManager.disableBlend();
        GlStateManager.popMatrix();
    }
}
