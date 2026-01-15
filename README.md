## CI Failure Demo Repo (for testing auto-fix-agent)

### What this is
A tiny repo with a GitHub Actions workflow that **fails on purpose**.
Use it to trigger real `workflow_run` failures and verify your webhook receiver + AI diagnosis.

---

### Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

You should see a failing test.

---

### Trigger a real GitHub Actions failure
1) Create a new GitHub repository (example: `ci-failure-demo`)
2) Push this folder to that repo (as its root)
3) GitHub Actions will run on `push` and fail

---

### Connect to your webhook receiver
In the demo repo (GitHub):
- Settings → Webhooks → Add webhook
- Payload URL: `https://<YOUR_NGROK_HOST>/webhooks/github`
- Content type: `application/json`
- Events: select **Workflow runs**

Now push any commit: you should see `🚨 FAILURE DETECTED` and then `🧠 AI DIAGNOSIS COMPLETE ...` in your agent logs.

---

### Make it pass (optional)
Edit `tests/test_demo.py` and change the failing assertion to a correct one, then push again.


trigger Wed Jan 14 16:12:01 PST 2026
trigger Wed Jan 14 16:17:48 PST 2026
trigger Wed Jan 14 16:20:17 PST 2026
trigger Wed Jan 14 16:23:22 PST 2026
trigger Wed Jan 14 16:28:23 PST 2026
trigger Wed Jan 14 16:36:19 PST 2026
trigger Wed Jan 14 16:36:58 PST 2026
