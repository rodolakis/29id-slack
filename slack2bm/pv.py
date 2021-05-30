import time
from epics import PV
from slack2bm import log


def epics_ring(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Ring
    pvs['s_current']                = PV('S:SRcurrentAI')
    pvs['shutter_status']           = PV('PA:02BM:STA_A_FES_OPEN_PL')
    pvs['acis_shutter_permit']      = PV('ACIS:ShutterPermit')
    pvs['s_desired_mode']           = PV('S:DesiredMode')
    pvs['ops_message1']             = PV('OPS:message5')
    pvs['ops_message2']             = PV('OPS:message5')
    pvs['ops_message3']             = PV('OPS:message5')
    pvs['ops_message4']             = PV('OPS:message5')
    pvs['ops_message5']             = PV('OPS:message5')

    return pvs

def epics_eps(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # EPS
    pvs['Fault:Temp:M1']            = PV(eps_prefix + 'Fault:Temp:M1')
    pvs['Fault:Helium_Flow']        = PV(eps_prefix + 'Fault:Helium_Flow')
    pvs['Fault:Water:P6_Shutter']   = PV(eps_prefix + 'Fault:Water:P6_Shutter')
    pvs['Fault:Water:DMM']          = PV(eps_prefix + 'Fault:Water:DMM')
    pvs['Fault:Water:BMA_Window']   = PV(eps_prefix + 'Fault:Water:BMA_Window')
    pvs['Fault:Water:M1']           = PV(eps_prefix + 'Fault:Water:M1')
    pvs['Fault:Water:FilterSlits']  = PV(eps_prefix + 'Fault:Water:FilterSlits')
    pvs['Vacuum:BMB_Slits']         = PV(eps_prefix + 'Vacuum:BMB_Slits')
    pvs['Vacuum:Mini_Hutch_2']      = PV(eps_prefix + 'Vacuum:Mini_Hutch_2')
    pvs['Vacuum:Mini_Hutch_1']      = PV(eps_prefix + 'Vacuum:Mini_Hutch_1')
    pvs['Vacuum:P6_Shutter']        = PV(eps_prefix + 'Vacuum:P6_Shutter')
    pvs['Vacuum:DMM']               = PV(eps_prefix + 'Vacuum:DMM')
    pvs['Vacuum:M1']                = PV(eps_prefix + 'Vacuum:M1')
    pvs['Vacuum:FilterSlits']       = PV(eps_prefix + 'Vacuum:FilterSlits')

    return pvs

def epics_energy(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Energy information
    pvs['energy']                   = PV(tomoscan_prefix + 'Energy')
    pvs['energy_mode']              = PV(tomoscan_prefix + 'EnergyMode')
    pvs['filters']                  = PV(tomoscan_prefix + 'Filters')

    return pvs

def epics_optics(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Optics information
    pvs['scintillator_type']        = PV(tomoscan_prefix + 'ScintillatorType')
    pvs['scintillator_thickness']   = PV(tomoscan_prefix + 'ScintillatorThickness')
    pvs['image_pixel_size']         = PV(tomoscan_prefix + 'ImagePixelSize')
    pvs['detector_pixel_size']      = PV(tomoscan_prefix + 'DetectorPixelSize')
    pvs['camera_objective']         = PV(tomoscan_prefix + 'CameraObjective')
    pvs['camera_tube_lens']         = PV(tomoscan_prefix + 'CameraTubeLength')

    return pvs
    
def epics_sample(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Sample information
    pvs['sameple_name']             = PV(tomoscan_prefix + 'SampleName')
    pvs['sample_description_1']     = PV(tomoscan_prefix + 'SampleDescription1')
    pvs['sample_description_2']     = PV(tomoscan_prefix + 'SampleDescription2')
    pvs['sample_description_3']     = PV(tomoscan_prefix + 'SampleDescription3')

    return pvs
    
def epics_user(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # User information
    pvs['user_name']                = PV(tomoscan_prefix + 'UserName')
    pvs['user_last_name']           = PV(tomoscan_prefix + 'UserLastName')
    pvs['user_institution']         = PV(tomoscan_prefix + 'UserInstitution')
    pvs['user_badge']               = PV(tomoscan_prefix + 'UserBadge')
    pvs['user_email']               = PV(tomoscan_prefix + 'UserEmail')
    pvs['proposal_number']          = PV(tomoscan_prefix + 'ProposalNumber')
    pvs['proposal_title']           = PV(tomoscan_prefix + 'ProposalTitle')
    pvs['esaf_number']              = PV(tomoscan_prefix + 'ESAFNumber')
    pvs['user_info_update']         = PV(tomoscan_prefix + 'UserInfoUpdate')

    return pvs
    
def epics_data(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Data management information
    pvs['detector_top_dir']         = PV(tomoscan_prefix + 'DetectorTopDir')
    pvs['user_last_name']           = PV(tomoscan_prefix + 'UserLastName')
    pvs['experiment_year_month']    = PV(tomoscan_prefix + 'ExperimentYearMonth')
    pvs['remote_data_analysis_dir'] = PV(tomoscan_prefix + 'RemoteAnalysisDir')
    pvs['copy_to_analysis_dir']     = PV(tomoscan_prefix + 'CopyToAnalysisDir')

    return pvs
    
def epics_scan(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Beam status information
    pvs['testing']                  = PV(tomoscan_prefix + 'Testing')

    # Rotation axis
    pvs['rotation_start']           = PV(tomoscan_prefix + 'RotationStart"')
    pvs['rotation_step']            = PV(tomoscan_prefix + 'RotationStep')
    pvs['rotation_stop']            = PV(tomoscan_prefix + 'RotationStop')
    pvs['num_angle']                = PV(tomoscan_prefix + 'NumAngles')
    pvs['return_rotation']          = PV(tomoscan_prefix + 'ReturnRotation')

    # Dark field control
    pvs['num_dark_fields']          = PV(tomoscan_prefix + 'NumDarkFields')
    pvs['dark_field_mode']          = PV(tomoscan_prefix + 'DarkFieldMode')
    pvs['dark_field_value']         = PV(tomoscan_prefix + 'DarkFieldValue')

    # Flat field control
    pvs['num_flat_fields']          = PV(tomoscan_prefix + 'NumFlatFields')
    pvs['flat_field_mode']          = PV(tomoscan_prefix + 'FlatFieldMode')
    pvs['flat_field_axis']          = PV(tomoscan_prefix + 'FlatFieldAxis')
    pvs['flat_field_value']         = PV(tomoscan_prefix + 'FlatFieldValue')
    pvs['sample_in_x']              = PV(tomoscan_prefix + 'SampleInX')
    pvs['sample_out_x']             = PV(tomoscan_prefix + 'SampleOutX')
    pvs['sample_in_y']              = PV(tomoscan_prefix + 'SampleInY')
    pvs['sample_out_y']             = PV(tomoscan_prefix + 'SampleOutY')

    # Scan control
    pvs['move_sample_in']           = PV(tomoscan_prefix + 'MoveSampleIn')
    pvs['move_sample_out']          = PV(tomoscan_prefix + 'MoveSampleOut')
    pvs['start_scan']               = PV(tomoscan_prefix + 'StartScan')
    pvs['abort_scan']               = PV(tomoscan_prefix + 'AbortScan')

    # Scan status 
    pvs['scan_status']              = PV(tomoscan_prefix + 'ScanStatus')
    pvs['images_collected']         = PV(tomoscan_prefix + 'ImagesCollected')
    pvs['images_saved']             = PV(tomoscan_prefix + 'ImagesSaved')
    pvs['elapsed_time']             = PV(tomoscan_prefix + 'ElapsedTime')
    pvs['remaining_time']           = PV(tomoscan_prefix + 'RemainingTime')
    pvs['server_running']           = PV(tomoscan_prefix + 'ServerRunning')

    # Frame type
    pvs['frame_type']               = PV(tomoscan_prefix + 'FrameType')

    return pvs
    
def epics_file(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # File path and name control
    pvs['file_path']                = PV(tomoscan_prefix + 'FilePath')
    pvs['file_name']                = PV(tomoscan_prefix + 'FileName')
    pvs['file_path_exists']         = PV(tomoscan_prefix + 'FilePathExists')
    pvs['overwrite_warning']        = PV(tomoscan_prefix + 'OverwriteWarning')

    # Location for data in HDF5 file
    pvs['hdf5_projection_location'] = PV(tomoscan_prefix + 'HDF5ProjectionLocation')
    pvs['hdf5_dark_location']       = PV(tomoscan_prefix + 'HDF5DarkLocation')
    pvs['hdf5_flat_location']       = PV(tomoscan_prefix + 'HDF5FlatLocation')
    pvs['hdf5_location']            = PV(tomoscan_prefix + 'HDF5Location')

    # HDF File plugin 
    pvs['FPNumCaptured']            = PV(fp_prefix + 'NumCaptured_RBV')
    pvs['FPFullFileName']           = PV(fp_prefix + 'FullFileName_RBV')
    pvs['FPFullFileName']           = PV(fp_prefix + 'FullFileName_RBV')

    return pvs
    
def epics_detector(eps_prefix, tomoscan_prefix, ad_prefix, fp_prefix):

    pvs = {}

    # Exposure time
    pvs['exposure_time']            = PV(tomoscan_prefix + 'ExposureTime')
    pvs['flat_field_time']          = PV(tomoscan_prefix + 'FlatExposureTime')
    pvs['different_flat_exposure']  = PV(tomoscan_prefix + 'DifferentFlatExposure')

    # Detector
    camera_prefix = ad_prefix + 'cam1:'
    pvs['CamManufacturer']          = PV(camera_prefix + 'Manufacturer_RBV')
    pvs['CamModel']                 = PV(camera_prefix + 'Model_RBV')
    pvs['CamAcquire']               = PV(camera_prefix + 'Acquire')
    pvs['CamAcquireTime']           = PV(camera_prefix + 'AcquireTime')
    pvs['CamAcquireBusy']           = PV(camera_prefix + 'AcquireBusy')
    pvs['CamImageMode']             = PV(camera_prefix + 'ImageMode')
    pvs['CamTriggerMode']           = PV(camera_prefix + 'TriggerMode')
    pvs['CamNumImages']             = PV(camera_prefix + 'NumImages')
    pvs['CamNumImagesCounter']      = PV(camera_prefix + 'NumImagesCounter_RBV')

    return pvs

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
        if not epics_pvs[key].connected:
            log.error('PV %s is not connected', epics_pvs[key].pvname)
            slack_messages += ('\nPV ' + epics_pvs[key].pvname + ' is not connected', )
            all_connected = False
        else:
            log.info('%s: %s' % (key, epics_pvs[key].get(as_string=True)))
            slack_messages += ('\n' + key + ': ' + epics_pvs[key].get(as_string=True), )

    return all_connected, slack_messages

