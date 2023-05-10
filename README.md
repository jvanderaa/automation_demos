# Plan for Automation Day 2023

## Set Up Items

For ansible to run:

```
export no_proxy=*
```

## Demo Plan

- Regions [Possible cut]
- Sites
  - Site Overview Page: https://automationday.josh-v.com/dcim/sites/site01/?tab=main
- Devices
  - https://automationday.josh-v.com/dcim/devices/dc766d41-bae3-42f2-877b-a9838022ee06/?tab=main
- Tags
- Status - Custom status
- Racks + Elevations [Possible cut]
- Manufacturers | Device Types | Devices | Roles -> Powerful
- Platforms -> OS [Possible cut]
- IPAM -> Relationships
- Circuits
- Extensibility
  - Custom Fields [Possible cut]
  - Job Results
    - RBAC
    - Logging
    - Scheduling
    - Centralized Scripts execution, known environment
  - ChangeLog [Possible cut]
- Config Contexts (Review via the following GraphQL Query, device page where it is all getting the data from if demo.nautobot.com)
```
{
  devices(tag: "demo-golden-config") {
    name
    config_context
  }
}
```
- Apps
  - Show APIs interface, how to dive in
- Golden Configuration
  - 5 Set up items
    - Compliance Rules  [Possible cut]
    - Compliance Features  [Possible cut]
    - Config Removals  [Possible cut]
    - Config Replacements  [Possible cut]
    - Settings  [Possible cut]
  - Reports Overview
  - Device Detail
- DLM
  - Show hardware end of life report
- Circuit Maintenance
  - Show the circuit maintenances
  - The relationship that is built for circuits
  - Find sites with Overlapping maintenance

## Automation Focused Demos

### Get next available address (Ansible Playbook)

```
ansible-playbook get_and_set_next_available.yml
```

### Ansible Inventory demonstrations

Demonstration of GraphQL vs REST Inventories. Show the groupings based on data in Nautobot. Sites & Device Types & Roles

```
ansible-inventory -i graphql_inventory.yml --list
```

```
ansible-inventory -i rest_inventory.yml --list 
```

### Nornir (pynautobot Example)

Gathers primary IP address from Nautobot and prints out a message.

```
python nornir_example.py
```

