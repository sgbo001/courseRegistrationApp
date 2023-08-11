from storages.backends.azure_storage import AzureStorage

class AzureStaticStorage(AzureStorage):
    account_name = 'c2063081'
    account_key = 'Ce8GO0ugoRfwDfGgE12t9gmwdJt7fUQquK00mQD57Xm00PSMSBY1jJwAel5dqDaWjp3nJ3b1SjVd+AStLO6D1A=='
    azure_container = 'static'
    expiration_secs = None

class AzureMediaStorage(AzureStorage):
    account_name = 'c2063081'
    account_key = 'Ce8GO0ugoRfwDfGgE12t9gmwdJt7fUQquK00mQD57Xm00PSMSBY1jJwAel5dqDaWjp3nJ3b1SjVd+AStLO6D1A=='
    azure_container = 'media'
    expiration_secs = None

