"""Small code change for validating delivery from a real Git push.

Run with: python3 webhook_push_smoke_test.py
This script makes no network requests and contains no webhook credentials.
The Git push of this file, not execution of this script, triggers the webhook.
"""
import json


def smoke_test_result():
    return {
        "test": "real-git-push-webhook",
        "repository": "hswell/test1",
        "expected_event": "push",
        "ok": True,
    }


if __name__ == "__main__":
    print(json.dumps(smoke_test_result(), sort_keys=True))
