import spx

# 1. check_access ကို အမြဲ True ဖြစ်အောင် ပြင်ခြင်း
def patched_check_access(self):
    print(f"\n{spx.G}[✓] Key System Bypassed Successfully!{spx.w}")
    return True

# 2. _get_hwid ကို မလိုလားအပ်သော စစ်ဆေးမှုများမလုပ်အောင် ပြင်ခြင်း
def patched_get_hwid(self):
    return "BYPASSED_HWID"

# Patch လုပ်ခြင်း (မူရင်း class ၏ method များကို အစားထိုးခြင်း)
spx.AuthManager.check_access = patched_check_access
spx.AuthManager._get_hwid = patched_get_hwid

if __name__ == '__main__':
    # မူရင်းဖိုင်ထဲက start() function ကို ခေါ်ခြင်း
    spx.start()
