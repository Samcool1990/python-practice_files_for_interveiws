import schedule
import time
from datetime import datetime
import pytz
import os

def process_files():
    """
    Function to process files - customize this function according to your needs
    """
    print(f"Processing files at {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')}")
    # Add your file processing logic here
    # For example:
    # - Read files from a directory
    # - Process the files
    # - Save results
    pass

def schedule_monday_processing():
    """
    Schedule the file processing task to run every Monday before 10:00 AM IST
    """
    # Set the timezone to IST
    ist = pytz.timezone('Asia/Kolkata')
    
    # Schedule the job to run every Monday at 9:30 AM IST
    schedule.every().monday.at("09:30").do(process_files)
    
    print("Scheduled file processing for every Monday at 9:30 AM IST")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    try:
        schedule_monday_processing()
    except KeyboardInterrupt:
        print("\nScheduler stopped by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}") 