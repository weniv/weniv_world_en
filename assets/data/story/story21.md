# Rescue Mission

## Rescue Mission `Class` `Data Structure`

The Space Stone, a stone that controls space! Gary received the Space Stone from Licat and opened a portal.

The Frog Tribe, which has been the main labor force supplier in Weniv World, has suffered for a long time under forced labor. Their lives were deeply entrenched in slave-like habits, which was the biggest obstacle Gary faced. He pondered over how to persuade those who were reluctant to change.

> "I'll wield an ax to every tied up chain, ribbit!"

Gary decided to move the tribe members to a safe place to talk. He knew this process wouldn't be easy. Some would resist forced change, and there might even be those who would oppose Gary.

Nevertheless, Gary decided to proceed with the rescue mission.


### Mission
Implement a process to safely move all tribe members to a new environment using Gary's Space Stone. This mission should be solved using one of the data structures, either a 'queue' or a 'stack'. Each tribe member will enter the portal sequentially through the queue.

### Basic Data
```python
class TribeMember:
    pass

class PortalQueue:
    pass

tribe_members = [
    TribeMember('member1'), 
    TribeMember('member2'),
    TribeMember('member3'),
    TribeMember('member4'),
    TribeMember('member5')
]
portal_queue = PortalQueue()

# Create member instances and add to the queue
for member in tribe_members:
    portal_queue.enter_portal(member)

# Transport all tribe members
result = portal_queue.transport_all()
print(result)
```

### Output
```python
'All tribe members were transported safely.'
```

## Hints
```python
class TribeMember:
    # Initialize member and define attribute
    def __init__(self, name):
        self.name = name

class PortalQueue:
    # Initialize portal queue and define member management methods
    def __init__(self):
        self.queue = []

    def enter_portal(self, member):
        # Code to enter a portal
        pass

    def transport_all(self):
        # Code to move all members (check if all 5 members have moved)
        pass
```