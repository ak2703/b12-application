import hashlib, hmac, json, urllib.request
from datetime import datetime, timezone

payload = {
    "action_run_link": "https://github.com/ak2703/b12-application/actions/runs/25039908583",
    "email": "contact@akshayvilekar.me",
    "name": "Akshay Vilekar",
    "repository_link": "https://github.com/ak2703/b12-application",
    "resume_link": "https://raw.githubusercontent.com/ak2703/b12-application/main/Akshay_Vilekar_Resume_B12.pdf",
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