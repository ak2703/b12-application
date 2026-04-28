import hashlib, hmac, json, urllib.request
from datetime import datetime, timezone

payload = {
    "action_run_link": "FILL_THIS_AFTER_FIRST_RUN",
    "email": "contact@akshayvilekar.me",
    "name": "Akshay Vilekar",
    "repository_link": "https://github.com/YOUR_USERNAME/b12-application",
    "resume_link": "https://www.akshayvilekar.me",
    "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
secret = b"hello-there-from-b12"
signature = "sha256=" + hmac.new(secret, body, hashlib.sha256).hexdigest()

req = urllib.request.Request(
    "https://b12.io/apply/submission",
    data=body,
    headers={"Content-Type": "application/json", "X-Signature-256": signature},
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(r.read().decode())