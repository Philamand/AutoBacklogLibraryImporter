# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "psnawp",
# ]
# ///
import json
import httpx
from psnawp_api import PSNAWP


NPSSO = ""


def main():
    try:
        psnawp = PSNAWP(NPSSO)
        client = psnawp.me()

        game_entitlements = []

        for game_entitlement in client.game_entitlements():
            print(game_entitlement)
            game_entitlements.append(game_entitlement)

        headers = {
            "apollographql-client-name": "PlayStationApp-Android",
            "content-type": "application/json",
            "Authorization": f"Bearer {client.authenticator.token_response['access_token']}",
        }

        r = httpx.get(
            'https://m.np.playstation.com/api/graphql/v1/op?operationName=metGetStoreWishlist&variables={}&extensions={"persistedQuery":{"version":1,"sha256Hash":"571149e8aa4d76af7dd33b92e1d6f8f828ebc5fa8f0f6bf51a8324a0e6d71324"}}',
            headers=headers,
        )
        for entry in r.json()["data"]["storeWishlist"]:
            try:
                title_id = entry["id"].split("-")[1]
                platform_id = "ps5"
                if "PS5" not in entry["platforms"]:
                    platform_id = "ps4"
                game_entitlements.append(
                    {
                        "conceptMeta": {"conceptId": "0"},
                        "entitlementAttributes": [
                            {
                                "entitlementKeyFlag": True,
                                "platformId": platform_id,
                                "placeholderFlag": False,
                            }
                        ],
                        "entitlementType": 5,
                        "featureType": 1,
                        "id": entry["id"],
                        "isConsumable": False,
                        "platformId": platform_id,
                        "productId": entry["id"],
                        "rewardMeta": {"retentionPolicy": -1},
                        "skuId": entry["id"],
                        "titleMeta": {"name": entry["name"], "titleId": title_id},
                    }
                )
            except Exception as e:
                print(e)

        with open("playstation_entitlements.json", "w", encoding="utf-8") as file:
            json.dump(game_entitlements, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
