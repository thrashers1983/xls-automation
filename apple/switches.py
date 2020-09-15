import os


def acc_stat(store_no):
    devices = []
    ws_c3560cx_12tc_s = 0
    ws_c3560cx_12pc_s = 0
    ws_c3560cx_8pc_s = 0
    ws_c3560_12pc_s = 0
    ws_c3560_8pc_s = 0
    c2960 = 0
    store = {}
    output = os.popen(f"capri devices fqdn='^{store_no}.*' deviceState='!DECOMMISSIONED' "
                      f"--fields=fqdn,model | grep acc | grep -v fd")
    for device in output:
        devices.append(device.strip())
    total = len(devices)
    for device in devices:
        if 'WS-C3560CX-12TC-S' in device:
            ws_c3560cx_12tc_s += 1
        elif 'WS-C3560CX-12PC-S' in device:
            ws_c3560cx_12pc_s += 1
        elif 'WS-C3560CX-8PC-S' in device:
            ws_c3560cx_8pc_s += 1
        elif 'WS-C3560-12PC-S' in device:
            ws_c3560_12pc_s += 1
        elif 'WS-C3560-8PC-S' in device:
            ws_c3560_8pc_s += 1
        elif '2960' in device:
            c2960 += 1
    ratio = c2960/total
    store['store'] = store_no
    store['acc-sw QTY'] = total
    store['WS-C3560CX-12TC-S'] = ws_c3560cx_12tc_s
    store['WS-C3560CX-12PC-S'] = ws_c3560cx_12pc_s
    store['WS-C3560CX-8PC-S'] = ws_c3560cx_8pc_s
    store['WS-C3560-12PC-S'] = ws_c3560_12pc_s
    store['WS-C3560-8PC-S'] = ws_c3560_8pc_s
    store['C2960'] = c2960
    store['C2960 ratio'] = ratio
    return store


def core_stat(store_no):
    devices = []
    store = {}
    store['store'] = store_no
    output = os.popen(f"capri devices fqdn='^{store_no}.*' deviceState='!DECOMMISSIONED' "
                      f"--fields=fqdn,model |  grep -E 'core-sw|srv-sw|rsr-sw'")
    for device in output:
        devices.append(device.strip())
    for device in devices:
        if 'core-sw1' in device:
            _, model = device.split(',')
            store['core-sw1'] = model
        elif 'core-sw2' in device:
            _, model = device.split(',')
            store['core-sw2'] = model
        elif 'srv-sw1' in device:
            _, model = device.split(',')
            store['srv-sw1'] = model
        elif 'rsr-sw1' in device:
            _, model = device.split(',')
            store['rsr-sw1'] = model
        elif 'rsr-sw2' in device:
            _, model = device.split(',')
            store['rsr-sw2'] = model
        elif 'rsr-sw3' in device:
            _, model = device.split(',')
            store['rsr-sw3'] = model
        else:
            fqdn, model = device.split(',')
            store[fqdn] = model
    return store
