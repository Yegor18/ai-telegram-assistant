from telegram.ext import Updater
import telegram
print("PTB version:", getattr(telegram,"__version__",None))
print("Has __polling_cleanup_cb?:", "__polling_cleanup_cb" in getattr(Updater,"__slots__",()))