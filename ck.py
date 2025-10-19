import sys
import os
import asyncio
import logging
import multiprocessing

# নিশ্চিত করা যে current directory থেকে .so import হবে
sys.path.append(os.path.dirname(__file__))

# ck.so import করা
try:
    import ck  # ck.cpython-312-x86_64-linux-gnu.so
except ImportError:
    print("❌ ck module not found. Make sure .so file is in the same folder.")
    sys.exit(1)

# logging setup
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

def check_status_wrapper():
    """ck module এর check_status ফাংশন run করবে"""
    if hasattr(ck, "check_status"):
        ck.check_status()
    else:
        logging.warning("⚠️ ck module এ check_status function পাওয়া যায়নি!")

async def main_wrapper():
    """ck module এর main coroutine run করবে"""
    if hasattr(ck, "main"):
        await ck.main()
    else:
        logging.warning("⚠️ ck module এ main coroutine পাওয়া যায়নি!")

if __name__ == "__main__":
    multiprocessing.freeze_support()

    # প্রথমে check_status run
    check_status_wrapper()

    # তারপর main coroutine run
    try:
        asyncio.run(main_wrapper())
    except KeyboardInterrupt:
        logging.info("Bot shutting down via KeyboardInterrupt.")
