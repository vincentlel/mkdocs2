import logging
import os

import requests
from pystac_client import Client
from dotenv import load_dotenv

# Logger configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading secrets from environment variables

# Ensure environment variables are set before running this script.
# You can set them in your terminal session or add them permanently to your shell configuration
# (e.g., .bash_profile, .bashrc) using the following format:
#
# export EDS_CLIENT_ID="your_client_id"
# export EDS_SECRET="your_client_secret"
# export EDS_AUTH_URL="your_auth_url"
#
# Alternatively, you can manage environment variables using a .env file and the python-dotenv package.

load_dotenv()

CLIENT_ID = os.getenv("EDS_CLIENT_ID")
CLIENT_SECRET = os.getenv("EDS_SECRET")
EDS_AUTH_URL = os.getenv("EDS_AUTH_URL")
API_URL = "https://api.earthdaily.com/platform/v1/stac"

# Setup requests session
session = requests.Session()
session.auth = (CLIENT_ID, CLIENT_SECRET)


def get_new_token(session):
    """Obtain a new authentication token using client credentials."""
    token_req_payload = {"grant_type": "client_credentials"}
    try:
        token_response = session.post(EDS_AUTH_URL, data=token_req_payload)
        token_response.raise_for_status()
        tokens = token_response.json()
        return tokens["access_token"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to obtain token: {e}")
        raise e


def initialize_stac_client(api_url, token):
    """Initialize and return a configured PySTAC client."""
    return Client.open(api_url, headers={"Authorization": f"Bearer {token}"})


def main():
    token = get_new_token(session)
    client = initialize_stac_client(API_URL, token)

    try:
        # Get all collections
        for collection in client.get_all_collections():
            logger.info(
                f"Retrieved collection: {collection.id} - {collection.description}"
            )

        # Get specific collection
        collection = client.get_collection("sentinel-2-l2a")
        logger.info(
            f"Details of collection '{collection.id}': {collection.description}"
        )

        # Perform a search
        items = client.search(
            collections=["sentinel-2-l2a", "sentinel-2-l1c"],
            datetime="2022-07-01T00:00:00.000000Z/2023-08-01T00:00:00.000000Z",
            intersects={
                "coordinates": [
                    [
                        [-124.18953337119558, 49.734095507050256],
                        [-124.18953337119558, 48.73413273779468],
                        [-121.93408220580699, 48.73413273779468],
                        [-121.93408220580699, 49.734095507050256],
                        [-124.18953337119558, 49.734095507050256],
                    ]
                ],
                "type": "Polygon",
            },
            query={"eo:cloud_cover": {"lt": 10}},
            sortby=[{"field": "properties.eo:cloud_cover", "direction": "asc"}],
            limit=50,
            max_items=100,
        ).items()

        for index, item in enumerate(items):
            logger.info(
                f"Item {index}: ID={item.id}, Cloud Cover={item.properties['eo:cloud_cover']}"
            )

        # Query for specific items
        items = client.search(
            collections=["sentinel-2-l2a"],
            ids=[
                "S2B_35XMG_20230615_1_L2A",
                "S2B_39XVJ_20230615_0_L2A",
                "S2B_27LZJ_20230615_0_L2A",
            ],
        ).items()

        for index, item in enumerate(items):
            logger.info(f"Specific item {index}: ID={item.id}")

        # Query for cloud masks
        items = client.search(
            collections=["sentinel-2-l2a"],
            query={"eda:ag_cloud_mask_available": {"eq": True}},
            max_items=50,
        ).items()

        for index, item in enumerate(items):
            cloud_mask_item = client.get_collection(
                item.properties["eda:ag_cloud_mask_collection_id"]
            ).get_item(item.properties["eda:ag_cloud_mask_item_id"])

            logger.info(
                f"Cloud mask available for item ID={item.id}. Details: {cloud_mask_item.id}"
            )

    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
