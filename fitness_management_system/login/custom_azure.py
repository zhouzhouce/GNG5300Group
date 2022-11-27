from storages.backends.azure_storage import AzureStorage


class AzureStaticStorage(AzureStorage):
    account_name = 'djangoj'  # Must be replaced by your storage_account_name
    # Must be replaced by your <storage_account_key>
    account_key = 'aWBYUcwLGCECljXb7IvztBsTfiI9VqQhjKn7CjaSGFzPGg0eQtXx75dcoAdXqsOWJgRtfcHJJXEy+ASt1AdavA=='
    azure_container = 'static'
    expiration_secs = None