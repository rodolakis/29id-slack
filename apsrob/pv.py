from epics import PV

def slack_pvs(tomoscan_prefix, fp_prefix):
    
    s_pvs = {}
    s_pvs['user_name'] = PV(tomoscan_prefix + 'UserName')
    s_pvs['user_last_name'] = PV(tomoscan_prefix + 'UserLastName')
    s_pvs['user_affiliation'] = PV(tomoscan_prefix + 'UserInstitution')
    s_pvs['user_badge'] = PV(tomoscan_prefix + 'UserBadge')
    s_pvs['user_email'] = PV(tomoscan_prefix + 'UserEmail')
    s_pvs['proposal_number'] = PV(tomoscan_prefix + 'ProposalNumber')
    s_pvs['proposal_title'] = PV(tomoscan_prefix + 'ProposalTitle')
    s_pvs['user_info_update_time'] = PV(tomoscan_prefix + 'UserInfoUpdate')
    s_pvs['experiment_date'] = PV(tomoscan_prefix + 'ExperimentYearMonth')

    s_pvs['FPNumCaptured']     = PV(fp_prefix + 'NumCaptured_RBV')
    s_pvs['FPFullFileName']    = PV(fp_prefix + 'FullFileName_RBV')
    return s_pvs


