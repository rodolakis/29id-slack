import time
from epics import PV
from slackaps import log

def check_pvs_connected(epics_pvs):
    """Checks whether all EPICS PVs are connected.
    Returns
    -------
    bool
        True if all PVs are connected, otherwise False.
    """

    slack_messages = ()
    all_connected = True

    for key in epics_pvs:
        pv = PV(epics_pvs[key])
        time.sleep(.1)
        if not pv.connected:
            log.error('PV %s is not connected', pv.pvname)
            slack_messages += ('\nPV ' + pv.pvname + ' is not connected', )
            all_connected = False
        else:
            log.info('%s: %s' % (key, pv.get(as_string=True)))
            slack_messages += ('\n' + key + ': ' + pv.get(as_string=True), )

    return all_connected, slack_messages

