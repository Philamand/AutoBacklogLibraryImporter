# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "psnawp",
# ]
# ///
import json
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

        with open("playstation_entitlements.json", "w", encoding="utf-8") as file:
            json.dump(game_entitlements, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
