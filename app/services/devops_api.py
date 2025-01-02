import requests

class AzureDevOpsAPI:
    def __init__(self, organization, project, pat):
        self.base_url = f"https://dev.azure.com/{organization}/{project}/_apis"
        self.headers = {"Authorization": f"Basic {pat}"}

    def get_work_items(self, ids):
        url = f"{self.base_url}/wit/workitems?ids={','.join(map(str, ids))}&api-version=7.1-preview.3"
        response = requests.get(url, headers=self.headers)
        return response.json() if response.status_code == 200 else None