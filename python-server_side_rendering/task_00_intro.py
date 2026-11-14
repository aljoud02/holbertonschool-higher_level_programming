#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    """Generates personalized invitation files from a template and lists of attendees.
    """
    # 1. Type validation
    if not isinstance(template, str):
        print(f"Error: template must be a string. Got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries. Got {type(attendees).__name__}.")
        return

    # 2. Empty validation
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Process each attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]
    
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Replace None or empty/missing data with "N/A"
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace(f"{{{placeholder}}}", str(value))
        
        # 4. Generate Output Files
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
