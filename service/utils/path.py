def get_config_path(service):
    class_path = __file__
    index = class_path.index('service')
    config_path = class_path[:index] + 'service/configs/' + service + '_config.ini'
    return config_path