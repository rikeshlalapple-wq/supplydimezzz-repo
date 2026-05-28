import os
import sys
import time
import random
from datetime import datetime

def run_matrix_clock():
    # Matrix-green style text formatting
    GREEN = "\033[32m"
    BRIGHT_GREEN = "\033[1;32m"
    WHITE = "\033[1;37m"
    RESET = "\033[0m"
    
    # Try to dynamically detect terminal width, default to 40
    try:
        columns = os.get_terminal_size().columns
    except Exception:
        columns = 40

    # Initialize falling column tracks
    tracks = [0] * columns
    
    print("\033[2J") # Clear screen cleanly
    print(f"{GREEN}[*] Matrix Time Stream Initialized. Press CTRL+C to close session.{RESET}\n")
    time.sleep(1.5)

    try:
        while True:
            # Generate the scrolling digital rain rows
            row = []
            current_time = datetime.now().strftime("  %H:%M:%S  ")
            
            for col in range(columns):
                # Randomly determine stream flow behavior
                if tracks[col] == 0:
                    if random.random() > 0.98:
                        tracks[col] = random.randint(5, 15) # Length of code stream
                
                if tracks[col] > 0:
                    # Make the leading edge of the stream bright white
                    if tracks[col] == 1:
                        row.append(f"{WHITE}{random.randint(0, 9)}{RESET}")
                    else:
                        row.append(f"{GREEN}{random.randint(0, 9)}{RESET}")
                    tracks[col] -= 1
                else:
                    row.append(" ")
            
            # Splice the live system clock cleanly right into the center row
            print_row = "".join(row)
            if random.random() > 0.85:
                mid = columns // 2
                start = mid - (len(current_time) // 2)
                end = start + len(current_time)
                print_row = print_row[:start] + f"{BRIGHT_GREEN}[{current_time.strip()}]{RESET}" + print_row[end:]

            sys.stdout.write(print_row + "\n")
            sys.stdout.flush()
            time.sleep(0.06) # Smooth, steady frame drop rate
            
    except KeyboardInterrupt:
        print(f"\n{GREEN}[!] Visualizer suspended cleanly. Stream closed.{RESET}\n")

if __name__ == "__main__":
    run_matrix_clock()
