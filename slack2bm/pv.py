from epics import PV
import log

def pv2bm(tomoscan_prefix, ad_prefix, fp_prefix):
    
    pvs = {}

    # Ring
    pvs['Current']                 = PV('S:SRcurrentAI')
    pvs['ShutterStatus']           = PV('PA:02BM:STA_A_FES_OPEN_PL')
    pvs['BeamReady']               = PV('ACIS:ShutterPermit')

    # EPS
    pvs['Fault:Temp:M1']           = PV('2bm:Fault:Temp:M1')
    pvs['Fault:Helium_Flow']       = PV('2bm:Fault:Helium_Flow')
    pvs['Fault:Water:P6_Shutter']  = PV('2bm:Fault:Water:P6_Shutter')
    pvs['Fault:Water:DMM']         = PV('2bm:Fault:Water:DMM')
    pvs['Fault:Water:BMA_Window']  = PV('2bm:Fault:Water:BMA_Window')
    pvs['Fault:Water:M1']          = PV('2bm:Fault:Water:M1')
    pvs['Fault:Water:FilterSlits'] = PV('2bm:Fault:Water:FilterSlits')
    pvs['Vacuum:BMB_Slits']        = PV('2bm:Vacuum:BMB_Slits')
    pvs['Vacuum:Mini_Hutch_2']     = PV('2bm:Vacuum:Mini_Hutch_2')
    pvs['Vacuum:Mini_Hutch_1']     = PV('2bm:Vacuum:Mini_Hutch_1')
    pvs['Vacuum:P6_Shutter']       = PV('2bm:Vacuum:P6_Shutter')
    pvs['Vacuum:DMM']              = PV('2bm:Vacuum:DMM')
    pvs['Vacuum:M1']               = PV('2bm:Vacuum:M1')
    pvs['Vacuum:FilterSlits']      = PV('2bm:Vacuum:FilterSlits')

    # User info
    pvs['user_name']               = PV(tomoscan_prefix + 'UserName')
    pvs['user_last_name']          = PV(tomoscan_prefix + 'UserLastName')
    pvs['user_affiliation']        = PV(tomoscan_prefix + 'UserInstitution')
    pvs['user_badge']              = PV(tomoscan_prefix + 'UserBadge')
    pvs['user_email']              = PV(tomoscan_prefix + 'UserEmail')
    pvs['proposal_number']         = PV(tomoscan_prefix + 'ProposalNumber')
    pvs['proposal_title']          = PV(tomoscan_prefix + 'ProposalTitle')
    pvs['user_info_update_time']   = PV(tomoscan_prefix + 'UserInfoUpdate')
    pvs['experiment_date']         = PV(tomoscan_prefix + 'ExperimentYearMonth')

    # AreaDetector
    camera_prefix = ad_prefix + 'cam1:'
    pvs['CamManufacturer']         = PV(camera_prefix + 'Manufacturer_RBV')
    pvs['CamModel']                = PV(camera_prefix + 'Model_RBV')
    pvs['CamAcquire']              = PV(camera_prefix + 'Acquire')
    pvs['CamAcquireTime']          = PV(camera_prefix + 'AcquireTime')
    pvs['CamAcquireBusy']          = PV(camera_prefix + 'AcquireBusy')
    pvs['CamImageMode']            = PV(camera_prefix + 'ImageMode')
    pvs['CamTriggerMode']          = PV(camera_prefix + 'TriggerMode')
    pvs['CamNumImages']            = PV(camera_prefix + 'NumImages')
    pvs['CamNumImagesCounter']     = PV(camera_prefix + 'NumImagesCounter_RBV')

    # HDF File plugin 
    pvs['FPNumCaptured']           = PV(fp_prefix + 'NumCaptured_RBV')
    pvs['FPFullFileName']          = PV(fp_prefix + 'FullFileName_RBV')
    pvs['FPFullFileName']          = PV(fp_prefix + 'FullFileName_RBV')
    return pvs

def check_pvs_connected(epics_pvs):
    """Checks whether all EPICS PVs are connected.
    Returns
    -------
    bool
        True if all PVs are connected, otherwise False.
    """

    slack_message = ()
    all_connected = True
    for key in epics_pvs:
        if not epics_pvs[key].connected:
            log.error('PV %s is not connected', epics_pvs[key].pvname)
            slack_message += ('\nPV ' + epics_pvs[key].pvname + ' is not connected', )
            all_connected = False
        else:
            log.info('PV %s is connected', epics_pvs[key].pvname)
            slack_message += ('\nPV ' + epics_pvs[key].pvname + ' is connected', )

    return all_connected, slack_message

