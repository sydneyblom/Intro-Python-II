# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser

# Create a file called `item.py` and add an `Item` class in there.
#   The item should have `name` and `description` attributes.
#      * Hint: the name should be one word for ease in parsing later.
#   This will be the _base class_ for specialized item types to be declared later.
class Item:
    def __init__(self, i_name=sword, i_description):
        self.i_name = i_name
        self.i_description = i_description
    def __repr__(self):
        return f"{self.i_name}, {self.i_description}