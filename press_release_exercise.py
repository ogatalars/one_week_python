press_release = """

Doody Calls, a nationwide leader in dog poop removal services, 
is growing its footprint in the pooper scooper industry with the opening of an office in Orlando, Florida. 
Doody Calls currently cleans up dog poop in over 57 territories across 23 states and 
has been named the number-one dog poop removal franchise in the United States by Entrepreneur Magazine's annual Franchise 500 list.

"""

# # Remove the leading and trailing whitespace (new lines) from press_release


# # Replace the phrase "dog poop" with "pet waste" in the press release.  Our research shows "pet phrase" tests better than "dog poop"


# # We changed our company name! replace the phrase "Doody Calls" with "DoodyCalls" (no space between the words)


# # Our research shows that it's best to shout our press releases. Make the entire press release uppercased!

# # Print out the updated press release with all of the above changes:

white_space = press_release.strip()
replace1 = white_space.replace("dog poop", "pet waste")
replace2 = replace1.replace("Doody Calls", "DoodyCalls")
final_press = press_release.upper()
print(final_press)