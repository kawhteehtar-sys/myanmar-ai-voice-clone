# Myanmar AI Voice Studio — Backend starter

This is a secure backend foundation, not a finished AI voice engine.

## Deploy on Render
1. Push this folder and `render.yaml` to your GitHub repository.
2. In Render, choose **New → Blueprint** and connect the repository.
3. Render creates `myanmar-ai-voice-api`. It generates `APP_TOKEN` automatically.
4. Set `FRONTEND_ORIGIN` to the exact URL of your frontend.
5. Check `https://YOUR-RENDER-SERVICE.onrender.com/health`.

## Important
- `/api/tts` and `/api/voice-clone` deliberately return 501 until a real provider is connected.
- Do not put provider API keys in `index.html`.
- A public frontend cannot keep a shared secret hidden. For personal-only use, add sign-in/authentication before exposing the service.
- Voice cloning must only be used with the speaker's permission.
