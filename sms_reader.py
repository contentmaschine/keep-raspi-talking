import serial, time, re
import game_state


rgx_index = re.compile('\\+CMTI.*,([0-9]+)')
rgx_defuse = re.compile("defuse", re.I)

port = serial.Serial("/dev/serial0", baudrate=115000, timeout=10.0)
enter = b"\n"

def sms_reader():
    port.write(b"AT+CPIN=2401" + enter)
    time.sleep(0.3)
    if port.read(10).decode("utf-8") == "ERROR":
        raise ValueError("CAN'T ENTER PIN")

    # Disable Echo
    port.write(b'ATE0' + enter)
    time.sleep(0.3)

    # clear any misleading bytes in the buffer
    port.reset_output_buffer()

    while not game_state.sms_done:
        event = port.read(100)
        # port outputs bytes, regex needs string, commands need bytes
        event = event.decode("utf-8")
        #print(event)
        match_object = rgx_index.search(event)
        if match_object is not None:
            sms_index = match_object.group(1)
            sms_index = str.encode(sms_index)
            print(sms_index)
            receive_message(sms_index)
        time.sleep(0.1)
    return True

def receive_message(sms_index):
    # text mode
    port.write(b"AT+CMGF=1" + enter)
    time.sleep(0.3)
    # read sms at index
    port.write(b"AT+CMGR=" + sms_index + enter)
    time.sleep(0.3)
    sms = port.read(1000)
    sms = sms.decode("utf-8")
    #print(sms)
    match_object = rgx_defuse.search(sms)

    if match_object is not None:
        game_state.sms_done = True
    else:
        game_state.strike()
