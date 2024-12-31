#Messaging system in Python

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.receiver.username}\nMessage: {self.content}"


class User:
    def __init__(self, username):
        self.username = username
        self.inbox = []

    def send_message(self, receiver, content, messaging_system):
        message = Message(self.username, receiver, content)
        messaging_system.add_message(message)
        print(f"Message sent from {self.username} to {receiver.username}.")

    def view_inbox(self):
        if not self.inbox:
            print(f"{self.username}'s inbox is empty.")
        else:
            print(f"{self.username}'s Inbox:")
            for i, message in enumerate(self.inbox, 1):
                print(f"\nMessage {i}:\n{message}")


class MessagingSystem:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        message.receiver.inbox.append(message)


# Example usage:
if __name__ == "__main__":
    # Initialize messaging system
    system = MessagingSystem()

    # Create users
    alice = User("Alice")
    bob = User("Bob")

    # Send messages
    alice.send_message(bob, "Hello, Bob! How are you?", system)
    bob.send_message(alice, "Hi Alice! I'm good, thank you!", system)

    # View inboxes
    alice.view_inbox()
    bob.view_inbox()

#Question: If there are backup of database should you consider restoring ?
# Answer: Restoring a database from a backup is a critical decision and should be considered only after 
# evaluating specific factors. Below are key considerations:

# 1. When to Consider Restoring
# Data Loss: If important data is lost due to accidental deletion, corruption, or hardware failure.
# Security Breach: If the database is compromised, and the integrity of the data is questionable.
# System Failure: When a critical system failure renders the database unusable.
# Testing/Recovery: To test disaster recovery processes or migrate data to a new environment.
# Rollback: If a deployment, migration, or update goes wrong and the system needs to revert to a previous 
# stable state.


# 2. Factors to Evaluate Before Restoring
# Root Cause: Identify and address the reason for failure or corruption to prevent recurrence.
# Backup Integrity: Ensure the backup is complete, uncorrupted, and up-to-date.
# Impact Assessment: Assess the impact of restoring, such as data consistency, downtime, and rollback of 
# recent changes.
# Data Currency: Determine how much data (transactions, updates) will be lost post-restoration due to the 
# time gap between the backup and the current state.


# 3. Best Practices for Restoration
# Test First: Always test the backup on a staging or test environment to verify its validity.
# Communicate: Inform stakeholders about the restoration process and its implications.
# Backup Before Restoring: Create a backup of the current state (even if corrupted) for forensic analysis or 
# rollback if needed.
# Downtime Planning: Schedule the restoration during low-traffic periods to minimize user impact.
# Data Validation: Validate the restored data for completeness and correctness.
# Incremental Restoration: If possible, restore incrementally to minimize downtime and allow for quicker 
# recovery of critical data.


# 4. Alternatives to Restoration
# Repair: Attempt to repair the database using built-in tools or scripts.
# Point-in-Time Recovery: Use point-in-time recovery (if available) to restore only specific parts of the 
# database.
# Partial Restore: Restore specific tables, schemas, or sections instead of the entire database.
# Audit Logs: Rebuild lost or corrupted data using logs or change records.



# 5. Risks of Restoration
# Data Loss: Transactions after the backup timestamp will be lost unless they can be re-entered or reprocessed.
# Downtime: The restoration process may lead to extended unavailability of the system.
# Incompatibility: The backup may not be compatible with the current system state or schema changes.
# Failed Restoration: Backup files might be corrupted or incomplete, leading to a failed restore.



# Decision-Making Matrix
# Scenario	Restore Backup?	Alternative Actions
# Minor data corruption	No	Attempt repair or restore specific objects.
# Large-scale corruption	Yes	Validate backup and perform a full restore.
# Recent accidental deletion	Maybe	Consider point-in-time recovery or partial restore.
# Post-deployment failure	Yes	Rollback to the previous state using backups.
# Security breach	Yes	Restore, but first secure the system.
# By evaluating these factors and following best practices, you can decide if restoring a database from a 
# backup is the most appropriate action.




# What is the difference between AWS Lambda & AWS EC2




# Develop a python function which takes a string as a parameter, it returns either True or False depending on whether its a  balanced string or not.
# Examples of a balanced string: (True cases)
# (hello world)
# (hello (world))
# Examples of False cases
# (hello (world)
# )hello (world)

def parenthesis_balanced(s):
    stack = []
    opening = "("
    closing = ")"
    
    for char in s:
        if char in opening:
            stack.append(char)
            
        if char in closing:
            if not stack:
                return False
            if opening.index(stack.pop()) != closing.index(char):
                return False
    return not stack
    
print(parenthesis_balanced("(hello (world))"))
print(parenthesis_balanced("(hello (world)"))      