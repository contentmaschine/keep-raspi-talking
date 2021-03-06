import game_state, simon_says, wires, sms_reader, morse, lcd_assets
import concurrent.futures, time
import multiprocessing

# TODO:
#  success screen
#  Instructions for Players
#  Board mehr conveniently stecken
#  Simon Says Buttons anmalen

countdown_process = lcd_assets.start_screen()

thread_executor = concurrent.futures.ThreadPoolExecutor()
wires = thread_executor.submit(wires.wires)
simon_says = thread_executor.submit(simon_says.simon_says)

# waits for both games to be finished
if wires.result() and simon_says.result():
    # artistic pause
    time.sleep(1)
    thread_executor.submit(morse.morse, {5: "SMS", 6: "FELIX", 26: "DEFUSE"})
    sms_reader = thread_executor.submit(sms_reader.sms_reader)
    if sms_reader.result():
        lcd_assets.win_screen(countdown_process)
