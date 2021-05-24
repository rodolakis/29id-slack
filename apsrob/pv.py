from epics import PV

def img_pvs(tomoscan_prefix, fp_prefix):
    
    pvs = {}
    pvs['user_name'] = PV(tomoscan_prefix + 'UserName')
    pvs['user_last_name'] = PV(tomoscan_prefix + 'UserLastName')
    pvs['user_affiliation'] = PV(tomoscan_prefix + 'UserInstitution')
    pvs['user_badge'] = PV(tomoscan_prefix + 'UserBadge')
    pvs['user_email'] = PV(tomoscan_prefix + 'UserEmail')
    pvs['proposal_number'] = PV(tomoscan_prefix + 'ProposalNumber')
    pvs['proposal_title'] = PV(tomoscan_prefix + 'ProposalTitle')
    pvs['user_info_update_time'] = PV(tomoscan_prefix + 'UserInfoUpdate')
    pvs['experiment_date'] = PV(tomoscan_prefix + 'ExperimentYearMonth')

    pvs['FPNumCaptured']     = PV(fp_prefix + 'NumCaptured_RBV')
    pvs['FPFullFileName']    = PV(fp_prefix + 'FullFileName_RBV')
    return pvs


