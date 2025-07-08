def extract_change_features(change_log):
    return {
        'files_changed': change_log['files_changed'],
        'lines_added': change_log['lines_added'],
        'lines_removed': change_log['lines_removed'],
        'services_affected': len(change_log['services'])
    }
