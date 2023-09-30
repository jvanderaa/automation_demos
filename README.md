# Plan for Automation Demos

## Set Up Items

For ansible to run:

```
export no_proxy=*
```

## Demo Plan

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

