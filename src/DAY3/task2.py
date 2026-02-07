# Create a tuple for screen resolution
screen_res = (1920, 1080)

# Print current resolution
print("Current Resolution:", str(screen_res[0]) + "x" + str(screen_res[1]))

# The Experiment (This will cause an error if you run it)
#screen_res[0] = 1280   # Uncomment to see: TypeError: 'tuple' object does not support item assignment

# The Fix
print("Tuples cannot be modified!")
