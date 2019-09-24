from pyhocon import ConfigFactory
configuration = ConfigFactory.parse_file('application.conf')
# datasets = configuration.get('datasets')
