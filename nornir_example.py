"""Testing file."""
# pylint: disable=duplicate-code
import os
from nornir import InitNornir
from nornir.core.task import Task, Result

# Disabling pylint for example
from nornir_utils.plugins.functions import print_result  # pylint: disable=import-error
import pynautobot

QUERY_STRING = """
query ($device_name:[String]) {
  devices(name: $device_name) {
    primary_ip4 {
      address
    }
  }
}
"""


def hello_world(task: Task, nautobot: pynautobot.api) -> Result:
    """Example to show work inside of a task.

    Args:
        task (Task): Nornir Task

    Returns:
        Result: Nornir result
    """
    # Get the default IP address
    variables = {"device_name": task.host.name}
    graph_response = nautobot.graphql.query(
        query=QUERY_STRING, variables=variables
    ).json

    return Result(
        host=task.host,
        result=f"{task.host.name} says hello world with IP: {graph_response['data']['devices'][0]['primary_ip4']['address']}",
    )


def main():
    """Nornir testing."""
    site = ["site01", "site02"]

    my_nornir = InitNornir(
        inventory={
            "plugin": "NautobotInventory",
            "options": {
                "nautobot_url": os.getenv("NAUTOBOT_URL"),
                "nautobot_token": os.getenv("NAUTBOT_TOKEN"),
                "filter_parameters": {"site": site},
                "ssl_verify": True,
            },
        },
    )

    print(f"Hosts found: {len(my_nornir.inventory.hosts)}")
    # Print out the keys for the inventory
    print(my_nornir.inventory.hosts.keys())

    # Build the pynautobot object
    nautobot = pynautobot.api(
        url=os.getenv("NAUTOBOT_URL"), token=os.getenv("NAUTOBOT_TOKEN")
    )

    result = my_nornir.run(task=hello_world, nautobot=nautobot)
    print_result(result)


if __name__ == "__main__":
    main()
