import time

# Define the segments for each digit
segments = {
    0: ["###", "# #", "# #", "# #", "###"],
    1: ["  #", "  #", "  #", "  #", "  #"],
    2: ["###", "  #", "###", "#  ", "###"],
    3: ["###", "  #", "###", "  #", "###"],
    4: ["# #", "# #", "###", "  #", "  #"],
    5: ["###", "#  ", "###", "  #", "###"],
    6: ["###", "#  ", "###", "# #", "###"],
    7: ["###", "  #", "  #", "  #", "  #"],
    8: ["###", "# #", "###", "# #", "###"],
    9: ["###", "# #", "###", "  #", "###"],
    ":": ["   ", " # ", "   ", " # ", "   "],
}

def display_digit(digit):
    """Display a single digit using the segments"""
    for segment in segments[digit]:
        print(segment)

def display_time():
    """Display the current time in seven-segment display format"""
    current_hour = list(str(time.strftime('%H')))
    current_minute = list(str(time.strftime('%M')))
    current_second = list(str(time.strftime('%S')))
    current_time = current_hour + current_minute + current_second
    
    # convert current_time list to intagers and print in as segment
    for i in current_time:
        display_digit(eval(i))
        print('\n')

    # Wait one second before refreshing the display
    time.sleep(1)
    # Clear the console before refreshing the display
    print("\033c", end="")
    display_time()

# Start displaying the time
display_time()
