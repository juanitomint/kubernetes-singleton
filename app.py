import time
import os

LOCK_FILE_PATH = '/config/lock'
INSTANCE_ID = os.getenv('HOSTNAME', 'default-instance')

def acquire_lock():
    while True:
        try:
            with open(LOCK_FILE_PATH, 'r') as f:
                lock_status = f.read().strip()
            if lock_status == "free":
                with open(LOCK_FILE_PATH, 'w') as f:
                    f.write(INSTANCE_ID)
                print(f"Lock acquired by {INSTANCE_ID}")
                return True
            else:
                print(f"Lock is held by {lock_status}. Retrying...")
        except Exception as e:
            print(f"Exception when reading/writing lock file: {e}")
        time.sleep(5)

def release_lock():
    try:
        with open(LOCK_FILE_PATH, 'r') as f:
            lock_status = f.read().strip()
        if lock_status == INSTANCE_ID:
            with open(LOCK_FILE_PATH, 'w') as f:
                f.write("free")
            print(f"Lock released by {INSTANCE_ID}")
    except Exception as e:
        print(f"Exception when reading/writing lock file: {e}")

if __name__ == "__main__":
    try:
        if acquire_lock():
            # Perform the singleton task here
            print(f"{INSTANCE_ID} is performing the singleton task")
            while True:
                time.sleep(10)  # Keep the lock as long as the task is running
    except KeyboardInterrupt:
        release_lock()
