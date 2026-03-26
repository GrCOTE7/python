import { defineConfig } from "vite";

export default defineConfig({
  root: "./frontend/src",
  build: {
    outDir: "../../static/dist",
    emptyOutDir: true,
    manifest: true,
  },
  server: {
    port: 3000,
    hmr: {
      protocol: "ws",
      host: "localhost",
    },
  },
});
